import os

print(os.getcwd())
#test
os.chdir('C://Temp')

print(os.getcwd())

os.path.join('F', 'PYTHON')

myFiles = ['teste.txt','felipe.txt', 'theo.txt']
for filename in myFiles:
    #print(os.path.join('C:\\Temp', filename))
    print(os.path.join('F:\\', 'PYTHON', filename))

#os.makedirs('F:\\PYTHON\\MakeDir')