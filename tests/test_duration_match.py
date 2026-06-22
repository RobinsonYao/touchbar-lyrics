from src.player import AppleMusicPlayer
from src.netease_provider import NeteaseProvider


def main():

    track = AppleMusicPlayer.get_current_track()

    if track is None:
        print("No music playing.")
        return

    print()
    print("Apple Music")
    print("----------------")

    print(track["song"])
    print(track["artist"])
    print(f"{track['duration']:.1f} s")

    print()

    result = NeteaseProvider.search_song(
        track["song"]
    )

    songs = result["result"]["songs"]

    print("NetEase Candidates")
    print("----------------")

    for song in songs[:10]:

        duration = song["duration"] / 1000

        artists = ", ".join(
            a["name"]
            for a in song["artists"]
        )

        print(
            f"{duration:7.1f}s | "
            f"{artists:20s} | "
            f"{song['name']}"
        )


if __name__ == "__main__":
    main()