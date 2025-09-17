file =open('output.txt','w')
writing_file= file.write('hello ,Python!')
file.close()

file= open('output.txt','a')
appending_file= file.write('learning file handling in Python')
file.close()

file= open('output.txt','r')
reading_file= file.read()
print(reading_file)
file.close()

