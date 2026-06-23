from AppKit import (
    NSApplication,
    NSWindow,
    NSCustomTouchBarItem,
    NSTextField,
    NSTouchBar
)
from Foundation import NSObject


class TouchBarDelegate(NSObject):

    def touchBar_makeItemForIdentifier_(
            self,
            touchBar,
            identifier
    ):

        item = NSCustomTouchBarItem.alloc().initWithIdentifier_(
            identifier
        )

        label = NSTextField.labelWithString_(
            "HELLO TOUCHBAR"
        )

        item.setView_(label)

        return item


class WindowDelegate(NSObject):

    def touchBar(self):

        bar = NSTouchBar.alloc().init()

        bar.setDelegate_(TouchBarDelegate.alloc().init())

        bar.setDefaultItemIdentifiers_(
            ["hello"]
        )

        return bar


app = NSApplication.sharedApplication()

window = NSWindow.alloc().init()

delegate = WindowDelegate.alloc().init()

window.setDelegate_(delegate)

window.makeKeyAndOrderFront_(None)

app.run()