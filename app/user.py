import sys

class User(object):  
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.food_recipe = {}
        self.categories = {}

    def create_categories(self,category_name):
        if category_name not in self.categories.keys():
            self.categories[category_name] = []
        else: 
            return "categories already exists"

    def view_category(self,name):
        if name in self.categories.keys():
            return self.categories[name]
        else:
            return "The category not found"

    def update_cat(self,old_name, new_name):
        if old_name in self.categories.keys():
            new_name = old_name
        else:
            return "old category not found"

    def delete_category(self,name):
        if name in self.categories.keys():
            del self.categories[name]
        else: 
            return "invalid Category"

       
    def create_food_recipe(self,category_name, name, instructions=""" """ ):
        """
        this method allows user to create a food recipe and it's instructions 
        """
        if category_name in self.categories.keys():
            self.categories[category_name].append(name)
            if name not in self.food_recipe.keys():
                instructions = instructions.split("\r\n") 
                self.food_recipe[name] = instructions 
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
    

