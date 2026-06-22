# tests/test_lyric.py

from src.netease_provider import NeteaseProvider


def main():

    song_id = 359338

    result = NeteaseProvider.get_lyric(
        song_id
    )

    print(result)


if __name__ == "__main__":
    main()