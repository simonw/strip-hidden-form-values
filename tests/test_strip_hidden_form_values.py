from click.testing import CliRunner
from strip_hidden_form_values.cli import cli
import pytest


@pytest.mark.parametrize(
    "html,expected",
    (
        ("", ""),
        # This one should go through unchanged:
        (
            """
    <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1" />
            <title>Title &amp; suchlike</title>
            <link rel="stylesheet" href="css/main.css" />
        </head>
        <body>
            <script src="js/scripts.js"></script>
        </body>
        </html>
    """,
            """
    <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1" />
            <title>Title &amp; suchlike</title>
            <link rel="stylesheet" href="css/main.css" />
        </head>
        <body>
            <script src="js/scripts.js"></script>
        </body>
        </html>
    """,
        ),
        # This should have the hidden input values stripped
        (
            """
    <!DOCTYPE html>
        <html lang="en">
        <body>
            <p>Form:
            <input type="text" name="name" value="default name">
            <input type="hidden" name="hidden_1" value="hidden value 1">
            <input type="HIDDEN" name="hidden&amp;2" value="hidden value 2">
            <input type="HiDDeN" name="hidden_3" value="hidden value 3" />
            <input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="p8nVm4PgVPA" />
        </body>
        </html>
    """,
            """
    <!DOCTYPE html>
        <html lang="en">
        <body>
            <p>Form:
            <input type="text" name="name" value="default name">
            <input type="hidden" name="hidden_1" value="">
            <input type="HIDDEN" name="hidden&amp;2" value="">
            <input type="HiDDeN" name="hidden_3" value="" />
            <input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="" />
        </body>
        </html>
    """,
        ),
    ),
)
@pytest.mark.parametrize("use_stdin", (False, True))
def test_file(tmpdir, html, expected, use_stdin):
    args = []
    input = None
    if not use_stdin:
        filepath = str(tmpdir / "test.html")
        open(filepath, "w").write(html)
        args = [filepath]
    else:
        input = html
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, args, input=input)
        assert result.exit_code == 0
        assert result.output == expected
