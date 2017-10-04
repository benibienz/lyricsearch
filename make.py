from tools import make_lyric_file
import argparse

"""
Finds google play lyrics for acapellas and creates a csv of lyric sets.
Input path to directory containing audio files with song names.
Example filename: aretha_franklin-a_deeper_love.mp3
Generates lyrics.csv file in current directory.
"""

parser = argparse.ArgumentParser()
parser.add_argument('path', type=str, help='path to dir of acapellas')
args = parser.parse_args()

if __name__ == '__main__':
    make_lyric_file(args.path)