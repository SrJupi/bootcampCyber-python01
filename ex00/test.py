from book import Book
from recipe import Recipe

if __name__ == '__main__':
    try:
        recipe = Recipe("cooki", 0, 10, ["dough", "sugar", "love"], "dessert", "deliciousness incarnate")
    except TypeError as msg:
        print(msg)
    try:
        recipe = Recipe("cooki", 1.5, 10, ["dough", "sugar", "love"], "dessert", "deliciousness incarnate")
    except TypeError as msg:
        print(msg)
    try:
        recipe = Recipe("cooki", 1, 10, [], "dessert", "deliciousness incarnate")
    except TypeError as msg:
        print(msg)
    try:
        recipe = Recipe("cooki", 1, 10, ["dough", "sugar", "love"], "dessert", "deliciousness incarnate")
    except TypeError as msg:
        print(msg)
    else:
        print('Recipe was created:')
        print(recipe)
    b = Book("My seductive recipes")
    print('Creation of book:', b.creation_date)
    print('Last update of book:', b.last_update)
    crumble = Recipe("Crumble" , 1, 25, ["apples", "flour", "sugar"], "dessert", "delicious")
    b.add_recipe(crumble)
    print('Last update of book:', b.last_update)
    b.get_recipe_by_name("Crumble")
    b.get_recipe_by_name("Liver Icecream")
    print(b.get_recipes_by_types("dessert")[0])
    print(b.get_recipes_by_types("asdasd"))
    b.add_recipe(recipe)
    b.add_recipe(crumble)
    new_cooki = Recipe("cooki", 2, 10, ["dough", "sugar", "HATE"], "dessert", "deliciousness incarnate")
    b.add_recipe(new_cooki)



