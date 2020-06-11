import unittest
from RollTwoDice import RollTwoDice

class TestRollTwoDice(unittest.TestCase):
      def setUp(self):
          self.rtd = RollTwoDice()

class TestInit(TestRollTwoDice):
      def test_initial_firstDice(self):
          self.assertEqual(self.rtd.firstDice, {})

      def test_initial_secondDice(self):
          self.assertEqual(self.rtd.secondDice, {})

      def test_initial_total(self):
          self.assertEqual(self.rtd.total, 0)

      def test_initial_specialCase(self):
          self.assertEqual(self.rtd.specialCase, '')
          
      def test_initial_dice(self):
          self.assertEqual(self.rtd.dice, [{"val": 1, "img": '\u2680'}, {"val": 2, "img": '\u2681'}, {"val": 3, "img": '\u2682'}, {"val":4, "img": '\u2683'}, {"val":5, "img": '\u2684'}, {"val":6, "img": '\u2685'}])

class TestCheckRollDiceCases(TestRollTwoDice):
      def test_compute_total(self):
          self.rtd.diceValues()
          self.rtd.computeTotal()
          self.assertEqual(int(self.rtd.firstDice['val']) + int(self.rtd.secondDice['val']), self.rtd.total)

      def test_case_SnakeEyes(self):
          self.rtd.firstDice['val'] = 1
          self.rtd.secondDice['val'] = 1
          self.rtd.caseSnakeEyes()
          self.assertEqual(self.rtd.specialCase, 'Snake Eyes')
    
      def test_case_Lucky7(self):
          self.rtd.total = 7
          self.rtd.caseLucky7()
          self.assertEqual(self.rtd.specialCase, 'Lucky 7')

class TestRandomChoice(TestRollTwoDice):    
      def test_random_firstDice(self):
          self.rtd.diceValues()
          self.assertIn(self.rtd.firstDice['val'], [1,2,3,4,5,6])

      def test_random_secondDice(self):
          self.rtd.diceValues()
          self.assertIn(self.rtd.secondDice['val'], [1,2,3,4,5,6])
          
class TestDiceImage(TestRollTwoDice):
      def test_random_firstDice(self):
          self.rtd.diceValues()
          self.assertEqual(self.rtd.firstDice['img'], next((sub['img'] for sub in self.rtd.dice if sub['val'] == self.rtd.firstDice['val']), None))

      def test_random_secondDice(self):
          self.rtd.diceValues()
          self.assertEqual(self.rtd.secondDice['img'], next((sub['img'] for sub in self.rtd.dice if sub['val'] == self.rtd.secondDice['val']), None))
              
if __name__ == '__main__':
    unittest.main()   
