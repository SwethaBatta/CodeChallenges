## RollTwoDice

- User provides input command to roll the dice through GUI.
- Initialized a list for dice values which has dictionaries with the key-value pairs - {dice value : image} 
  Note - unicode character string is used for image
- Used python random() module to make a random selection from the above initialized list of 6 values.
- Displays individual dice counts, total count and special case message (Snake Eyes, Lucky 7)
- Created unit tests for all the methods in unitTests_RollTwoDice.py
- To run unit tests, execute the below command from this cloned repository/RollTwoDice folder
  > python -m unittest -v unitTests_RollTwoDice.py 
  

**Optimization**
- Organized the code into modular methods based on the use-cases. This also supports unit test effort.
- Used dictionary comprehension for verifying dice images unit tests.
- GUI code structure can be further refactored for extendability and modularity.

