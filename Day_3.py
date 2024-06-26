'''
2. Write a Python function to sum four numbers
Sample List : (5, 6, 1, 2)
Expected Output : 14
'''
def sumFourNumbers(int1,int2,int3,int4):
    sum = int1 + int2 + int3 + int4 
    return sum


def myMainFunction():
    helenAge = 5
    timAge = 6
    jonAge = 1
    ceceAge = 2
    sum_of_their_ages = sumFourNumbers(helenAge,timAge,jonAge,ceceAge)
    print('The sum of my kids ages are:',sum_of_their_ages)

myMainFunction()

#return: an = to the terminal to output your result


