#! /Users/ykobayashi/.pyenv/shims/python
import argparse
import os
import sys

import pyperclip


def replace_n2space(input_file_name: str = None):
    if input_file_name is None:
        print('input text here.')
        input_text = sys.stdin.read()
    else:
        try:
            input_file_name = os.path.expanduser(input_file_name)
            with open(input_file_name, 'r') as f:
                input_text = f.read()
        except (IOError, TypeError):
            raise FileNotFoundError(str(input_file_name) + ' : file open error.')

    return input_text.replace('\n', ' ')


def main():
    parser = argparse.ArgumentParser(description='改行文字を半角スペースに置き換える')
    parser.add_argument('--input_file', '-i', nargs='?', default=None, help='入力ファイル')
    parser.add_argument('--output_file', '-o', nargs='?', default=None, help='出力ファイル')

    args = parser.parse_args()

    result_text = replace_n2space(args.input_file)

    if args.output_file:
        with open(args.output_file, 'w') as f:
            f.write(result_text)
    else:
        print('\n---------------------------------------------------------\n')
        print(result_text + '\n')
        pyperclip.copy(result_text + '\n')


if __name__ == '__main__':
    main()
    print('complete.')
