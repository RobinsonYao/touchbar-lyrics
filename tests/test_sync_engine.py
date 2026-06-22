from src.netease_provider import NeteaseProvider
from src.lrc_parser import LRCParser
from src.sync_engine import SyncEngine


def main():

    result = NeteaseProvider.get_lyric(
        359338
    )

    lrc_text = result["lrc"]["lyric"]

    timeline = LRCParser.parse(
        lrc_text
    )

    test_times = [
        35,
        50,
        80,
        160,
        220
    ]

    print()

    for t in test_times:

        lyric = SyncEngine.get_current_lyric(
            timeline,
            t
        )

        print(
            f"{t:6.1f}s -> {lyric}"
        )

    print()


if __name__ == "__main__":
    main()