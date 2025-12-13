import math
inputFile = open("day1input.txt")
puzzleInput = inputFile.readlines()

siteExample = [
	"L68",
	"L30",
	"R48",
	"L5",
	"R60",
	"L55",
	"L1",
	"L99",
	"R14",
	"L82"
]

def executeOneStep(start: int, instruction: str) -> tuple[int, int]:
	zeroesRecorded = 0
	modification = parseLine(instruction)
	final = start + modification

	#count clicks
	if final >= 100:
		zeroesRecorded += final // 100
	if final == 0:
		zeroesRecorded += 1
	if final < 0 and start != 0:
		zeroesRecorded += abs(math.ceil(final / 100)) + 1
	
	final = final % 100

	return (final, zeroesRecorded)

def parseLine(line: str) -> int:
	mult = 1
	if line[0] == "L":
		mult = -1
	
	return int(line[1:]) * mult

def puzzle(inputText: list[str], debug = False):
	dialPointer = 50
	totalZeros = 0
	for instruction in inputText:
		outcome = executeOneStep(dialPointer, instruction)
		dialPointer = outcome[0]
		totalZeros += outcome[1]
		if debug:
			print(f"Executed command: {instruction}. Dial now at {dialPointer}. Total zeroes at {totalZeros}")
	return totalZeros

print(executeOneStep(50, "L150"))
print(puzzle(puzzleInput))