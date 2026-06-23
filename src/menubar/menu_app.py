import threading
import time

from runtime.realtime_player import run_loop
from state.app_state import AppState

from src.output.touchbar_output import TouchBarOutput
from src.cache_manager import CacheManager
from src.menubar.menu_actions import MenuActions


from AppKit import (
    NSApplication,
    NSApplicationActivationPolicyAccessory,
    NSStatusBar,
    NSMenu,
    NSMenuItem
)


class MenuApp:

    def __init__(self):

        self.app = NSApplication.sharedApplication()

        # 真正后台 Agent
        self.app.setActivationPolicy_(
            NSApplicationActivationPolicyAccessory
        )

        # 全局状态
        self.state = AppState()
        self.actions = (
            MenuActions.alloc()
            .initWithApp_(self)
        )
        # MenuBar
        self.status_item = (
            NSStatusBar.systemStatusBar()
            .statusItemWithLength_(-1)
        )
        self.show_expanded()



        # 菜单
        self.menu = NSMenu.alloc().init()

        self.toggle_item = (
            NSMenuItem.alloc()
            .initWithTitle_action_keyEquivalent_(
                "Collapse TouchBar",
                "toggleTouchBar:",
                ""
            )
        )

        self.menu.addItem_(
            self.toggle_item
        )
        self.toggle_item.setTarget_(
            self.actions
        )

        self.menu.addItem_(
            NSMenuItem.separatorItem()
        )

        self.menu.addItem_(
            NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(
                "Quit",
                "terminate:",
                ""
            )
        )

        self.status_item.setMenu_(
            self.menu
        )

    # ----------------------------------
    # Menubar Display
    # ----------------------------------

    def show_expanded(self):

        self.status_item.button().setTitle_(
            "→ 🎵"
        )

    def show_collapsed(self):

        self.status_item.button().setTitle_(
            "↓ 🎵"
        )

    def show_fallback_lyric(self, lyric):

        if not lyric:
            lyric = "..."

        self.status_item.button().setTitle_(
            f"{lyric} ↓ 🎵"
        )


    # ----------------------------------
    # Toggle TouchBar
    # ----------------------------------

    def toggle_touchbar(self):

        if self.state.touchbar_state == "EXPANDED":

            print("[Collapse TouchBar]")

            self.state.collapse_touchbar()

        else:

            print("[Expand TouchBar]")

            self.state.expand_touchbar()

    # ----------------------------------
    # Menubar Refresh
    # ----------------------------------


    def refresh_menubar(self):

        while True:

            if self.state.touchbar_state == "LOST":

                if self.state.user_collapsed:

                    self.show_collapsed()
                    self.toggle_item.setTitle_(
                    "Expand TouchBar"
                )

                else:

                    self.show_fallback_lyric(
                        self.state.current_lyric
                    )
                    self.toggle_item.setTitle_(
                        "Expand TouchBar"
                    )
            elif self.state.touchbar_state == "COLLAPSED":

                self.show_collapsed()
                self.toggle_item.setTitle_(
                "Expand TouchBar"
            )

            else:

                self.show_expanded()
                self.toggle_item.setTitle_(
                    "Collapse TouchBar"
                )
                

            time.sleep(0.2)

    # ----------------------------------
    # Run
    # ----------------------------------

    def run(self):

        CacheManager.init()

        output = TouchBarOutput()

        output.init_touchbar()

        worker = threading.Thread(
            target=run_loop,
            args=(self.state, output),
            daemon=True
        )

        worker.start()

        menubar_worker = threading.Thread(
            target=self.refresh_menubar,
            daemon=True
        )

        menubar_worker.start()

        self.app.run()