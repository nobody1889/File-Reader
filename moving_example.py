from file_reader import FileReader

types: list[str] = input('entre file type : \n').split(' ')  # client input as list
search = FileReader()  # create the instance
start_from = input("ENTER THE START :(don't enter ~ for home)\n")
destination = input("ENTER THE DESTINATION :\n")
search.move_files(parameters_list=types, start_from=start_from, destination=destination)  # give the start point and end
size = len(search.parameters.keys())
print('searched files :  ', size)
for lists in search.parameters.values():
    for file in lists:
        print(file)
