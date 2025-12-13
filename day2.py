#Read in the input for the puzzle
puzzleInput = open("day2input.txt").read().split(",")
puzzleInputSplit = []
for i in range(len(puzzleInput)):
	splitRange = puzzleInput[i].split("-")
	puzzleInputSplit.append([int(splitRange[0]), int(splitRange[1])])

#Takes in an ID, checks if it is valid or not
def checkValidity(id: int) -> bool:
	#all invalid IDs have to be even in length
	if len(str(id)) % 2 != 0:
		return True
	
	#here, all IDs will be even, and can be split in two and compared
	stringId = str(id)
	digits = len(stringId)
	halfDigits = digits // 2
	halves = [
		stringId[:halfDigits],
		stringId[halfDigits:]
	]
	if halves[0] == halves[1]:
		return False
	else:
		return True

#Finds all invalid IDs within a given range
def findInvalidIdInRange(start: int, stop: int) -> list[int]:
	invalidIds = []
	for i in range(start, stop):
		if checkValidity(i) == False:
			invalidIds.append(i)
	return invalidIds

#Finally, find the sum of all invalid IDs
def sumInvalidIdsInRangeList(rangeList: list[list[int]]) -> int:
	totalSum = 0
	for idRange in rangeList:
		totalSum += sum(findInvalidIdInRange(idRange[0], idRange[1]))

	return totalSum

#Main sequence of code
print(sumInvalidIdsInRangeList(puzzleInputSplit))