from AppKit import (
    NSApplication,
    NSWindow,
    NSTouchBar,
    NSCustomTouchBarItem,
    NSTextField,
    NSMakeRect,
    NSBackingStoreBuffered
)
from Foundation import NSObject


class TouchBarDelegate(NSObject):

    def touchBar_makeItemForIdentifier_(
            self,
            touchBar,
            identifier
    ):
        print("MAKE ITEM:", identifier)

        item = NSCustomTouchBarItem.alloc(
        ).initWithIdentifier_(identifier)

        label = NSTextField.labelWithString_(
            "HELLO TOUCHBAR"
        )

        item.setView_(label)

        return item


class Window(NSWindow):

    def makeTouchBar(self):

        print("MAKE TOUCH BAR")

        bar = NSTouchBar.alloc().init()

        delegate = TouchBarDelegate.alloc().init()

        self._delegate_ref = delegate

        bar.setDelegate_(delegate)

        bar.setDefaultItemIdentifiers_(
            ["hello"]
        )

        return bar


app = NSApplication.sharedApplication()

window = Window.alloc().initWithContentRect_styleMask_backing_defer_(
    NSMakeRect(100, 100, 400, 300),
    15,
    NSBackingStoreBuffered,
    False
)

window.setTitle_("TouchBar Debug")

window.makeKeyAndOrderFront_(None)

app.run()