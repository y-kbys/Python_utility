import argparse


def print_2to3(input_file_name: str = None, output_file_name: str = None) -> int:
    if input_file_name is None:
        input_file_name = input('Please enter a input file name.')

    try:
        with open(input_file_name, 'r') as f:
            input_lines = f.readlines()
    except IOError:
        print(input_file_name + ' does not exist.')
        return -1

    if output_file_name is None:
        output_file_name = input_file_name

    with open(output_file_name, 'w') as f:
        for line in input_lines:
            if line.find('print ') != -1:
                line = line.replace('print ', 'print(')
                line = line.replace('\n', ')\n')
            f.write(line)

    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='python main.py')
    parser.add_argument('--input_file', '-i', nargs='?', help='Specify input file')
    parser.add_argument('--output_file', '-o', nargs='?', help='Specify output file')

    args = parser.parse_args()

    print_2to3(input_file_name=args.input_file, output_file_name=args.output_file)

    print('complete!')
