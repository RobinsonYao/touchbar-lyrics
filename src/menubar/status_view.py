from objc import super

from AppKit import (
    NSView,
    NSButton,
    NSMakeRect
)


class CustomStatusView(NSView):

    def init(self):

        self = super(
            CustomStatusView,
            self
        ).init()

        if self is None:
            return None

        # Arrow Button
        self.arrow_button = (
            NSButton.alloc()
            .initWithFrame_(
                NSMakeRect(
                    0,
                    0,
                    30,
                    22
                )
            )
        )

        self.arrow_button.setTitle_("→")

        self.addSubview_(
            self.arrow_button
        )

        # Icon Button
        self.icon_button = (
            NSButton.alloc()
            .initWithFrame_(
                NSMakeRect(
                    35,
                    0,
                    30,
                    22
                )
            )
        )

        self.icon_button.setTitle_("🎵")

        self.addSubview_(
            self.icon_button
        )

        return self