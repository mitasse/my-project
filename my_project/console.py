"""Command line interface for my-project.

See click documentation at https://click.palletsprojects.com/

"""
import click





@click.group()
@click.version_option()
def run() -> None:
    """Command line interface for my-project."""


@run.command()
def hello() -> None:
    """Command to check my-project is correctly installed."""
    click.echo("Welcome to my-project!")


if __name__ == "__main__":
    run(prog_name="my-project")  # pragma: no cover
