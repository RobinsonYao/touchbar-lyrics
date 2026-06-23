# state/app_state.py


class AppState:
    """
    全局状态中心
    """

    def __init__(self):

        # --------------------
        # 当前歌曲
        # --------------------
        self.song_key = None

        # 歌词时间轴
        self.timeline = None

        # 匹配结果
        self.match = None

        # 上一句歌词（避免重复发送）
        self.last_lyric = None

        # 当前歌词
        self.current_lyric = ""

        # --------------------
        # TouchBar 状态
        # --------------------
        self.touchbar_state = "EXPANDED"

        # 用户是否主动收起
        self.user_collapsed = False

    # ====================================
    # Lyric
    # ====================================

    def set_lyric(self, lyric):

        self.current_lyric = lyric

    # ====================================
    # TouchBar State
    # ====================================

    def expand_touchbar(self):

        self.touchbar_state = "EXPANDED"

        self.user_collapsed = False

    def collapse_touchbar(self):

        self.touchbar_state = "COLLAPSED"

        self.user_collapsed = True

    def lost_touchbar(self):

        self.touchbar_state = "LOST"

    def restore_touchbar(self):

        if self.user_collapsed:
            self.touchbar_state = "COLLAPSED"
        else:
            self.touchbar_state = "EXPANDED"