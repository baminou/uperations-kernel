
import kernel
from kernel.documentable import Documentable


class Event(Documentable):

    def __init__(self, operation):
        self._operation = operation
        self.trigger()
        return

    def trigger(self):
        for listener_type in kernel.EVENTS[self.__class__]:
            listener_type(self).handle()
        return