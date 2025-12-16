#advent of code, day 4
#author: lotusfish

#minimal input processing required for this task
def inputToLists(filename: str) -> list[str]:
	file = open(filename)
	lines = file.readlines()
	return lines

#takes in the data as well as an x and y co-ordinate and returns the number of
#neighbouring rolls
def getRollNeighbours(data: list[str], x:int, y:int, debug=False) -> int:
	neighbours = 0
	DIR_VEC = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
	for vec in DIR_VEC:
		try: #allows out-of-bounds to be handled and treated as a lack of roll rather than error
			if y + vec[0] < 0 or x + vec[1] < 0:
				raise IndexError #python allows negative list indexing but i dont
			
			toCheck = data[y + vec[0]][x + vec[1]]
			if toCheck == "@":
				neighbours += 1
			if debug:
				print(toCheck)
		except IndexError:
			if debug:
				print("*")
			pass 
	return neighbours

testData = {
	"letters"  : ["abc","def","ghi"],
	"allRolls" : ["@@@","@@@","@@@"],
	"allBlank" : ["...","...","..."]
}

