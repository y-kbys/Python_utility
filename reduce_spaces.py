#! /Users/ykobayashi/.pyenv/shims/python
import os
import argparse


def reduce_spaces(input_file_name):
    if input_file_name is None:
        raise TypeError('入力ファイル名を与えてください')
    try:
        input_file_name = os.path.expanduser(input_file_name)
        with open(input_file_name, 'r') as f:
            input_text = f.read()
    except (IOError, TypeError):
        raise FileNotFoundError(str(input_file_name) + ' : file open error.')

    new_text = input_text.replace('  ', ' ')
    new_text = new_text.replace('\n\n\n', '\n\n')
    while new_text != input_text:
        input_text = new_text
        new_text = input_text.replace('  ', ' ')
        new_text = new_text.replace('\n\n\n', '\n\n')

    return new_text


def main():
    parser = argparse.ArgumentParser(description='連続する半角空白文字を一つに置き換える')
    parser.add_argument('input', nargs='?', default=None, help='入力ファイル')
    parser.add_argument('--input_file', '-i', nargs='?', default=None, help='入力ファイル')
    parser.add_argument('--output_file', '-o', nargs='?', default=None, help='出力ファイル')

    args = parser.parse_args()

    input_file_name = args.input_file if args.input_file else args.input

    result_text = reduce_spaces(input_file_name)

    if args.output_file is None:
        output_file = input_file_name
    else:
        output_file = args.output_file

    with open(output_file, 'w') as f:
        f.write(result_text.replace(' }', '}'))


if __name__ == '__main__':
    main()
    print('complete.')
