# your code goes here
def main():
    #print("Please enter the input here!")
    #print('yo 001')
    isFirstLine = True
    while True:
    	currNumLines = int(input())
    	if (currNumLines == 0):
    		break
    	#print(currNumLines)
    	#print('yo 002')
    	printTheSeq(currNumLines, isFirstLine)
	isFirstLine = False

def printTheSeq(numOfLine, isFirstLine):
	compArr = []
	#print('yo 003')
	for x in range(numOfLine):
		char = input()
		compArr.append(char)
	printSeq(compArr, isFirstLine)
	if (validate(compArr) != True):
		print('Error decoding image!')
		

def printSeq(compArr, isFirstLine):
	if not isFirstLine:
		print("\n", end='')
	for line in compArr:
		#print(line)
		data = line.split()
		char = data.pop(0)
		for x in data:
			printCurrChar(char, x)
			if (char == '#'):
				char = '.'
			else:
				char = '#'
	print("\n", end='')
	#print("\n", end='')


def printCurrChar(char, x):
	for i in range(int(x)):
		print(char, end="")

def validate(compArr):
	prevTotal = 0
	for line in compArr:
		#print(line)
		data = line.split()
		curTotal = 0
		for da in data:
			if (da.isnumeric()):
				curTotal = curTotal + int(da)
		if (prevTotal == 0):
			prevTotal = curTotal
		elif (prevTotal != curTotal):
			return False
	return True

if __name__=="__main__":
    main()
