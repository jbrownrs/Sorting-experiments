import unittest
import bubbleSort

class TestBubbleSort(unittest.TestCase):

    def test_basicSort(self):
        unsortedList = [3,2,1]
        expectedList = [1,2,3]
        self.assertEqual(bubbleSort.bubbleSort(unsortedList), expectedList)

    def test_alreadySorted(self):
        sortedList = [1,2,3]
        expectedList = [1,2,3]
        self.assertEqual(bubbleSort.bubbleSort(sortedList), expectedList)

    def test_emptyList(self):
        emptyList = []
        expectedList = []
        self.assertEqual(bubbleSort.bubbleSort(emptyList), expectedList)

    def test_sortCharacters(self):
        unsortedList = ['b','a','c']
        expectedList = ['a','b','c']
        self.assertEqual(bubbleSort.bubbleSort(unsortedList), expectedList)        
                
        
if __name__ == '__main__':
    unittest.main()
