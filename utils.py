"""
utils.py
--------
Shared utility functions and a shared Rich Console instance used across the
application for consistent, professional-looking terminal output.

Having a single shared `console` object ensures that all output (tables,
panels, error messages, etc.) is rendered consistently and respects the
same terminal width, color system, etc.
"""

from typing import Optional

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

# A single shared Console instance used throughout the entire application.
console = Console()


def print_error(message: str) -> None:
    """Print a formatted error message inside a red panel."""
    console.print(
        Panel.fit(
            f"[bold white]{message}[/bold white]",
            title="[bold red]Error[/bold red]",
            border_style="red",
            padding=(1, 2),
        )
    )


def print_warning(message: str) -> None:
    """Print a formatted warning message inside a yellow panel."""
    console.print(
        Panel.fit(
            f"[bold white]{message}[/bold white]",
            title="[bold yellow]Warning[/bold yellow]",
            border_style="yellow",
            padding=(1, 2),
        )
    )


def print_info(message: str) -> None:
    """Print a formatted informational message inside a blue panel."""
    console.print(
        Panel.fit(
            f"[white]{message}[/white]",
            title="[bold cyan]Info[/bold cyan]",
            border_style="cyan",
            padding=(1, 2),
        )
    )


def print_success(message: str) -> None:
    """Print a formatted success message inside a green panel."""
    console.print(
        Panel.fit(
            f"[bold white]{message}[/bold white]",
            title="[bold green]Success[/bold green]",
            border_style="green",
            padding=(1, 2),
        )
    )


def clean_value(value: Optional[str]) -> str:
    """
    Normalize values returned by the OMDb API.

    OMDb frequently returns the literal string "N/A" for fields that have
    no data. This helper converts such values (and empty/None values) into
    a consistent, human-friendly placeholder so the UI never shows a raw
    "N/A" string inconsistently mixed with real data.
    """
    if value is None:
        return "Not available"
    value = value.strip()
    if value == "" or value.upper() == "N/A":
        return "Not available"
    return value


def build_details_table(movie: dict) -> Table:
    """
    Build a Rich Table that neatly presents all requested movie details:
    release year, runtime, genres, director, actors, IMDb rating, plot,
    poster URL, country, language, and awards.
    """
    table = Table(
        show_header=False,
        box=None,
        padding=(0, 1),
        expand=True,
    )
    table.add_column("Field", style="bold cyan", no_wrap=True, ratio=1)
    table.add_column("Value", style="white", ratio=3)

    rows = [
        ("Title", clean_value(movie.get("Title"))),
        ("Release Year", clean_value(movie.get("Year"))),
        ("Runtime", clean_value(movie.get("Runtime"))),
        ("Genres", clean_value(movie.get("Genre"))),
        ("Director", clean_value(movie.get("Director"))),
        ("Actors", clean_value(movie.get("Actors"))),
        ("IMDb Rating", f"{clean_value(movie.get('imdbRating'))} / 10"),
        ("Country", clean_value(movie.get("Country"))),
        ("Language", clean_value(movie.get("Language"))),
        ("Awards", clean_value(movie.get("Awards"))),
        ("Poster URL", clean_value(movie.get("Poster"))),
        ("Plot", clean_value(movie.get("Plot"))),
    ]

    for field, value in rows:
        table.add_row(field, value)

    return table
