"""Module entry point for ``python -m runtraj``."""

from runtraj.cli import app


def main() -> None:
    """Run the Typer CLI."""
    app()


if __name__ == "__main__":
    main()
