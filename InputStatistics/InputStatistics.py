# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11

@author: SwethaBatta
"""
import sys

class InputStats(object):
    def __init__(self):
        self.numbersList = []
    
    def isValidList(self, numbersList):
        isValid = True
        error = []
        self.numbersList = numbersList
        
        if len(self.numbersList) == 0:
            return [False, 'No input is given!']
        
        for val in self.numbersList:
            try:
                num = int(val)
                if num > sys.maxsize or num < -sys.maxsize:
                    isValid = False
                    error.append(f'Input "{val}" is out of range') 
            
            except ValueError:
                isValid = False
                try:
                    error.append(f'Input "{val}" is of datatype {eval(val).__class__.__name__}')
                
                except NameError:
                    error.append(f'Input "{val}" is of datatype string') 
                    
                except SyntaxError:
                    error.append(f'Input "{val}" is an invalid character') 

                
        return [isValid, error]

    def inputStatistics(self, numbersStringList):
        print("\n")
        print("All entered numbers ", numbersStringList)

        self.numbersList = [int(numeric_string) for numeric_string in numbersStringList]

        # Calculating the sum of all user entered numbers
        numbersListSum = 0
        for num in self.numbersList:
            numbersListSum += num
        print("Sum of all entered numbers = ", numbersListSum)

        # Calculating the average of all user entered numbers
        average = numbersListSum / len(self.numbersList)
            
        print("Average of all entered numbers = ", round(average, 2))

        # Sorting the list to retrieve highest and lowest values
        self.numbersList.sort()
        print("Highest = ", self.numbersList[-1])
        print("Lowest = ", self.numbersList[0])


if __name__ == '__main__':
    inpStats = InputStats() 
    numbersStringList = input("Enter numbers separated by space: ").split()   

    if inpStats.isValidList(numbersStringList)[0]:
        inpStats.inputStatistics(numbersStringList)
    else:
        print(f"The given input contains the below errors:  \n{inpStats.isValidList(numbersStringList)[1]}\n\nPlease enter only integer values")
    
    
    '''
    try:
        numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
        inpStats.inputStatistics(numbers)
    except ValueError:
         print(f"The list contains the below invalid inputs with datatypes")
    '''