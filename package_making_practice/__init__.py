"""
My first Package creation (copied version on Pyler)
"""
__all__ = [
    'brightness', 'battery'
]

from package_making_practice.utils import Proxy
from package_making_practice import facades

# create Proxy object to :class: `package_making_practice.facades.Brightness`
brightness = Proxy('brightness', facades.Brightness)
# create Proxy object to :class: `package_making_practice.facades.Battery`
battery = Proxy('battery', facades.Battery)
