from AppKit import NSObject
from objc import super

from AppKit import (
    NSApplication,
    NSWindow,
    NSMakeRect,
    NSBackingStoreBuffered,
    NSTouchBar,
    NSCustomTouchBarItem,
    NSTextField
)

from Foundation import NSObject

from .output_base import OutputBase


# =========================
# Window (TouchBar Owner)
# =========================
class TouchBarWindow(NSWindow):

    def initWithLabel_(self, label):

        self = super(TouchBarWindow, self).init()
        self.label = label
        return self

    def makeTouchBar(self):
        print("MAKE TOUCH BAR")
        bar = NSTouchBar.alloc().init()

        bar.setDelegate_(self)

        bar.setDefaultItemIdentifiers_(["lyric"])

        return bar

    def touchBar_makeItemForIdentifier_(self, touchBar, identifier):

        item = NSCustomTouchBarItem.alloc().initWithIdentifier_(identifier)

        item.setView_(self.label)

        return item


# =========================
# Output
# =========================
class TouchBarOutput(OutputBase):

    def __init__(self):

        self.app = None
        self.window = None
        self.label = None
        self._initialized = False

    def init_touchbar(self):

        if self._initialized:
            return


        self.label = NSTextField.labelWithString_("...")

        self.window = TouchBarWindow.alloc().initWithContentRect_styleMask_backing_defer_(
            NSMakeRect(-10000, -10000, 1, 1),
            15,
            NSBackingStoreBuffered,
            False
        )

        self.window.label = self.label

        self.window.setTitle_("TouchBar Lyrics")

        #self.window.makeKeyAndOrderFront_(None)
        self.window.makeFirstResponder_(self.window)
        #self.window.becomeKeyWindow()
        self.window.orderFrontRegardless()
        self.window.setAlphaValue_(0)

        self.window.setIgnoresMouseEvents_(True)

        self._initialized = True
        self.window.setContentView_(self.window.contentView())

    def send(self, text):

        if not text:
            return

        self.label.setStringValue_(text)