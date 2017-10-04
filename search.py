from tools import search_for_lyric
import argparse

"""
Searches lyrics.csv for specified lyric. Prints matching song names.
"""

parser = argparse.ArgumentParser()
parser.add_argument('lyric', type=str, help='lyric to search')
args = parser.parse_args()

if __name__ == '__main__':
    print('Songs that contain {}:'.format(args.lyric))
    search_for_lyric(args.lyric)
