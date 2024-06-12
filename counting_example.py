from file_reader import FileReader

types: list[str] = input('entre file types or names : \n').split(' ')  # client input as list
search = FileReader()  # create the instance

mylist, d = search.count_files(types, start_from=input("ENTER THE START :(don't enter ~ for home)\n"))

# show our output
for key in mylist:
    print(key + ' : ', mylist[key])

num, d_list = d
print('number of denied files :  ', num)
