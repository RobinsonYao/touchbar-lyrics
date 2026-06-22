import subprocess


class AppleMusicPlayer:

    @staticmethod
    def get_current_track():

        script = """
        tell application "Music"
            if player state is not stopped then
                set trackName to name of current track
                set artistName to artist of current track
                set albumName to album of current track
                set trackPos to player position
                set trackDuration to duration of current track
                return trackName & "||" & artistName & "||" & albumName & "||" & trackPos & "||" & trackDuration
            else
                return "NOT_PLAYING"
            end if
        end tell
        """

        try:
            result = subprocess.run(
                ["osascript", "-e", script],
                capture_output=True,
                text=True,
                timeout=0.8   # ⭐关键
            )

            output = result.stdout.strip()

            if output == "NOT_PLAYING":
                return None

            parts = output.split("||")

            if len(parts) != 5:
                return None

            return {
                "song": parts[0],
                "artist": parts[1],
                "album": parts[2],
                "position": float(parts[3]),
                "duration": float(parts[4])
            }

        except subprocess.TimeoutExpired:
            return None   # ⭐避免卡死整个loop

        except Exception:
            return None