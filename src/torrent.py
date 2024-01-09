import libtorrent as lt
from src.session import Session
from src.download import Download

class Torrent:
    def __init__(self, magnet):
        self._magnet = magnet
        self._select = None
        self._torrent_param = None
        self._session = Session(lt)

    def load_torrent(self):
        self._torrent_param = lt.parse_magnet_uri(self._magnet)
        self._torrent_param.save_path = '.'
        return self._torrent_param

    def list_file(self):
        info = self.load_torrent()

        Download(info, self._session()).listFile()

    def download(self, selected, total):
        priority = []

        for i in range(total):
            if i in selected:
                priority.append(7)
                continue
                
            priority.append(0)

        info = self.load_torrent()
        info.file_priorities = priority
        Download(info, self._session()).download()
