# files,

# creating file obj
myFile = open('../file/myFile.txt')

# reading file
print(myFile.read())

print(myFile.read())
# the output above is empyt because the cursor is set to below of file and hence we need to reset cursor

myFile.seek(0)
print(myFile.read())

# so everytime using the file we need to reset the cursor

# converting each line to list, using readLine method
myFile.seek(0)
listLines = myFile.readlines()
print(listLines)

# always close to prevent any errors, other obj cant delete or access

print('Writing to a file')
myFile.seek(0)
# WRITING to files
with open('../file/myFile.txt', mode='a') as myReadFile:
    myReadFile.write('\nAdding fourth line')

# here w is to write, r to read, a to append, r+ to read and write, w+ to write and read

print(myFile.read())

# using w to writing

with open('newWriteFile.txt', mode='w') as f:
    f.write('I wrote it at runtime')
# creates new file if not present, at runtime and writes


myFile.close()
