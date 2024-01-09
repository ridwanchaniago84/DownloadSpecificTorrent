import time
import sys

class Download:
    def __init__(self, torrent_info, session):
        self._torrent_info = torrent_info
        self._session = session
        self._file = None

    def status(self):
        self._file = self._session.add_torrent(self._torrent_info)
        self._status = self._file.status()
        return self._status
    
    def listFile(self):
        print(f'Listing {self.status().name}')

        while not self.status().has_metadata:
            time.sleep(1)
        
        info = self.status().torrent_file
        files = info.files()
        numFiles = files.num_files()

        for i in range(numFiles):
            file_entry = files.at(i)
            print(f"Index {i}: {file_entry.path} - {file_entry.size} bytes")

        print(f'Total file: {numFiles}')

    def download(self):
        print(f'Start downloading {self.status().name}')

        while not self._status.is_seeding:
            s = self.status()

            print('\r%.2f%% complete (down: %.1f kB/s up: %.1f kB/s peers: %d) %s' % (
                s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000,
                s.num_peers, s.state), end=' ')
                
            sys.stdout.flush()

            if s.progress == 1:
                break

            time.sleep(1)

        print(f'\n{self._status.name} downloaded successfully.')
