"""
lyric_provider.py

Public lyric provider

Functions:
- Search lyric by song and artist
- Return raw LRC text
"""

import requests
from urllib.parse import quote


class LyricProvider:

    @staticmethod
    def get_lyric(song: str, artist: str = "") -> str | None:
        """
        Get lyric from public API

        Parameters
        ----------
        song : str
        artist : str

        Returns
        -------
        str | None
        """

        query = song

        if artist:
            query += f" {artist}"

        url = (
            "https://api.lyrics.ovh/v1/"
            f"{quote(artist)}/{quote(song)}"
        )

        try:

            response = requests.get(
                url,
                timeout=10
            )

            if response.status_code != 200:
                return None

            data = response.json()

            return data.get("lyrics")

        except Exception as e:

            print(f"Lyric API Error: {e}")

            return None