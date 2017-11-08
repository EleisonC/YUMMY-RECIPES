import unittest 

from app.user import User

class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.chris = User("user","123")

    def test_create_food_recipe(self):
        """ tests if a user can add a food recipe name and the instructions"""
        self.chris.create_categories("breakfast")
        self.chris.create_food_recipe('breakfast',"fried eggs","eggs, oil, fire")
        self.assertEqual(self.chris.food_recipe,{'fried eggs': ['eggs, oil, fire']})

    def test_view(self):
        """tests if a user can view the instructions for requested food recipe name"""
        self.chris.food_recipe = {'fried eggs': ['eggs, oil, fire']}
        self.assertEqual(self.chris.view("fried eggs"),['eggs, oil, fire'])

    def test_update(self):
        """tests if a user can rename a food recipe"""
        self.chris.food_recipe = {'zfired eggs': ['eggs, oil, fire']}
        self.assertEqual(self.chris.update("zfired eggs","fried eggs"),{'fried eggs': ['eggs, oil, fire']})

    def test_update_inst(self):
        """tests if a user can add intsructions"""
        self.chris.food_recipe = {'fried eggs': ['eggs, oil, fire']}
        self.assertEqual(self.chris.update_inst("fried eggs","boil in hot water"),['eggs, oil, fire',"boil in hot water"])
    
    def test_delete(self):
        """tests if a user can delete a food recipe"""
        self.chris.food_recipe = {'fried eggs': ['eggs, oil, fire']}
        self.assertEqual(self.chris.delete("fried eggs"), {})
