"""
Brightness
"""


class Brightness(object):
    """
    Brightness facade
    """
    def current_level(self):
        return self._current_level()

    def set_level(self, level):
        return self._set_level(level)

    # private

    def _current_level(self):
        raise NotImplementedError()

    def _set_level(self, level):
        raise NotImplementedError()
