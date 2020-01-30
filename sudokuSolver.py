grid=[[6,2,0,9,0,0,7,0,0],
	  [4,1,9,0,0,0,0,0,0],
	  [0,0,0,0,1,2,0,0,0],
	  [0,0,0,0,0,0,2,0,0],
	  [0,0,0,6,5,0,0,0,0],
	  [3,6,0,0,0,0,0,0,0],
	  [0,0,4,2,0,3,0,0,9],
	  [0,0,0,0,0,9,1,0,0],
	  [5,0,6,0,0,0,0,0,4]]

emptySpaces = []

indexCounter = 0

auxVar = 0

number = 1

auxArr =[]

#This function checks for any empty cell in the grid and saves its index
#on an auxiliary array
def checkEmptySpaces(array):
	for i in range(len(grid)):
		for j in range(0,len(grid[0])):
			if(grid[i][j]==0):
				return (i,j)


#Checks row to see if a certain number is already present on a certain row
def usedInRow(array,row,number):
	if number in array[row]:
		return True
	else:
		return False

#Checks column to see if a certain number is already present on a certain column
def usedInColumn(array,column,number):
	for i in range(len(array)):
		if (array[i][column]==number): return True
	return False

#Checks corresponding box/subgrid of empty cell to see if a certain number
#already exists
def usedInBox(array, cellRow, cellColumn,number):
	#Checks through the box to see if the number we want to put is in another cell
	for i in range(3):
		for j in range(3):
			if (array[i + (cellRow-(cellRow % 3))][j + (cellColumn-(cellColumn % 3))] == number): 
				return True
	return False

#Function to check if it is safe to use a number on a specific cell
def isSafeToUse(array, rowPos, colPos, number):
	if (usedInRow(array, rowPos, number) or usedInColumn(array, colPos, number) or usedInBox(array, rowPos, colPos, number)):
		return False
	return True
	 

def solveSudoku(array):

	emptySpace = checkEmptySpaces(array)

	if not emptySpace:
		return True
	else:
		row, col = emptySpace

	for number in range(1,10):
		if isSafeToUse(array, row, col, number):
			array[row][col] = number
			
			if (solveSudoku(array)):
				return True
			array[row][col] = 0

	return False

		
				



for i in grid:
	print(i)
print("\n")

"""
print(emptySpaces)
print(usedInRow(grid,1,5))
print(usedInColumn(grid,1,5))
print(usedInBox(grid,1,1,4))
print(safeToUse(grid,1,1,5))

#solveSudoku(indexCounter,grid, emptySpaces)
print(isSafeToUse(grid, emptySpaces[5][0], emptySpaces[5][1], 2))
print(usedInRow(grid, 0, 2))
print(usedInColumn(grid, 1, 2))
print(usedInBox(grid,0,1,2))
"""
solveSudoku(grid)
for i in grid:
	print(i)
print("\n")