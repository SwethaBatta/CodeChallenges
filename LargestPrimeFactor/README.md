## Largest Prime factor

- Calculating the prime factors of a given number by dividing the given number recursively with its smallest prime factor until it becomes 1.
- If the number is even, we try to check and see if 2 is its maximum prime factor through the first loop. If yes, the execution ends here.
- If the number is odd, we loop through the odd integers to find the factors and keep updating the value 'maxPrime'.
- Since every composite number has atleast one prime factor less than or equal to its square root, we use this limiting value in range of odd number iteration. The time complexity would be O(sqrt(n)) due to this.
- Since no extra space is used and constant space to store maxPrime value is used, space complexity is constant O(1)


**Optimization**
- Checking for validitity of the number at the beginning of execution helps in avoiding unnecessary computations
- isValidNumber method only accepts positive integers which are within range limits
