#advent of code 2025: day 3 part 1
#author: lotusfish
#this is probably the least efficient possible implementation but i dont care

#takes a filename and returns an array of banks
def processInputFromFile(fileName: str) -> list[int]:
	file = open(fileName)
	banks = file.readlines()
	banks = list(map(int, banks))
	return banks

#gets all valid pairs of two activated batteries in a bank
def pairsFromBank(bank: int) -> list[int]:
	pairs = []
	bankStr = str(bank)
	for i in range(len(bankStr)):
		for j in range(len(bankStr)):
			if j > i:
				pairs.append(int(bankStr[i] + bankStr[j]))
	
	return pairs

#takes a list of banks and returns the sum of the largest joltages of each
def maxJoltageFromBanks(banks: list[int]) -> int:
	maxJoltage = 0
	for bank in banks:
		maxJoltage += max(pairsFromBank(bank))
	
	return maxJoltage

print(maxJoltageFromBanks(processInputFromFile("day3input.txt")))