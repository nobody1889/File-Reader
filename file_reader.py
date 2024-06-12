import os
import shutil
import sys
from typing import Union


class FileReader:
    def __init__(self, defaults: str = None):
        self.defaults = defaults
        self.denied_files: list[Union[int, list[str]]] = []
        self.parameters: dict = {}

    def __start_value(self, start: str):
        if not start:
            return self.defaults if self.defaults else os.getcwd()
        return start

    def count_files(self, parameters_list: list[str], start_from: str = None,
                    _ret: bool = True) -> tuple:  # main file to run
        # {algorithm : recursion}
        start_from = self.__start_value(start_from)
        if _ret:
            self.denied_files: list[Union[int, list[str]]] = [0, ['', ]]
            self.parameters: dict = {key: [] for key in parameters_list}
        if not start_from.endswith('/'):
            start_from += '/'
        try:
            files_list: list[str] = [start_from + file for file in os.listdir(start_from) if
                                     not file.startswith('.')]  # know all files in directory
            for file in files_list:
                for key in self.parameters.keys():
                    if file.endswith(key):
                        self.parameters[key].append(file)
                if os.path.isdir(file) and not os.path.islink(file):  # if file is a directory and not a link
                    # directory check inside
                    self.count_files(parameters_list, start_from=file, _ret=False)
            if _ret:  # some times don't need to return something
                return self.parameters, self.denied_files
        except KeyboardInterrupt:  # when client interrupt the process
            print('Interrupted')
            sys.exit()
        except FileNotFoundError:  # when file not found
            print('File Not Found')
        except PermissionError:  # skip the files which need permission
            self.denied_files[0] += 1
            self.denied_files[1].append(start_from)
        except OSError:
            print(f'OS Error {start_from}')

    def move_files(self, parameters_list: list[str], destination: str, start_from: str = None) -> None:
        def handel_files(name, start_file, end_file) -> tuple:
            counter = 1
            for_now = '1' * 10
            while name + str(counter) in os.listdir(end_file):
                counter += 1
            os.rename(start_file, for_now)
            p = start_file.find(name)
            start_file = name + str(counter) + start_file[p + len(name):]
            return start_file, for_now

        if not os.path.isdir(destination):
            os.makedirs(destination)

        parameters, denied = self.count_files(parameters_list, start_from=start_from)
        for lists in parameters.values():
            for file in lists:
                print(f'Moving {file} to {destination}')
                if (t := file.split('/')[-1].split('.')[0]) not in os.listdir(destination):
                    shutil.move(file, destination)
                file, now = handel_files(t, file, destination)
                shutil.move(now, destination)
                os.chdir(destination)
                os.rename(destination + '/' + now, file)

        print('all files moved to ' + destination)

    def delete(self, parameters_list: list[str], start_from: str = None) -> None:  # be careful when
        parameters, _ = self.count_files(parameters_list=parameters_list, start_from=start_from)
        print(parameters)
        input('Press any key to continue . . .')
        try:
            for lists in parameters.values():
                for file in lists:
                    if os.path.isdir(file):
                        shutil.rmtree(file)
                    else:
                        os.remove(file)
        except PermissionError:
            print('Permission denied try as root')


if __name__ == '__main__':
    print('you can see how many files you have as .pdf or ... ')
