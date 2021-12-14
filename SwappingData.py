def SwapFileData():
    file_1=input("Enter the file name")
    file_2=input("Enter the file name")
    with open(file_1, 'r') as A:
        data_A=A.read()
    with open(file_2, 'r') as B:
        data_B=B.read()
    with open(file_1, 'w') as A:
        A.write(data_B)
    with open(file_2, 'w') as B:
        B.write(data_A)

SwapFileData()
print("The files has been swapped")
