import os
import argparse


def count_text(input_file_name=None):
    try:
        input_file_name = os.path.expanduser(input_file_name)
        with open(input_file_name, 'r') as f:
            input_text = f.read()
    except (IOError, TypeError):
        print(str(input_file_name) + ' : file open error.')
        return -1

    print(len(input_text.replace('\n', '').replace(' ', '')))

    return len(input_text.replace('\n', '').replace(' ', ''))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='count_text(input_file_name) : 入力ファイルの文字数を返します')
    parser.add_argument('--input_file', '-i', nargs='?', default=None, help='Specify input file')

    args = parser.parse_args()

    count_text(input_file_name=args.input_file)

    print('complete.')
