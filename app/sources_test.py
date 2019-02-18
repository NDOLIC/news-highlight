import unittest
from models import sources
sources = sources.sources

class MovieTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the sources class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_sources = sources('metro','Metro','News, Sport, Showbiz','http://metro.co.uk','general','en')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_sources,sources))

    def test_init(self):
       '''
       set up a method that tests if the source object is correctly initiated
       '''
       self.assertEqual(self.new_sources.id,"metro")
       self.assertEqual(self.new_sources.name,"Metro")
       self.assertEqual(self.new_sources.description,"News, Sport, Showbiz")
       self.assertEqual(self.new_sources.category,"general")
       self.assertEqual(self.new_sources.language,"en")
       self.assertEqual(self.new_sources.url,"http://www.independent.co.uk")

if __name__ == '__main__':
    unittest.main()