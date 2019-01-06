"""
Battery
------
provides battery information of windows PC
usage:
>>> from package_making_practice import battery
>>> battery.status
"""


class Battery(object):
    """
    battery info facade
    """
    @property
    def status(self):
        return self.get_state()

    def get_state(self):
        return self._get_state()

    # private

    def _get_state(self):
        raise NotImplementedError()
