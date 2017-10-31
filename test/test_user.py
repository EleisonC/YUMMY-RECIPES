import unittest 

from app.user import User

class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.chris = User()

    def test_create_food_recipe(self):
        self.chris.create_food_recipe("fried eggs","eggs, oil, fire")
        self.assertEqual(self.chris.food_recipe,{'fried eggs': ['eggs, oil, fire']})

    def test_view(self):
        self.chris.food_recipe = {'fried eggs': ['eggs, oil, fire']}
        self.assertEqual(self.chris.view("fried eggs"),['eggs, oil, fire'])

    def test_update(self):
        self.chris.food_recipe = {'zfired eggs': ['eggs, oil, fire']}
        self.assertEqual(self.chris.update("zfired eggs","fried eggs"),{'fried eggs': ['eggs, oil, fire']})

    def test_update_inst(self):
        self.chris.food_recipe = {'fried eggs': ['eggs, oil, fire']}
        self.assertEqual(self.chris.update_inst("fried eggs","boil in hot water"),['eggs, oil, fire',"boil in hot water"])
    
    def test_delete(self):
        self.chris.food_recipe = {'fried eggs': ['eggs, oil, fire']}
        self.assertEqual(self.chris.delete("fried eggs"), {})