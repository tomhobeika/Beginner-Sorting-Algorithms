# Stores the data for each word and its count
class Word: 
	def __init__(self, word, count):
		self.word = word
		self.count = count
	def getCount(self):
		return self.count
	def getWord(self):
		return self.word
	def setCount(self,newCount):
		self.count = newCount
	def incrementCount():
		self.count = self.count + 1

# Adds word to both the Word and String lists
def addWord(list, word,test,testWord):
	#index = len(list) - 1
	#list[index] = word
	list.append(word)

	#testIndex = len(test) - 1
	#test[testIndex] = testWord
	test.append(testWord)

# Simple search for a list element's index
def searchIndex(list, element):
	for i in range(len(list)):
		if list[i].getWord() == element:
			return i 

# Takes any non letter characters out of string and returns string
def puncDestroy(word):
	letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	output = ""
	for x in word:
		if x in letters:
			output = output + x
	return output

# Quick Sort algorithm to sort the list by count of word
def quickSort(list):
	def sorter(items, low, high):
		if low < high:
			split = partition(items, low, high)
			sorter(items, low, split)
			sorter(items, split + 1, high)

	sorter(list, 0, len(list)-1)

# Partition method used for Quick Sort to get pivot point
def partition(list,start,end):
	low = start - 1
	high = end + 1

	pivot = list[(low + high) // 2].getCount()
	
	while True:
		low = low + 1
		while list[low].getCount() < pivot:
			low = low + 1

		high = high - 1
		while list[high].getCount() > pivot:
			high = high - 1

		if low >= high:
			return high

		list[low], list[high] = list[high], list[low]

# Bubble Sort to be used on already sorted list to sort alphabetically
def bubbleSort(list):
	i = 0
	j = i + 1
	for x in list:
		if list[i].getCount() == list[j].getCount():
			if list[i].getWord() < list[j].getWord():
				alphSort(list)
		i = i + 1

# Used to swap elements from Bubble Sort
def alphSort(list):
	i = 0
	for x in list:
		j = i + 1
		if j >= len(list):
			return

		if list[i].getCount() == list[j].getCount():
			if list[i].getWord() < list[j].getWord():
				temp = list[i]
				list[i] = list[j]
				list[j] = temp
		i = i + 1

# Displays list in ascending order
def displayAscending(list):
	for x in list:
		print(x.getWord()+": "+str(x.getCount()))

# Displays list in decending order
def displayDescending(list):
	for x in reversed(list):
		print(x.getWord()+": "+str(x.getCount()))

# Displays top and bottom 15 results with amount of unique words
def displayTopAndBot(list):
	x = 0
	print("Top 15 Results:")
	while x < 15:
		j = (len(list) - 1) - x
		print(list[j].getWord()+": "+str(list[j].getCount()))
		x = x + 1

	print("-----------------------")

	i = 15
	print("Bottom 15 Results:")
	while i > 0:
		print(list[i].getWord()+": "+str(list[i].getCount()))
		i = i - 1

	print("-----------------------")

	uniqueWords = str(len(list))

	print("There are {0} unique words in this file.".format(uniqueWords))


#Read and display name of file
filename = input("Please enter the filename: ")
print(filename + " entered!")

#Open file
try:
	f = open(filename, "r", encoding='utf-8')
except:
	print("You didn't enter a valid filename.")
	exit()

#Read lines
splitWords = []	# Temp split string array
wordDict = [] 	# Array of word objects
wordTest = []	# Array of string elements for if passes

lines = f.readlines()

for x in lines: 				# Reads each line
	tempSplit = x.split()		
	for y in tempSplit:			# Reads each word
		tempWord = y.lower()	# Converts to lower case

		tempWord = puncDestroy(tempWord)

		if tempWord in wordTest:# If word is added, finds word in array and increments count
			index = searchIndex(wordDict, tempWord)			
			count = wordDict[index].getCount() + 1
			wordDict[index].setCount(count)
		else: # If word is unique, create an object for it and set count to 1			
			count = 1
			word = Word(tempWord,count)
			addWord(wordDict,word,wordTest,tempWord)
		
		addWord(splitWords,tempWord,wordTest,tempWord)

quickSort(wordDict) 		# Sort by count
bubbleSort(wordDict)		# Sort alphabetically, keeping count in-tact

displayTopAndBot(wordDict) 	# Displays output
