from file_reader import FileReader

types: list[str] = input('entre file type : \n').split(' ')  # client input as list
search = FileReader(types)  # create the instance

mylist = search.count_files(start_from=input("ENTER THE START :(don't enter ~ for home)\n"))  # give the start point

# show our output
for key in mylist:
    print(key, mylist[key])

print(search.checked_files_list)
print(search.checked_files_number)
