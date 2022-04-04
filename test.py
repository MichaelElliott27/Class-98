def counting():
    fileName=input("enter the file name:")

    countWords=0
    file=open(fileName,'r')
    for line in file:
        words=line.split()
        countWords=countWords+len(words)
    print("CountedWords:")
    print(countWords)   

counting() 