from AppKit import (
    NSApplication,
    NSApplicationActivationPolicyProhibited,
    NSStatusBar,
    NSMenu,
    NSMenuItem
)


class MenuApp:

    def __init__(self):

        self.app = NSApplication.sharedApplication()

        # 真正后台 Agent
        self.app.setActivationPolicy_(
            NSApplicationActivationPolicyProhibited
        )

        # 菜单栏图标
        self.status_item = NSStatusBar.systemStatusBar().statusItemWithLength_(-1)
        self.status_item.button().setTitle_("🎵")

        # 菜单
        self.menu = NSMenu.alloc().init()

        self.menu.addItem_(
            NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(
                "Running",
                None,
                ""
            )
        )

        self.menu.addItem_(NSMenuItem.separatorItem())

        self.menu.addItem_(
            NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(
                "Quit",
                "terminate:",
                ""
            )
        )

        self.status_item.setMenu_(self.menu)

    def run(self):

        self.app.run()