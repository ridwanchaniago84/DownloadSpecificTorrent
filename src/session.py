class Session:
    def __init__(self, libTorrent):
        self._lt = libTorrent
        self._session = None

    def create_session(self):
        self._session = self._lt.session({'listen_interfaces': '0.0.0.0:6881'})
        return self._session

    def __call__(self):
        return self.create_session()