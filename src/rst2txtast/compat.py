import logging

from . import cmd

logger = logging.getLogger(__name__)


def run():
    logger.warning(
        "このCLIは後方互換性維持のために動作させています。極力 'rst2txtast' を使用してください。"  # noqa: E501
    )
    return cmd.run()
