import click


@click.group()
@click.version_option()
def cli():
    "CLI tool for stripping hidden form values from an HTML document"


@cli.command(name="command")
@click.argument(
    "example"
)
@click.option(
    "-o",
    "--option",
    help="An example option",
)
def first_command(example, option):
    "Command description goes here"
    click.echo("Here is some output")
