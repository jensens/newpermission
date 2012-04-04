from Products.Five import BrowserView

class NewView(BrowserView):

    def __call__(self):
        res = u'New View called, New Permission granted.'

