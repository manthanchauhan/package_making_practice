"""
utils
"""


class Proxy(object):
    '''
    Based on http://code.activestate.com/recipes/496741-object-proxying
    version by Tomer Filiba, PSF license.
    '''

    __slots__ = ['_obj', '_name', '_facade']

    def __init__(self, name, facade):
        object.__init__(self)
        object.__setattr__(self, '_obj', None)
        object.__setattr__(self, '_name', name)
        object.__setattr__(self, '_facade', facade)

    def _ensure_obj(self):
        obj = object.__getattribute__(self, '_obj')
        if obj:
            return obj
        # do the import
        try:
            name = object.__getattribute__(self, '_name')
            module = 'plyer.platforms.{}.{}'.format(
                platform, name)
            mod = __import__(module, fromlist='.')
            obj = mod.instance()
        except:  # pylint: disable=bare-except
            import traceback
            traceback.print_exc()
            facade = object.__getattribute__(self, '_facade')
            obj = facade()

        object.__setattr__(self, '_obj', obj)
        return obj

    def __getattribute__(self, name):
        result = None

        if name == '__doc__':
            return result

        # run _ensure_obj func, result in _obj
        object.__getattribute__(self, '_ensure_obj')()

        # return either Proxy instance or platform-dependent implementation
        result = getattr(object.__getattribute__(self, '_obj'), name)
        return result

    def __delattr__(self, name):
        object.__getattribute__(self, '_ensure_obj')()
        delattr(object.__getattribute__(self, '_obj'), name)

    def __setattr__(self, name, value):
        object.__getattribute__(self, '_ensure_obj')()
        setattr(object.__getattribute__(self, '_obj'), name, value)

    def __bool__(self):
        object.__getattribute__(self, '_ensure_obj')()
        return bool(object.__getattribute__(self, '_obj'))

    def __str__(self):
        object.__getattribute__(self, '_ensure_obj')()
        return str(object.__getattribute__(self, '_obj'))

    def __repr__(self):
        object.__getattribute__(self, '_ensure_obj')()
        return repr(object.__getattribute__(self, '_obj'))

    def random(self):
        print('HI')
