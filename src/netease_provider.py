"""
netease_provider.py

NetEase Music provider
"""

import requests


class NeteaseProvider:

    SEARCH_API = "https://music.163.com/api/search/get"

    @classmethod
    def search_song(
            cls,
            song_name
    ):

        params = {
            "s": song_name,
            "type": 1,
            "offset": 0,
            "limit": 10
        }

        response = requests.get(
            cls.SEARCH_API,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        return response.json()



    @classmethod
    def find_best_match(
            cls,
            song_name,
            artist_name,
            duration=None
    ):

        result = cls.search_song(song_name)

        songs = result["result"]["songs"]

        best_score = -1
        best_song = None

        for song in songs:

            score = 0

            # 歌名
            if song_name in song["name"]:
                score += 50

            # 歌手
            for artist in song["artists"]:

                if artist_name in artist["name"]:
                    score += 30

            # 时长
            if duration is not None:

                netease_duration = song["duration"] / 1000

                diff = abs(
                    netease_duration - duration
                )

                if diff < 1:
                    score += 20

                elif diff < 3:
                    score += 10

                elif diff < 5:
                    score += 5

            if score > best_score:

                best_score = score
                best_song = song

        if best_song:
            return best_song

        if songs:
            return songs[0]

        return None 
    
    @classmethod
    def get_lyric(cls, song_id):

        url = (
            "https://music.163.com/api/song/lyric"
            f"?id={song_id}&lv=1&kv=1&tv=-1"
        )

        response = requests.get(
            url,
            timeout=10
        )

        response.raise_for_status()

        return response.json()