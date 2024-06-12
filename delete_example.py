from file_reader import FileReader

types: list[str] = input('entre file types or names : \n').split(' ')  # client input as list
search = FileReader()  # create the instance
start_from = input("ENTER THE START :(don't enter ~ for home)\n")
search.delete(types, start_from=start_from)  # give the start point to search and delete
