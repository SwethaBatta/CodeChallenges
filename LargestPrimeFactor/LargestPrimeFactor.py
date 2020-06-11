import math
import sys


def validNumber(num : int):
    return num > 0 and num < sys.maxsize and num > -sys.maxsize and isinstance(num, int)
    
def largestPrimeFactor(num):
    maxPrimeFactor = -1
    inputNum = num
    
    if not validNumber(num):
        return (f"Largest prime factor of {inputNum} : Not a valid value. Try again!")
    
    #If number is even, 2 is the maximum prime factor
    while num%2 == 0:
        maxPrimeFactor = 2
        num /= 2
        
    #If not even, this odd loop executes to find the maximum prime factor
    for i in range(3, int(math.sqrt(num))+1, 2):
        while num % i == 0:
            maxPrimeFactor = i
            num /= i
    
    #If number not equal to 1
    if num != 1:
        maxPrimeFactor = num
    
    return (f'Largest prime factor of {inputNum} :  {int(maxPrimeFactor)}')

