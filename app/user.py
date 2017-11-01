import sys

class User(object):  
    def __init__(self):
        self.food_recipe = {}
       
    def create_food_recipe(self, name,instructions):
        """
        this method allows user to create a food recipe and it's instructions 
        """
        

        if name not in self.food_recipe.keys():
            self.food_recipe[name] = [instructions]
        else:
            return "Food recipe already exists"
        return self.food_recipe
    
    def view(self,name):
        """
        enables a user to view a food recipe
        """
        if name in self.food_recipe.keys():
            return self.food_recipe[name]
        else:
            return "Not Available"
    def update(self, name, new_name):
        """
        changing the recipe name
        """
        if name in self.food_recipe.keys():
            self.food_recipe[new_name] = self.food_recipe[name]
            del self.food_recipe[name]
        else:
            return "Recipe not located"
        return self.food_recipe
    
    def update_inst(self,name,inst):
        if name in self.food_recipe.keys():
            self.food_recipe[name].append(inst)
        else:
            return "incorrect recipe name or its not available"
        return self.food_recipe[name]
    def delete(self,name):
        if name in self.food_recipe.keys():
            del self.food_recipe[name]
        else:
            return "Invalid Request"
        return self.food_recipe
    

