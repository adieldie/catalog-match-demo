import unittest
from matcher import match_product
class Tests(unittest.TestCase):
    def setUp(self):
        self.catalog = {"caderno": [{"id":"sample-a", "price":12.0, "category":"escola"}, {"id":"sample-b", "price":12.0, "category":"escritorio"}]}
    def test_exact(self):
        self.assertEqual(match_product(" CADERNO ",12,self.catalog)[0],"sample-a")
    def test_category(self):
        self.assertEqual(match_product("caderno",12,self.catalog,"escritorio")[0],"sample-b")
    def test_fuzzy(self):
        self.assertEqual(match_product("cadernos",12,self.catalog)[0],"sample-a")
    def test_price_rejection(self):
        self.assertEqual(match_product("caderno",20,self.catalog),(None,None))
    def test_specific_alias(self):
        self.assertEqual(match_product("item",12,self.catalog,aliases={"item|12.00":"caderno"})[0],"sample-a")
    def test_empty(self):
        self.assertEqual(match_product("x",1,{}),(None,None))
if __name__ == "__main__": unittest.main()
