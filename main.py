import argparse
from src.torrent import Torrent

def load_torrent(magnet, section, select, total):
    if section != 'download' and section != 'list':
        return print('Select section download or list.')

    if section == 'list':
        return Torrent(magnet).list_file()
    
    if select is None or total is None:
        return print('Please fill -s and -t')
    
    select = select.split('|')
    selector_int = []

    for i in range(len(select)):
        selector_int.append(int(select[i]))

    selector_int = list(dict.fromkeys(selector_int))

    return Torrent(magnet).download(selector_int, total)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Specific Torrent', add_help=True)
    parser.add_argument('-m', '--magnet', type=str, required=True, help='Magnet torrent')
    parser.add_argument('-s', '--section', type=str, required=True, help='Select download or show list file. enum: download | list')
    parser.add_argument('-p', '--select', type=str, required=False, help='Index selected torrent. ex: 2|5|7')
    parser.add_argument('-t', '--total', type=int, required=False, help='Total file of torrent')
    
    args = parser.parse_args()

    load_torrent(args.magnet, args.section, args.select, args.total)
