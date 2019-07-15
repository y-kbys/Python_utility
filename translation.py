#! /Users/ykobayashi/.pyenv/shims/python
import argparse
import re
import sys
import unicodedata
from typing import Optional

import pyperclip
import requests
from googletrans import Translator


def _translate_english(string: str):
    url = 'https://translate.google.com/?hl=ja#en/ja/'
    headers = {"User-Agent": "Chrome/58.0.3029.110"}
    params = {'q': string}
    r = requests.get(url, headers=headers, params=params)

    pattern = "TRANSLATED_TEXT=\'(.*?)\'"
    result = re.search(pattern, r.text).group(1)

    return result


def _translate_japanese(string: str):
    url = 'https://translate.google.co.jp/?hl=en#ja/en/'
    headers = {"User-Agent": "Chrome/58.0.3029.110"}
    params = {'q': string}
    r = requests.get(url, headers=headers, params=params)

    pattern = "TRANSLATED_TEXT=\'(.*?)\'"
    result = re.search(pattern, r.text).group(1)

    return result


def is_japanese(string):
    for ch in string:
        try:
            name = unicodedata.name(ch)
        except ValueError:
            continue
        if "CJK UNIFIED" in name or "HIRAGANA" in name or "KATAKANA" in name:
            return True
    return False


def main():
    parser = argparse.ArgumentParser(description='標準入力をGoogle翻訳で和訳')
    parser.add_argument('--input_file', '-i', nargs='?', default=None, help='入力ファイル')
    parser.add_argument('--output_file', '-o', nargs='?', default=None, help='出力ファイル')
    parser.add_argument('--j2e', '-j', action='store_true', help='和文英訳フラグ')

    args = parser.parse_args()

    input_text: Optional[str] = None
    if args.input_file is None:
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

    if not input_text:
        exit(0)

    if args.j2e:
        result_text = Translator().translate(input_text, src="ja", dest="en").text
    elif is_japanese(input_text):
        result_text = Translator().translate(input_text, src="ja", dest="en").text
    else:
        result_text = Translator().translate(input_text, src="en", dest="ja").text

    if args.output_file:
        with open(args.output_file, 'w') as f:
            f.write(result_text)
    else:
        print(result_text + '\n')
        pyperclip.copy(result_text)


if __name__ == '__main__':
    main()
    print('complete.')
