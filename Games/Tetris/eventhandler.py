from events import Events

class EventHandler(Events):
    __events__ = ('on_left', 'on_right', 'on_update')