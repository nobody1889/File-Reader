from file_reader import FileReader

types: list[str] = input('entre file type : \n').split(' ')  # client input as list
search = FileReader(types)  # create the instance
start_from = input("ENTER THE START :(don't enter ~ for home)\n")
destination = input("ENTER THE DESTINATION :\n")
search.move_files(start_from=start_from, destination=destination)  # give the start point and end
print('searched files :  ', search.checked_files_number)
for file in search.checked_files_list:
    print(file)

