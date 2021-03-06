"""
Battery
------
provides battery information of windows PC
usage:
>>> from package_making_practice import battery
>>> battery.status
"""

from package_making_practice.platforms.windows.libs.batterystatus import battery_status


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
        status = {
            "isCharging": None,
            "percentage": None
        }
        query = battery_status()
        if not query:
            return status
        status["isCharging"] = query["BatteryFlag"] == 8
        status['percentage'] = query['BatteryLifePercent']
        return status
