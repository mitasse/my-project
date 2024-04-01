"""Tests for command-line interface."""

from click.testing import CliRunner

from my_project import __version__
from my_project import console


def test_command_line_interface_default() -> None:
    """Test the default CLI."""
    runner = CliRunner()
    result = runner.invoke(console.run)
    assert result.exit_code == 0


def test_command_line_interface_help() -> None:
    """Test the default CLI."""
    runner = CliRunner()
    help_result = runner.invoke(console.run, ["--help"])
    assert help_result.exit_code == 0
    assert "--help     Show this message and exit." in help_result.output


def test_command_line_interface_version() -> None:
    """Test the default CLI."""
    runner = CliRunner()
    version_result = runner.invoke(console.run, ["--version"])
    assert version_result.exit_code == 0
    assert __version__ in version_result.output


def test_command_line_interface_hello() -> None:
    """Test the default CLI."""
    runner = CliRunner()
    help_result = runner.invoke(console.run, ["hello"])
    assert help_result.exit_code == 0
    assert "Welcome to my-project!" in help_result.output
