from AppKit import (
    NSApplication,
    NSStatusBar,
    NSMenu,
    NSMenuItem
)

app = NSApplication.sharedApplication()

# 隐藏 Dock
app.setActivationPolicy_(2)

# 菜单栏图标
status_item = NSStatusBar.systemStatusBar().statusItemWithLength_(-1)
status_item.button().setTitle_("🎵")

# 菜单
menu = NSMenu.alloc().init()

menu.addItem_(
    NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(
        "Running",
        None,
        ""
    )
)

menu.addItem_(NSMenuItem.separatorItem())

menu.addItem_(
    NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(
        "Quit",
        "terminate:",
        ""
    )
)

status_item.setMenu_(menu)

app.run()