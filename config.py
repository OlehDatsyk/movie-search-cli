"""
config.py
---------
Centralized configuration for the Movie Search CLI application.

This module is responsible for:
    - Loading environment variables from a local .env file (via python-dotenv)
    - Exposing configuration constants used across the application
    - Validating that required configuration (like the API key) is present
      before the rest of the application tries to use it.

Keeping configuration in one place makes the application easier to maintain
and avoids scattering `os.getenv(...)` calls throughout the codebase.
"""

import os
import sys
from dotenv import load_dotenv

# Load variables defined in a .env file (if present) into the process
# environment. This must happen before we try to read any variables below.
load_dotenv()

# ---------------------------------------------------------------------------
# API Configuration
# ---------------------------------------------------------------------------

# Your personal OMDb API key. Get one for free at: https://www.omdbapi.com/apikey.aspx
OMDB_API_KEY = os.getenv("OMDB_API_KEY", "").strip()

# Base URL for the OMDb API. This rarely changes, but is kept configurable
# in case OMDb updates their endpoint or you want to point to a proxy.
OMDB_BASE_URL = os.getenv("OMDB_BASE_URL", "https://www.omdbapi.com/").strip()

# Request timeout (in seconds) for outgoing HTTP requests to the OMDb API.
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "10"))

# ---------------------------------------------------------------------------
# Application Metadata
# ---------------------------------------------------------------------------

APP_NAME = "Movie Search CLI"
APP_VERSION = "1.0.0"


def validate_config() -> None:
    """
    Validate that all required configuration values are present.

    If the OMDb API key is missing, the application cannot function, so we
    print a clear, actionable error message and exit immediately rather than
    letting the program crash later with a confusing stack trace.
    """
    if not OMDB_API_KEY:
        # Import here (not at top-level) to avoid a circular import between
        # config.py and utils.py during module initialization.
        from utils import console, print_error

        print_error(
            "Missing OMDb API key.\n\n"
            "Please create a '.env' file in the project root (you can copy "
            "'.env.example' to get started) and set:\n\n"
            "    OMDB_API_KEY=your_actual_api_key_here\n\n"
            "You can obtain a free API key at: https://www.omdbapi.com/apikey.aspx"
        )
        sys.exit(1)
