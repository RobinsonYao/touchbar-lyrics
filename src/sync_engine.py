"""
sync_engine.py

Lyric synchronization engine
"""


class SyncEngine:

    @staticmethod
    def get_current_lyric(
        timeline,
        current_time
    ):

        current_lyric = ""

        for item in timeline:

            if item["time"] <= current_time:
                current_lyric = item["lyric"]
            else:
                break

        return current_lyric