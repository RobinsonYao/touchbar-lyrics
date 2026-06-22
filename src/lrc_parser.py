"""
lrc_parser.py

Parse LRC lyric format
"""

import re


class LRCParser:

    @staticmethod
    def parse(lrc_text):

        timeline = []

        pattern = re.compile(
            r"\[(\d+):(\d+\.\d+)\](.*)"
        )

        for line in lrc_text.splitlines():

            match = pattern.match(line)

            if not match:
                continue

            minute = int(match.group(1))
            second = float(match.group(2))
            lyric = match.group(3).strip()

            timestamp = minute * 60 + second

            timeline.append(
                {
                    "time": timestamp,
                    "lyric": lyric
                }
            )

        return timeline