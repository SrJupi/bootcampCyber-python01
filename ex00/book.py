from datetime import datetime
from recipe import Recipe

class Book(object):
    '''Book Class: keeper of the recipes!'''

    def __init__(self, name="The best recipe book"):
        if not isinstance(name, str) or name == "":
            self.name = "I have no name..."
        else:
            self.name = name
        self.last_update = datetime.now()
        self.creation_date = self.last_update
        self.recipe_list = {"Starter": [],
                "Lunch": [],
                "Dessert": []}

    def __str__(self):
        txt = f'''I am a Recipe Book!
My name is "{self.name.upper()}".
I was created on {self.creation_date}.
My last update was on {self.last_update}
'''
        return txt
    
    def get_recipe_by_name(self, name):
        """Prints a recipe with the name and returns the instance"""
        recipe_ret = None
        name = name.lower().capitalize()
        for r_type in ["Starter", "Lunch", "Dessert"]:
            if name in [recipe.name for recipe in self.get_recipes_by_types(r_type)]:
                for recipe in self.recipe_list[r_type]:
                    if recipe.name == name:
                        recipe_ret = recipe
                        print(f'Hey! I found the recipe for "{name}"!\nHope you enjoy it:')
                        print(recipe_ret)
                        return recipe_ret
        if recipe_ret == None:
            print(f'Recipe "{name}" not found in {self.name}.')
        return recipe_ret

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        recipe_type = recipe_type.lower().capitalize()
        if recipe_type in ["Starter", "Lunch", "Dessert"]:
            return self.recipe_list[recipe_type]
        return []

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if isinstance(recipe, Recipe):
            for rtype in ["Starter", "Lunch", "Dessert"]:
                if recipe.name in self.get_recipes_by_types(rtype):
                    print(f"Recipe {recipe.name} already in {self.name}")
                    return
            self.recipe_list[recipe.recipe_type.lower().capitalize()].append(recipe)
            self.last_update = datetime.now()
            print(f'Recipe "{recipe.name}" inserted in book!')
        else:
            print(f'Recipe "{recipe}" not inserted in book. It is not a real recipe!')
