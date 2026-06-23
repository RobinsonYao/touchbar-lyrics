import time
import sys
import threading

from AppKit import NSApplication
from src.player import AppleMusicPlayer
from src.netease_provider import NeteaseProvider
from src.lrc_parser import LRCParser
from src.sync_engine import SyncEngine
from src.cache_manager import CacheManager
from src.output.touchbar_output import TouchBarOutput



# =========================
# STATE
# =========================
class State:
    song_key = None
    timeline = None
    match = None
    last_lyric = None


def build_song_key(track):
    return (
        track["song"],
        track["artist"],
        round(track["duration"])
    )


# =========================
# FAST LOOP (UI)
# =========================
def fast_loop(
        state,
        track,
        output
    ):

    if state.timeline is None:
        return

    lyric = SyncEngine.get_current_lyric(
        state.timeline,
        track["position"]
    )

    if lyric != state.last_lyric:
        output.send(lyric)
        print("SEND:", lyric)
        state.last_lyric = lyric


# =========================
# SLOW LOOP (SYNC)
# =========================
def slow_loop(state, track):

    song_key = build_song_key(track)

    if song_key == state.song_key:
        return

    print("\n[Song Changed]")
    print(track["song"], "-", track["artist"])

    # =====================
    # 1. 先查缓存
    # =====================

    cached_lrc = CacheManager.load_lrc(
        track["song"],
        track["artist"],
        track["duration"]
    )

    if cached_lrc:

        print("[Cache Hit]")

        state.timeline = LRCParser.parse(
            cached_lrc
        )

        state.song_key = song_key
        state.last_lyric = None

        return

    # =====================
    # 2. 网易云搜索
    # =====================

    match = NeteaseProvider.find_best_match(
        track["song"],
        track["artist"],
        track["duration"]
    )

    if not match:
        return

    lyric_data = NeteaseProvider.get_lyric(
        match["id"]
    )

    if not lyric_data:
        return

    if "lrc" not in lyric_data:
        return

    if "lyric" not in lyric_data["lrc"]:
        return

    lyric_text = lyric_data["lrc"]["lyric"]

    # =====================
    # 3. 保存缓存
    # =====================

    CacheManager.save_lrc(
        track["song"],
        track["artist"],
        track["duration"],
        lyric_text
    )

    print("[Cache Saved]")

    # =====================
    # 4. 建立时间轴
    # =====================

    state.timeline = LRCParser.parse(
        lyric_text
    )

    state.match = match
    state.song_key = song_key
    state.last_lyric = None

def run_loop(state, output):

    fast_tick = 0.25
    slow_tick = 3.0

    last_slow = 0

    while True:

        track = AppleMusicPlayer.get_current_track()

        if track is None:
            time.sleep(1)
            continue

        fast_loop(
            state,
            track,
            output
        )

        now = time.time()

        if now - last_slow > slow_tick:

            slow_loop(
                state,
                track
            )

            last_slow = now

        time.sleep(fast_tick)


# =========================
# MAIN LOOP
# =========================
def main():

    CacheManager.init()

    state = State()

    output = TouchBarOutput()

    output.init_touchbar()

    print("\nRealtime Player Started (Stable Mode)\n")

    worker = threading.Thread(
        target=run_loop,
        args=(state, output),
        daemon=True
    )

    worker.start()

    app = NSApplication.sharedApplication()

    app.run()