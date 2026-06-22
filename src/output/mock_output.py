from .output_base import OutputBase


class MockOutput(OutputBase):

    def send(self, text):

        print(
            f"[OUTPUT] {text}"
        )