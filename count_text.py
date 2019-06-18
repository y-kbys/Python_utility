import argparse
from pathlib import Path


def count_text(input_file_name=None):
    input_file_name = Path(input_file_name).expanduser().resolve()
    try:
        with input_file_name.open(mode='r') as f:
            input_text = f.read()
    except (IOError, TypeError):
        print(str(input_file_name) + ' : file open error.')
        return -1

    print(len(input_text.replace('\n', '').replace(' ', '')))

    return len(input_text.replace('\n', '').replace(' ', ''))


def main():
    parser = argparse.ArgumentParser(description='count_text(input_file_name) : 入力ファイルの文字数を返します')
    parser.add_argument('input_file', '--input_file', '-i', nargs='?', default=None, help='Specify input file')

    args = parser.parse_args()

    count_text(input_file_name=args.input_file)

    print('complete.')


if __name__ == '__main__':
    main()
