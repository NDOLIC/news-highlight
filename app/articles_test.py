import unittest
from models import sources
articles = articles.Articles

class articlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_articles = articles('techcrunch','techcrunch','Romain Dillet','following BCH fork','The Bitcoin Cash chain split into two different chains back in November','http://techcrunch.com/2019/02/15/coinbase-users-can-now-withdraw-bitcoin-sv-following-bch-fork','https://techcrunch.com/wp-content/uploads/2017/08/bitcoin-split-2017a.jpg?w=711','2019-02-15T14:53:40Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles,articles))

    def test_init(self):
       '''
       set up a method that tests if the source object is correctly initiated
       '''
       self.assertEqual(self.new_articles.id,"techcrunch")
       self.assertEqual(self.new_articles.name,"techcrunch")
       self.assertEqual(self.new_articles.author,"Romain Dillet")
       self.assertEqual(self.new_articles.title,"following BCH fork")
       self.assertEqual(self.new_articles.urlToImage,"https://techcrunch.com/wp-content/uploads/2017/08/bitcoin-split-2017a.jpg?w=711")
       self.assertEqual(self.new_articles.url,"http://techcrunch.com/2019/02/15/coinbase-users-can-now-withdraw-bitcoin-sv-following-bch-fork")
       self.assertEqual(self.new_articles.publishedAt,"2019-02-15T14:53:40Z")

       
if __name__ == '__main__':
    unittest.main()