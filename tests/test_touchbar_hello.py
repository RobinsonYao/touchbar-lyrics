from Cocoa import (
    NSApplication,
    NSWindow,
    NSMakeRect,
    NSBackingStoreBuffered
)

app = NSApplication.sharedApplication()

window = NSWindow.alloc().initWithContentRect_styleMask_backing_defer_(
    NSMakeRect(100, 100, 300, 200),
    15,
    NSBackingStoreBuffered,
    False
)

window.setTitle_("TouchBar Test")

window.makeKeyAndOrderFront_(None)

print("Window Created")

app.run()