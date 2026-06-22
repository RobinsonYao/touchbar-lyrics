"""
test_lyric_provider.py
"""

from src.lyric_provider import LyricProvider


def main():

    song = "Hotel California"
    artist = "Eagles"

    lyric = LyricProvider.get_lyric(
        song=song,
        artist=artist
    )

    if lyric is None:

        print("No lyric found.")
        return

    print()
    print("Lyric Preview")
    print("---------------------")

    print(lyric[:1000])

    print()


if __name__ == "__main__":
    main()