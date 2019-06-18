#! /Users/ykobayashi/.pyenv/shims/python
import argparse
from pathlib import Path


def reduce_spaces(input_file_name):
    if input_file_name is None:
        raise TypeError('入力ファイル名を与えてください')
    input_file_name = Path(input_file_name).expanduser().resolve()
    try:
        with input_file_name.open(mode='r') as f:
            input_text = f.read()
    except FileNotFoundError as e:
        print(f'{e.strerror}: {e.filename}')

    new_text = input_text.replace('  ', ' ')
    new_text = new_text.replace('\n\n\n', '\n\n')
    while new_text != input_text:
        input_text = new_text
        new_text = input_text.replace('  ', ' ')
        new_text = new_text.replace('\n\n\n', '\n\n')

    return new_text


def main():
    parser = argparse.ArgumentParser(description='連続する半角空白文字を一つに置き換える')
    parser.add_argument('input_file', '--input_file', '-i', nargs='?', default=None, help='入力ファイル')
    parser.add_argument('--output_file', '-o', nargs='?', default=None, help='出力ファイル')

    args = parser.parse_args()

    input_file_name = args.input_file

    result_text = reduce_spaces(input_file_name)

    output_file = args.output_file if args.output_file is not None else input_file_name

    with open(output_file, 'w') as f:
        f.write(result_text.replace(' }', '}'))


if __name__ == '__main__':
    main()
    print('complete.')
