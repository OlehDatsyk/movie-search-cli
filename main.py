"""
main.py
-------
Entry point for the Movie Search CLI application.

This script provides two modes of operation:

    1. Direct search mode (non-interactive):
       python main.py "Inception" --year 2010

    2. Interactive mode (menu-driven, beginner friendly):
       python main.py

Interactive mode is recommended for first-time users, especially those
running the app for the first time inside VS Code's integrated terminal.
"""

import argparse
import sys

from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

import config
from movie_service import (
    InvalidAPIKeyError,
    MovieNotFoundError,
    MovieService,
    MovieServiceError,
    NetworkError,
)
from utils import build_details_table, console, print_error, print_info, print_warning


def print_banner() -> None:
    """Display the application's welcome banner."""
    console.print(
        Panel.fit(
            f"[bold cyan]{config.APP_NAME}[/bold cyan] "
            f"[dim]v{config.APP_VERSION}[/dim]\n"
            "[white]Search for any movie and view detailed information "
            "powered by the OMDb API.[/white]",
            border_style="cyan",
            padding=(1, 2),
        )
    )


def display_movie(movie: dict) -> None:
    """Render a single movie's full details in a formatted panel/table."""
    title = movie.get("Title", "Unknown Title")
    year = movie.get("Year", "")

    console.print()
    console.print(
        Panel(
            build_details_table(movie),
            title=f"[bold green]{title} ({year})[/bold green]",
            border_style="green",
            padding=(1, 2),
        )
    )
    console.print()


def display_search_results(results: list) -> None:
    """Render a compact table of multiple search results."""
    table = Table(
        title="Search Results",
        show_lines=False,
        header_style="bold cyan",
        border_style="cyan",
    )
    table.add_column("#", justify="right", style="dim", no_wrap=True)
    table.add_column("Title", style="bold white")
    table.add_column("Year", justify="center")
    table.add_column("IMDb ID", style="dim")

    for idx, item in enumerate(results, start=1):
        table.add_row(
            str(idx),
            item.get("Title", "Unknown"),
            item.get("Year", "N/A"),
            item.get("imdbID", "N/A"),
        )

    console.print(table)


def run_single_search(service: MovieService, title: str, year: str = "") -> None:
    """Look up one movie by title (and optional year) and display it."""
    try:
        with console.status(f"[cyan]Searching for '{title}'...[/cyan]"):
            movie = service.get_movie_by_title(title, year=year)
        display_movie(movie)
    except MovieNotFoundError:
        print_warning(
            f"No movie found matching '{title}'"
            + (f" ({year})" if year else "")
            + ".\n\nTip: Double-check the spelling, or try searching without "
            "the release year."
        )
    except InvalidAPIKeyError as exc:
        print_error(str(exc))
        sys.exit(1)
    except NetworkError as exc:
        print_error(str(exc))
    except MovieServiceError as exc:
        print_error(f"An unexpected error occurred: {exc}")


def interactive_mode(service: MovieService) -> None:
    """Run a friendly, menu-driven loop for users unfamiliar with CLI flags."""
    print_banner()
    print_info(
        "Type a movie title to search, or type 'exit' at any time to quit."
    )

    while True:
        console.print()
        query = Prompt.ask("[bold cyan]Enter a movie title[/bold cyan]").strip()

        if not query:
            print_warning("Please enter a non-empty movie title.")
            continue

        if query.lower() in {"exit", "quit", "q"}:
            console.print("\n[bold cyan]Goodbye! 🎬[/bold cyan]\n")
            break

        year = Prompt.ask(
            "[bold cyan]Release year[/bold cyan] [dim](optional, press Enter to skip)[/dim]",
            default="",
            show_default=False,
        ).strip()

        run_single_search(service, query, year=year)


def build_arg_parser() -> argparse.ArgumentParser:
    """Configure the argparse CLI for non-interactive usage."""
    parser = argparse.ArgumentParser(
        prog="main.py",
        description=(
            f"{config.APP_NAME} - Search for movies and view detailed "
            "information (release year, runtime, genres, director, actors, "
            "IMDb rating, plot, poster URL, country, language, and awards)."
        ),
    )
    parser.add_argument(
        "title",
        nargs="?",
        default=None,
        help="The movie title to search for. If omitted, interactive mode starts.",
    )
    parser.add_argument(
        "-y",
        "--year",
        default="",
        help="Optional 4-digit release year to narrow down the search.",
    )
    parser.add_argument(
        "-s",
        "--search",
        action="store_true",
        help="List multiple matching results instead of a single best match.",
    )
    return parser


def main() -> None:
    config.validate_config()
    service = MovieService()

    parser = build_arg_parser()
    args = parser.parse_args()

    if args.title is None:
        interactive_mode(service)
        return

    print_banner()

    if args.search:
        try:
            with console.status(f"[cyan]Searching for '{args.title}'...[/cyan]"):
                results = service.search_movies(args.title)
            if not results:
                print_warning(f"No results found for '{args.title}'.")
            else:
                display_search_results(results)
        except InvalidAPIKeyError as exc:
            print_error(str(exc))
            sys.exit(1)
        except NetworkError as exc:
            print_error(str(exc))
        except MovieServiceError as exc:
            print_error(f"An unexpected error occurred: {exc}")
    else:
        run_single_search(service, args.title, year=args.year)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n\n[bold cyan]Interrupted. Goodbye! 🎬[/bold cyan]\n")
        sys.exit(0)
