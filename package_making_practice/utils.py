class Proxy(object):
    """creates a Proxy object for the facade
    """
    def __init__(self, name, facade):
        self._obj = None
        self._name = name
        self._facade = facade

