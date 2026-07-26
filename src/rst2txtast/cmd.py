from docutils.core import publish_cmdline

from . import writer


def run():
    publish_cmdline(writer=writer.ASTWriter())
