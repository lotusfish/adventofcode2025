#advent of code, day 4
#author: lotusfish

#minimal input processing required for this task
def inputToLists(filename: str) -> list[str]:
	file = open(filename)
	lines = file.readlines()
	return lines

#takes in the data as well as an x and y co-ordinate and returns the number of
#neighbouring rolls
def getRollNeighbours(data: list[str], x:int, y:int) -> int:
	neighbours = 0
	DIR_VEC = [[0, 1], [1, 0], [1, 1], [-1, 0], [0, -1], [1, -1], [-1, 1], [-1, -1]]
	for vec in DIR_VEC:
		try:
			toCheck = data[x + vec[0]][y + vec[1]]
			if toCheck == "@":
				neighbours += 1
		except:
			pass #ensures out-of-bounds errors just do nothing instead of crashing
	return neighbours

testData = [
	".@.",
	"...",
	"..."
]

print(getRollNeighbours(testData, 0, 0))
