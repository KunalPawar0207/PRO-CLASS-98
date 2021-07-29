def countWordsFromFile():
    fileName = input("Enter the file name: ")
    numbersOfWords = 0
    file = open(fileName, 'r')
    for line in file:
        words = line.split()
        numbersOfWords = numbersOfWords + len(words)

    print("Number of words: ") 
    print(numbersOfWords)

countWordsFromFile()