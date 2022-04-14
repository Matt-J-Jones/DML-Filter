from os import walk

#List of files in tree
fTree = []

#populate fTree with list of filenames
for (dirpath, dirnames, filenames) in walk("./"):
    fTree.extend(filenames)
    break

#remove the python file from filelist
fTree.remove('filter.py')

#list of characters to remove from file
schar = ["(", ")", "-", "_", "*", ]

#loops through text files in folder, cleaning them all
for name in fTree:
    fileToStrip = name

    f = open(fileToStrip , "r", encoding="utf8")

    #list of characters to remove from file
    schar = ["(", ")", "-", "_", "*", ]

    #import entire text document and load into memory
    for i in f.readlines():

        #convert to string, strip out whitespace
        str(i)
        i = i.strip()

        #remove characters from text line by line
        for x in schar:
            i = i.replace(x, "")

        #creates new file with "_" to designate it's been stripped
        newName = "_" + fileToStrip
        with open(newName, "a+", encoding = 'utf-8') as f2:
            f2.write(i)
            f2.write("\n")