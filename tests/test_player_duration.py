from src.player import AppleMusicPlayer


def main():

    track = AppleMusicPlayer.get_current_track()

    if track is None:
        print("No music playing.")
        return

    print()
    print("Current Track")
    print("---------------------")
    print(f"Song     : {track['song']}")
    print(f"Artist   : {track['artist']}")
    print(f"Album    : {track['album']}")
    print(f"Position : {track['position']:.1f} s")
    print(f"Duration : {track['duration']:.1f} s")
    print()


if __name__ == "__main__":
    main()