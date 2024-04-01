"""Tests for command-line interface."""

from click.testing import CliRunner

from my_project import __version__
from my_project.cli import cli


def test_command_line_interface_default() -> None:
    """Test the default CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.cli)
    assert result.exit_code == 0


def test_command_line_interface_help() -> None:
    """Test the default CLI."""
    runner = CliRunner()
    help_result = runner.invoke(cli.cli, ["--help"])
    assert help_result.exit_code == 0
    assert "--help     Show this message and exit." in help_result.output


def test_command_line_interface_version() -> None:
    """Test the default CLI."""
    runner = CliRunner()
    version_result = runner.invoke(cli.cli, ["--version"])
    assert version_result.exit_code == 0
    assert __version__ in version_result.output


def test_command_line_interface_hello() -> None:
    """Test the default CLI."""
    runner = CliRunner()
    help_result = runner.invoke(cli.cli, ["hello"])
    assert help_result.exit_code == 0
    assert "Welcome to my-project!" in help_result.output
