from math import floor, sqrt
#Read in the input for the puzzle
puzzleInput = open("day2input.txt").read().split(",")
puzzleInputSplit = []
for i in range(len(puzzleInput)):
	splitRange = puzzleInput[i].split("-")
	puzzleInputSplit.append([int(splitRange[0]), int(splitRange[1])])

#splits a string (though here it's used for casted ints) into n equal chunks
#assumes that the len(a) % n == 0
def splitIntoNChunks(a: str, n: int) -> list[str]:
	chunkLength = len(a) // n
	chunks = ["" for i in range(n)]
	for i in range(n):
		chunks[i], a = a[:chunkLength], a[chunkLength:]
	return chunks

#Takes ID, checks if it's valid
def checkValidity(id: int, debug = False) -> bool:
	idStr = str(id)
	for i in range(2, len(idStr)+1):
		if len(idStr) % i == 0:
			chunks = splitIntoNChunks(idStr, i)
			equal = all(x == chunks[0] for x in chunks)
			if debug:
				print(f"idStr: {idStr}, chunks: {chunks}, {equal}")
			if equal:
				return False
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