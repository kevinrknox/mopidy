from mopidy.mixers import BaseMixer

class DummyMixer(BaseMixer):
    def __init__(self):
        self._volume = None

    def _get_volume(self):
        return self._volume

    def _set_volume(self, volume):
        self._volume = volume
