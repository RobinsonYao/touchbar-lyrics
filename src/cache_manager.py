from pathlib import Path


class CacheManager:

    CACHE_DIR = Path("cache/lyrics")

    @classmethod
    def init(cls):

        cls.CACHE_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

    @classmethod
    def build_filename(
            cls,
            song,
            artist,
            duration
    ):

        safe_song = song.replace("/", "_")
        safe_artist = artist.replace("/", "_")

        return (
            cls.CACHE_DIR /
            f"{safe_artist}_{safe_song}_{round(duration)}.lrc"
        )

    @classmethod
    def load_lrc(
            cls,
            song,
            artist,
            duration
    ):

        file = cls.build_filename(
            song,
            artist,
            duration
        )

        if file.exists():
            return file.read_text(
                encoding="utf-8"
            )

        return None

    @classmethod
    def save_lrc(
            cls,
            song,
            artist,
            duration,
            content
    ):

        file = cls.build_filename(
            song,
            artist,
            duration
        )

        file.write_text(
            content,
            encoding="utf-8"
        )