import os
from yachalk import chalk
class FileInfo:
    def __init__(self, filename, root):
        self.filename = filename
        self.root = root
        self.line_count = 0

    def get_line_count(self):
        location = os.path.join(self.root, self.filename)
        try:
            with open(location, 'r') as file_to_count:
                self.line_count = len(file_to_count.readlines())
        except UnicodeDecodeError as error:
            print(chalk.red('\n> Error on file') + chalk.red.bold(' '+self.filename) +f': '+ chalk.magenta(error))

        return self.line_count

    def should_ignore(self, ignore_items):
        return any([ignore_name in os.path.join(self.root, self.filename) for ignore_name in ignore_items])

    def should_ignore_name(self, ignore_elements):
        return any([(ignore_item in os.path.join(self.root, self.filename)) for ignore_item in ignore_elements ])

    def __str__(self):
        name_dots = (self.filename+' ').ljust(35, '.')
        justified_number = ('.' * (6-len(str(self.line_count)))) + ' '+chalk.cyan(self.line_count)

        return name_dots + justified_number
