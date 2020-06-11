## Input Statistics

To accept a variable range of numeric inputs and computes highest, lowest and average number

- Accepting user input with input() function
- By default, python stores user input as 'String'. 
- The conversion to int can be done using int(input('Enter ..')) and exception handling can be used at this stage to raise exception for non-integer input, but this doesn't specify which input value is unacceptable in the given list.
- To keep the error messages more descriptive to the user about incorrect inputs, exception handling is done after collecting the input values in a list.
- **isValidList** method checks to see if the user's input is of the acceptable datatype (integer in this case) and within range limits.
- The exceptions handling for the following cases is implemented  
  - No input
  - Out of range
  - Invalid character (special characters)
  - Incorrect datatype
  
- The list **error[]** collects all the invalid inputs along with the error message.
   - If the value cannot be cast to 'int', it enters the except 'ValueError' block. Here, I used 'eval' to parse the string to get the     datatype by using 
      eval(val).__ class__.__ name__  [type(eval(val)) returns <class: 'float'>, hence used .__ class__.__ name__ to retrive 'float' ]
      Example: - [['3.5', 'float']]
   -  'eval' throws a 'NameError' exception when string is given as input. To handle this case, I used another try-except block to indicate a string datatype input   
- Inside **inputStatistics** method, I used a list comprehension to convert the given input string list to integer list.
- I rounded the average to 2 decimal places and sorted the list to obtain highest and lowest values.


- If descriptive error messages are not needed, the commented block of code in main can be used where the type casting is done at the time of accepting user input. List comprehension is used to create this integer list and any non-integer value will throw a generic exception.


Optimization
- All the exception handling is implemented in one method (isValidList), this is helpful in determining if the rest of the code needs to be accessed. 
Hence for a case when no input is given, there need wouldn't be a need to handle ZeroDivisionError while computing Average as the exception is raised in the first step.
- Used list comprehension to convert string list to integer list which adds computational efficiency interms of coding space and time.



