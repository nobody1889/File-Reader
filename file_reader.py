import os


class FileReader:
    def __init__(self, parameters: list[str]):
        self.start_from = None  # to see where you are (for now useless)
        self.parameters: dict = {key: 0 for key in parameters}  # take what kind of parameters client needs as dict to
        # count them
        self.parameters_keys: list[str] = parameters  # for compare
        self.checked_files_number: int = 0  # count how many file checked
        self.checked_files_list: list[str] = []  # memorise which files checked

    def count_files(self, start_from: str) -> dict:  # main file to run {algorithm : recursion}
        files_list: list[str] = [start_from + file for file in os.listdir(start_from) if
                                 not file.startswith('.')]  # know all files in directory
        for file in files_list:
            if os.path.isdir(file):  # if file is a directory check inside
                self.count_files(start_from="".join(file + "/"))
                self.checked_files_list.append(file)
            else:  # else check is what i seek for or not
                for key in self.parameters_keys:
                    if file.endswith(key):
                        self.parameters[key] += 1
                self.checked_files_number += 1
        return self.parameters  # i will think about it latter


if __name__ == '__main__':
    print('you can see how many files you have as .pdf or ... ')
