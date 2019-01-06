"""
Module of windows API for plyer.battery
"""

from package_making_practice.platforms.windows.libs.batterystatus import battery_status
from package_making_practice.facades import Battery


class WinBattery(Battery):
    """
    implementation of windows battery API
    """

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


def instance():
    """
    instance for facade proxy
    :return:
    """
    return WinBattery()
