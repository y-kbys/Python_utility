#! /Users/ykobayashi/.pyenv/shims/python
import argparse
import re
import sys
from typing import Optional

import mojimoji
import pyperclip
from googletrans import Translator

from translation import is_japanese


def main():
    parser = argparse.ArgumentParser(description='論文を翻訳したい。')
    parser.add_argument('--input_file', '-i', nargs='?', default=None, help='入力ファイル')
    parser.add_argument('--output_file', '-o', nargs='?', default=None, help='出力ファイル')
    parser.add_argument('--clipboard', '-c', action='store_true', help='クリップボードから入力')
    parser.add_argument('--j2e', '-j', action='store_true', help='和文英訳フラグ')

    args = parser.parse_args()

    input_text: Optional[str] = None
    if args.clipboard:
        input_text = pyperclip.paste()
        print(input_text)
    elif args.input_file is None:
        print('input text here.')
        input_text = sys.stdin.read()
    else:
        try:
            with open(args.input_file, 'r') as f:
                input_text = f.read()
        except FileNotFoundError as e:
            print(f'{e.strerror}: {e.filename}')

    print('\n---------------------------------------------------------\n')

    input_text = input_text.replace('\n', ' ')
    input_text = re.sub(r' \[[0-9, ]*\]', '', input_text)
    input_text = re.sub(r'et al.', 'et al', input_text)
    input_text = input_text.replace('. ', '.\n')
    input_text = input_text.replace('- ', '')

    if not input_text:
        exit(0)
    else:
        print(input_text)
        print()

    if args.j2e:
        result_text = Translator().translate(input_text, src="ja", dest="en").text
    elif is_japanese(input_text):
        result_text = Translator().translate(input_text, src="ja", dest="en").text
    else:
        result_text = Translator().translate(input_text, src="en", dest="ja").text

    result_text = mojimoji.zen_to_han(result_text, kana=False)  # 全角の数字とアルファベットを半角に

    if args.output_file:
        with open(args.output_file, 'w') as f:
            f.write(result_text)
    else:
        print(result_text + '\n')
        pyperclip.copy(result_text)  # クリップボードにコピー


if __name__ == '__main__':
    main()
    print('complete.')
