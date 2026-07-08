"""
movie_service.py
-----------------
Service layer responsible for communicating with the OMDb API.

This module isolates all HTTP/network logic away from the CLI (main.py),
following a clean separation of concerns:
    - main.py handles user interaction and presentation
    - movie_service.py handles data retrieval and error handling

Custom exceptions are used so that main.py can catch specific, meaningful
error conditions (e.g. "movie not found" vs. "network error") instead of
generic exceptions.
"""

from typing import Any, Dict, List

import requests

import config


class MovieServiceError(Exception):
    """Base exception for all movie service related errors."""


class MovieNotFoundError(MovieServiceError):
    """Raised when the OMDb API cannot find a movie matching the query."""


class InvalidAPIKeyError(MovieServiceError):
    """Raised when the OMDb API rejects the configured API key."""


class NetworkError(MovieServiceError):
    """Raised when a network-level failure prevents reaching the OMDb API."""


class MovieService:
    """
    A thin, well-behaved client around the OMDb API.

    Example:
        service = MovieService()
        movie = service.get_movie_by_title("Inception", year="2010")
        results = service.search_movies("Batman")
    """

    def __init__(self) -> None:
        self.base_url = config.OMDB_BASE_URL
        self.api_key = config.OMDB_API_KEY
        self.timeout = config.REQUEST_TIMEOUT
        self.session = requests.Session()

    def _request(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Perform a GET request against the OMDb API and return the parsed
        JSON body. Raises MovieServiceError subclasses on any failure.
        """
        params = {**params, "apikey": self.api_key}

        try:
            response = self.session.get(
                self.base_url, params=params, timeout=self.timeout
            )
        except requests.exceptions.Timeout as exc:
            raise NetworkError(
                "The request to the OMDb API timed out. Please check your "
                "internet connection and try again."
            ) from exc
        except requests.exceptions.ConnectionError as exc:
            raise NetworkError(
                "Could not connect to the OMDb API. Please check your "
                "internet connection and try again."
            ) from exc
        except requests.exceptions.RequestException as exc:
            raise NetworkError(f"An unexpected network error occurred: {exc}") from exc

        if response.status_code != 200:
            raise NetworkError(
                f"The OMDb API returned an unexpected HTTP status code: "
                f"{response.status_code}."
            )

        try:
            data = response.json()
        except ValueError as exc:
            raise MovieServiceError(
                "The OMDb API returned a response that could not be parsed "
                "as JSON."
            ) from exc

        # OMDb signals errors via a "Response": "False" field rather than
        # HTTP status codes, so we must inspect the payload itself.
        if data.get("Response") == "False":
            error_message = data.get("Error", "Unknown error from OMDb API.")

            if "Invalid API key" in error_message:
                raise InvalidAPIKeyError(
                    "The configured OMDb API key is invalid. Please check "
                    "the OMDB_API_KEY value in your .env file."
                )
            if "Movie not found" in error_message:
                raise MovieNotFoundError(error_message)

            raise MovieServiceError(error_message)

        return data

    def get_movie_by_title(self, title: str, year: str = "") -> Dict[str, Any]:
        """
        Fetch full details for a single movie by exact/closest title match.

        Args:
            title: The movie title to search for.
            year:  Optional 4-digit release year to disambiguate results.

        Returns:
            A dictionary containing the full movie record as returned by OMDb.
        """
        params = {"t": title, "plot": "full", "type": "movie"}
        if year:
            params["y"] = year

        return self._request(params)

    def search_movies(self, title: str) -> List[Dict[str, Any]]:
        """
        Search for multiple movies matching a (possibly partial) title.

        Returns:
            A list of lightweight movie summaries (Title, Year, imdbID, Type,
            Poster) as returned by OMDb's search endpoint.
        """
        params = {"s": title, "type": "movie"}
        data = self._request(params)
        return data.get("Search", [])
