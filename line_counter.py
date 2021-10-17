import os
from FileInfoClass import FileInfo
from yachalk import chalk

def main():
    print('   --  ' + chalk.cyan('Line Counter') + ' --')

    # location = "/Users/diego/Documents/Personal_Documents/code_review/mock_series/lib"
    # location = '/Users/diego/Documents/Projects/probably'
    # location = '/Users/diego/Documents/Projects/moneyEnvios'
    location = '/Users/diego/Documents/work/capicua/wurrly/frontend'
    ignore_list = get_ignore_list()
    count_lines(location, ignore_list)


def get_ignore_list():
    with open('./ignore', 'r') as ignore_file:
        ignore_list = [line.strip() for line in ignore_file.readlines()]
    return ignore_list


def count_lines(project_path, exclude):
    counted_files = 0
    total_lines = 0
    empty_lines = 0 # todo: implement this

    for root, _, files in os.walk(project_path):
        # print(root)
        for dir_file in files:
            info = FileInfo(dir_file, root)

            if not info.should_ignore(exclude):
                count = info.get_line_count()
                total_lines += count
                counted_files += 1
                print(info)
    print()
    print(f'''
Project {chalk.blue(project_path)}

Total files: {chalk.blue(counted_files)}
Total lines: {chalk.blue(total_lines)}
''')


if __name__ == "__main__":
    main()
