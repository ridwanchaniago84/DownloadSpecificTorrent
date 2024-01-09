# Download Specific Torrent
This is CLI Python Program for download specific file from torrent
## Installation
```
pip install -r requirements.txt
```
## Usage
### Listing file torrent
```
python main.py -m "MAGNET" -s "list"
```
### Download File
```
python main.py -m "MAGNET" -s "download" -p "INDEXFILE" -t "TOTALFILE"
```
## Arguments
Argument | Description
--- | ---
-m | Magnet of your torrent file.
-s | Select section menu. enum: download \\| list
-p | The index file will be downloaded. ex: 2\\|5\\|7
-t | Total file of torrent
## License
[MIT](https://github.com/ridwanchaniago84/DownloadSpecificTorrent/blob/main/LICENSE)
