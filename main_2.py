import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', '-name', help='org name', required=True)

args = parser.parse_args()

name = args.n

if __name__ == '__main__':
    pass