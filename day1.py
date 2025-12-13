inputFile = open("day1input.txt")
inputText = map(str.rstrip, inputFile.readlines())

dialPointer = 50
totalZeros = 0

for instruction in inputText:
	print(f"About to execute: {instruction}. Dial at: {dialPointer}. Total Zeroes: {totalZeros}")
	#rotate dial as instructed
	if instruction[0] == "R":
		dialPointer -= int(instruction[1:])
	else:
		dialPointer += int(instruction[1:])
	#account for rotation
	dialPointer = dialPointer % 100
	#check if 0
	if dialPointer == 0:
		totalZeros += 1

print(totalZeros)