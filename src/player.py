"""
player.py

Apple Music interface layer

Functions:
- Read current song
- Read artist
- Read album
- Read playback position
"""

import subprocess


class AppleMusicPlayer:

    @staticmethod
    def get_current_track():
        """
        Get current playing track info.

        Returns
        -------
        dict

        Example
        -------
        {
            "song": "海阔天空",
            "artist": "Beyond",
            "album": "乐与怒",
            "position": 35.6
        }
        """

        script = """
        tell application "Music"

            if player state is playing then

                set trackName to name of current track
                set artistName to artist of current track
                set albumName to album of current track
                set trackPos to player position

                return trackName & "||" & artistName & "||" & albumName & "||" & trackPos

            else

                return "NOT_PLAYING"

            end if

        end tell
        """

        result = subprocess.run(
            ["osascript", "-e", script],
            capture_output=True,
            text=True
        )

        output = result.stdout.strip()

        if output == "NOT_PLAYING":
            return None

        parts = output.split("||")

        if len(parts) != 4:
            return None

        return {
            "song": parts[0],
            "artist": parts[1],
            "album": parts[2],
            "position": float(parts[3])
        }