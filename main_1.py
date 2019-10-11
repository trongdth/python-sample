import argparse
import json
from bl.news import update_feed, search

parser = argparse.ArgumentParser()
parser.add_argument('-c', '-command', help='command', required=True)
parser.add_argument('-a', '-author', help='author', required=False)
parser.add_argument('-s', '-source', help='source', required=False)

args = parser.parse_args()

command = args.c
author = args.a
source = args.s

if __name__ == '__main__':
    if command in ['update', 'search']:
        if command == 'update':
            res = update_feed(country='vn') 
            if res:
                print 'ok'
            else:
                print 'nok'

        elif command == 'search':
            res = search(author=author, source=source)
            for r in res:
                print r.to_string()
    else:
        print 'invalid command'