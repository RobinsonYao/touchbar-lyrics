from Foundation import NSObject


class MenuActions(NSObject):

    def initWithApp_(self, app):

        self = self.init()

        if self is None:
            return None

        self.app = app

        return self

    def toggleTouchBar_(self, sender):

        self.app.toggle_touchbar()