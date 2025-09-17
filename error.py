
try:
    file = open('sample.txt','r')
    read_file= file.read('sample text file')
    print(read_file)
    file.close()
except  FileNotFoundError:
    print('This is a sample text file.\nIt contains multiple lines.')
finally:
    print("Error: The file 'sample.txt' was not found.")



