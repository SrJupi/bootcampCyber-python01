import sys

sys.tracebacklimit = 0


class Recipe(object):
    """Recipe Class: keep good food inside!"""

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
            msgs = self.print_errors(check)
            raise TypeError("ERROR: " + ", ".join(msgs))

    def __str__(self):
        txt = f'''{'~' * 50}
{self.name.upper()}
    -> Description:
        {self.description}
    -> Ingredients:
        {', '.join(self.ingredients)}
    -> Cooking time: {self.cooking_time} min
    -> Cooking level: {self.cooking_lvl}
    -> Recipe type: {self.recipe_type}
{'~' * 50}'''
        return txt

    def check_inputs(self):
        valid_types = ["Starter", "Lunch", "Dessert"]
        check = 0
        if not isinstance(self.name, str) or self.name == "":
            check |= 1
        else:
            self.name = self.name.lower().capitalize()
        if not isinstance(self.cooking_lvl, int) or self.cooking_lvl < 1 or self.cooking_lvl > 5:
            check |= 2
        if not isinstance(self.cooking_time, int) or self.cooking_time < 1:
            check |= 4
        if not isinstance(self.ingredients, list) or len(self.ingredients) == 0:
            check |= 8
        else:
            for ing in self.ingredients:
                if not isinstance(ing, str):
                    check |= 16
                    break
        if self.description is None:
            self.description = ""
        if not isinstance(self.description, str):
            check |= 32
        if not isinstance(self.recipe_type, str) or self.recipe_type.lower().capitalize() not in valid_types:
            check |= 64
        return check

    def print_errors(self, check):
        msgs = []
        if check & 1:
            msgs.append("Name must be a string")
        if check & 2:
            msgs.append("Cooking level must be an integer between 1 and 5")
        if check & 4:
            msgs.append("Cooking time must be an integer and bigger than zero")
        if check & 8:
            msgs.append("Ingredients must be a list of strings")
        if check & 16:
            msgs.append("Ingredients list must contain only strings")
        if check & 32:
            msgs.append("Description must be a string or empty")
        if check & 64:
            msgs.append("Recipe type must be Starter, Lunch or Dessert")
        return msgs
