from AppKit import (
    NSApplication,
    NSApplicationActivationPolicyAccessory,
    NSApplicationActivationPolicyProhibited,
    NSStatusBar,
    NSMenu,
    NSMenuItem
)

app = NSApplication.sharedApplication()

# 尝试真正 Agent 模式
app.setActivationPolicy_(NSApplicationActivationPolicyProhibited)

status_item = NSStatusBar.systemStatusBar().statusItemWithLength_(-1)
status_item.button().setTitle_("🎵")

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