class Recipe(object):
    '''Recipe Class: keep good food inside!'''

    def __init__(self,
            name, lvl,
            time, ing,
            rtype, desc=None):
        self.name = name
        self.cooking_lvl = lvl
        self.cooking_time = time
        self.ingredients = ing
        self.description = desc
        self.recipe_type = rtype
        check = self.check_inputs()
        if check > 0:
            self.print_errors(check)
            raise TypeError("Check your parameters!")

    def __str__(self):
        txt = f'''{'~'*50}
{self.name.upper()}
    -> Description:
        {self.description}
    -> Ingredients:
        {', '.join(self.ingredients)}
    -> Cooking time: {self.cooking_time} min
    -> Cooking level: {self.cooking_lvl} min
    -> Recipe type: {self.recipe_type}
{'~'*50}'''
        return txt

    def check_inputs(self):
        valid_types = ["Starter", "Lunch", "Dessert"]
        check = 0
        if not isinstance(self.name, str) or self.name == "":
            check |= 1
        else:
            self.name = self.name.lower().capitalize()
        if not isinstance(self.cooking_lvl, int) or self.cooking_lvl < 0 or self.cooking_lvl > 5: 
            check |= 2
        if not isinstance(self.cooking_time, int) or self.cooking_time < 1:
            check |= 4
        if not isinstance(self.ingredients, list):
            check |= 8
        else:
            for ing in self.ingredients:
                if not isinstance(ing, str):
                    check |= 16
                    break
        if self.description == None:
            self.description = ""
        if not isinstance(self.description, str):
            check |= 32
        if not isinstance(self.recipe_type, str) or self.recipe_type not in valid_types:
            check |= 64
        return check

    def print_errors(self, check):
        if check >= 64:
            print("ERROR: Recipe type must be Starter, Lunch or Dessert")
            check %= 64
        if check >= 32:
            print("ERROR: Description must be a string or empty")
            check %= 32
        if check >= 16 :
            print("ERROR: Ingredients list must contain only strings")
            check %= 16
        if check >= 8:
            print("ERROR: Ingredients must be a list of strings")
            check %= 8
        if check >= 4:
            print("ERROR: Cooking time must be an integer and bigger than zero")
            check %= 4
        if check >= 2:
            print("ERROR: Cooking level must be an integer between 0 and 5")
            check %= 2
        if check >= 1:
            print("ERROR: Name must be a string")
            check %= 1
