def swapFileData():
    file1 = input('enter your file name')
    file2 = input('enter your file name')

    with open(file1, 'r') as a:
        data_a = a.read()

    with open(file2, 'r') as a:
        data_b = a.read()

    with open(file1, 'w') as a:
        a.write(data_a)

    with open(file2, 'w') as a:
        a.write(data_b)

    

