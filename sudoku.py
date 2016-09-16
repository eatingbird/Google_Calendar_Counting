# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               

def check_if_in_list(fromList, toList):
    # for each element to check
    there=[]
    notThere=[]
    length = len(toList)

    counter = length-1
    for eList in fromList:
        if eList in toList:
            there.append(eList)
            counter-=1
        else:
            notThere.append(eList)
            counter-=1

    if len(there) == length:
        return True
    else:
        return False


def repeat_list_comparison(fromList, toList):
    length = len(toList)
    counter = length-1
    eCount = 0
    while counter>=0:
        if check_if_in_list(fromList, toList[counter]) == True:
            eCount+=1
            counter -=1
        else:
            counter -=1
    
    if eCount == length:
        return True
    else:
        return False

def take_last_out(input):
    length = len(input)
    input2=input
    cList =[]
    a=0

    cCounter=length-1
    while cCounter>=0:
        a=input2[cCounter].pop()
        cList.append(a)
        cCounter-=1
    else:
        return cList, input2 #supposed to be empty list

def check_sudoku(input):
    # make a full list of things to check
    length = len(input)
    n = length
    list = []
    while n>0:
        list.append(n)
        n-=1

    # Check rows
    row = repeat_list_comparison(list, input)
    if row == False:
        return False
    else:    # Check column
    
        #set up the Column list    
        totalList=[]
        dcounter = length-1
        while dcounter>=0:
            cList= take_last_out(input)
            totalList.append(cList[0])
            dcounter-=1

    column = repeat_list_comparison(list, totalList)
    if column == False:
        return False
    else:    # Check column
        return True


        
    
    
print check_sudoku(incorrect)
#>>> False

print check_sudoku(correct)
#>>> True

print check_sudoku(incorrect2)
#>>> False

print check_sudoku(incorrect3)
#>>> False

print check_sudoku(incorrect4)
#>>> False

print check_sudoku(incorrect5)
#>>> False
