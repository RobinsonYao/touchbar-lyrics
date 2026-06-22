import sys

from .output_base import OutputBase


class TerminalOutput(OutputBase):

    def send(self, text):

        sys.stdout.write(
            "\033[2K\r" + text
        )

        sys.stdout.flush()