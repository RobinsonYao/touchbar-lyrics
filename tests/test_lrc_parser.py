from src.netease_provider import NeteaseProvider
from src.lrc_parser import LRCParser


def main():

    result = NeteaseProvider.get_lyric(
        359338
    )

    lrc_text = result["lrc"]["lyric"]

    timeline = LRCParser.parse(
        lrc_text
    )

    print()

    for item in timeline[:10]:

        print(
            f"{item['time']:8.2f}  "
            f"{item['lyric']}"
        )

    print()


if __name__ == "__main__":
    main()