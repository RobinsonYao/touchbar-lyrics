from src.player import AppleMusicPlayer
from src.netease_provider import NeteaseProvider


def main():

    track = AppleMusicPlayer.get_current_track()

    song = NeteaseProvider.find_best_match(
        track["song"],
        track["artist"],
        track["duration"]
    )

    print()
    print("BEST MATCH")
    print("----------")

    print(song["id"])
    print(song["name"])
    print(song["artists"][0]["name"])
    print(song["duration"] / 1000)


if __name__ == "__main__":
    main()