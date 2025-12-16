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
	DIR_VEC = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
	for vec in DIR_VEC:
		try: #allows out-of-bounds to be handled and treated as a lack of roll rather than error
			if y + vec[0] < 0 or x + vec[1] < 0:
				raise IndexError #python allows negative list indexing but i dont
			
			toCheck = data[y + vec[0]][x + vec[1]]
			if toCheck == "@":
				neighbours += 1
		except IndexError:
			pass 
	return neighbours

#takes in the puzzle, returns a solution
def solve(data: list[str], threshold=4) -> int:
	accessibleRolls = 0
	foundAt = []
	for y in range(len(data)):
		for x in range(len(data[y])):
			if getRollNeighbours(data, x, y) < threshold and data[y][x] == "@":
				accessibleRolls += 1
				foundAt.append((y, x))
	return accessibleRolls

#takes in the puzzle, returns a solution following the rules of step 2
def solvePart2(data: list[str], threshold=4) -> int:
	workingData = data
	totalRolls = 0
	while True:
		rollsThisIteration = 0
		for y in range(len(data)):
			for x in range(len(data[y])):
				if getRollNeighbours(workingData, x, y) < threshold and workingData[y][x] == "@":
					totalRolls += 1
					rollsThisIteration += 1
					workingData[y] = workingData[y][:x] + "." + workingData[y][x+1:] #removes roll
		if rollsThisIteration == 0: #quits out if no changes are made - no more rolls can be removed
			break
	return totalRolls


testData = {
	"letters"  : ["abc","def","ghi"],
	"allRolls" : ["@@@","@@@","@@@"],
	"allBlank" : ["...","...","..."],
	"site"     : ["..@@.@@@@.", "@@@.@.@.@@", "@@@@@.@.@@", "@.@@@@..@.", "@@.@@@@.@@", ".@@@@@@@.@", ".@.@.@.@@@", ".@@@@@@@@.", "@.@.@@@.@."]
}

puzzleInput = inputToLists("day4input.txt")

print(solvePart2(testData["site"]))