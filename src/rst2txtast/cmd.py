from docutils.core import publish_cmdline

from . import writer


def run():
    publish_cmdline(
        writer=writer.ASTWriter(),
        # To disable include other files.
        settings_overrides={
            "file_insertion_enabled": False,
        },
    )
