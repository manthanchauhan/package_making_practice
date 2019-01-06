"""
helper of plyer.battery
"""

__all__ = [
    'battery_status'
]

import ctypes
from package_making_practice.platforms.windows.libs import win_api_defs


def battery_status():
    """
    implementation of windows API
    :return:
    """
    status = win_api_defs.SYSTEM_POWER_STATUS()
    if not win_api_defs.GetSystemPowerStatus(ctypes.pointer(status)):
        raise Exception('Cannot get battery status')
    return dict(
        (field, getattr(status, field))
        for field, _ in status._fields_
    )