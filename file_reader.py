import os
import shutil
import sys


class FileReader:
    def __init__(self, parameters: list[str]):
        self.start_from = None  # to see where you are (for now useless)
        self.parameters: dict = {key: 0 for key in parameters}  # take what kind of parameters client needs as dict to count them
        self.parameters_keys: list[str] = parameters  # for compare
        self.parameters_count_all: int = 0  # count all parameters for some needs
        self.checked_files_number: int = 0  # count how many file checked
        self.checked_files_list: list[str] = []  # memorise which files checked

    def count_files(self, start_from: str) -> dict:  # main file to run {algorithm : recursion}
        files_list: list[str] = [start_from + file for file in os.listdir(start_from) if not file.startswith('.')]  # know all files in directory
        for file in files_list:
            for key in self.parameters_keys:
                if file.endswith(key) or file == key:
                    self.parameters[key] += 1
                    self.parameters_count_all += 1
                    self.checked_files_list.append(file)
            self.checked_files_number += 1
            if os.path.isdir(file):  # if file is a directory check inside
                self.count_files(start_from="".join(file + "/"))
        return self.parameters

    def move_files(self, start_from: str, destination: str) -> None:
        self.count_files(start_from=start_from)
        if input(f'{self.parameters_count_all} files to move from {start_from} to {destination}\nare you sure you want to continue? (Y/n)') in ['y', 'Y', '\n']:
            for file in self.checked_files_list:
                print(f'Moving {file} to {destination}')
                shutil.move(file, destination)
            print('all files moved to ' + destination)
        else:
            sys.exit('presses stopped')


if __name__ == '__main__':
    print('you can see how many files you have as .pdf or ... ')
