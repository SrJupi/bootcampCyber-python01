from book import Book
from recipe import Recipe
from time import sleep
import os

def clear():
    os.system('clear')

def history():
    '''Amazing function to show the functionality'''
    clear()
    print('''Welcome to my test.py.
This script will test my Book and Recipe classes that are in the book.py and recipe.py files respectively.
First lets create a book to keep all the recipes.
''')
    ans = input("How do you like to call it? It's name should be a string.\n>> ")
    book = Book(ans)
    clear()
    input("Nice!\nTo test if it was created lets print it using print(book)! (press Enter to continue)")
    print(book)
    input("Ok! It seems that everything is ok with the book! Lets try to use it... (press Enter to continue)")
    clear()
    input('''The book have three functions:
    -> get_recipes_by_name: try to find a recipe by it's name on the book;
    -> get_recipes_by_types: return a list with the name of all recipes of the searched type;
    -> add_recipe: add a recipe to the book.

As you can imagine the book is a little bit useless without any recipe. Let's try to add some randon class as a Recipe to see how the book handle it. I will create the following "Recipe":

    my_recipe = 'I am not a Recipe!'

''')


    my_recipe = 'I am not a Recipe!'
    book.add_recipe(my_recipe)

    input('''\nAs it is possible to see the book check it is not a Recipe class object and does no insert it to the book dictionary of recipes.
So next we will see the Recipe class and lets create some recipes to use inside the Book class.
(press Enter to continue)''')
    clear()
    input('''The Recipe class will keep all information needed for a recipe. So it has to have:
    -> name (string)
    -> cooking level/difficulty (a integer between 0 and 5)
    -> cooking time (a positive integer)
    -> a list of ingredients (a list of strings)
    -> recipe type (a string that can be "Starter", "Lunch" or "Dessert")
    -> (optional) description (string)
On its __init__ function there are checks to validate all this parameters and if there are any issue it will print a informative message and raise an Excepction.
First lets try to create a not valid Recipe. I will use the following command:
    
    my_recipe = Recipe(123, 0, 10, ['ing1', 'ing2'], 'Starter')

Is possible to see that name is not a string so it should raise an Error and print what is failing. (press Enter to continue)
''')
    try:
        my_recipe = Recipe(123, 0, 10, ['ing1', 'ing2'], 'Starter')
    except:
        input("\nOH NO! You are inside the except block... Some shit happened. But we can see what made the Recipe constructor fails...")
    clear()
    input('''Now let's create a valid Recipe... Uhmm... let's make some Caipirinha:
    
    my_recipe = Recipe('Caipirinha', 0, 5, ['Lemon', 'Ice', 'Sugar', 'Cachaça'], 'Starter', 'The only known brazilian drink')

So with this code should work and create a instance of a Recipe... Finally...''')
    try:
        my_recipe = Recipe('Caipirinha', 0, 5, ['Lemon', 'Ice', 'Sugar', 'Cachaça'], 'Starter', 'The only known brazilian drink')
    except:
        input("\nOH NO! You are inside the except block... Some shit happened. But we can see what made the Recipe constructor fails...")
    input('''\nWe are outside the try/except block... so the Recipe for a Capirinha should have been created... lets print it:

    print(my_recipe)
''')
    print(my_recipe)
    input("NICE!\nNow let's add it to the book...")
    clear()
    print("So back to the book... Let's print it:")
    print(book)
    input('''Now let's add the Caipirinha to the book and print it again to see if there was updated

    book.add_recipe(my_recipe)
''')
    book.add_recipe(my_recipe)
    print(f"\n{book}")
    input('''Oh Yeah! The book was UPDATED!
Let's call the get_recipe_by_name to see if Caiprinha is saved on book.

    get_recipe = book.get_recipe_by_name("Caiprinha")

If the recipe exist on book it will print it and return its instance.
''')

    get_recipe = book.get_recipe_by_name("Caipirinha")

    input('''Nice. Now you got a reference for the Caiprinha inside the book and could change it as you please (and probably broke all my program... so I will not allow it).
Now let's try to get a recipe that does not exist... like Soup:

    get_recipe = book.get_recipe_by_name("Soup")
''')

    get_recipe = book.get_recipe_by_name("Soup")

    input('''\nAs you can see the book could not find any soup in its database.

Now I will quickly create some more recipes and add them to the book so we can try the get_recipe_by_types function...''')

    clear()
    print("Thinking in really hard recipes...")
    sleep(1.5)
    print("Ok... Adding new recipes...")
    book.add_recipe(Recipe('Water', 0, 1, ['Water'], 'Starter', 'It is water... what else do you need?'))
    book.add_recipe(Recipe('Pasta', 0, 3, ['Ramen Nissin', 'Flavor'], 'Lunch', 'Wow! Ready in 3min!'))
    book.add_recipe(Recipe('Salad', 0, 5, ['Tomato', 'Lettuce', 'Carrots'], 'Lunch', 'Lunch? Really? Are we on a diet?'))
    book.add_recipe(Recipe('Chocolate', 0, 1, ['Chocolate'], 'Dessert', 'Just open it and eat it... Not really difficult.'))
    sleep(0.3)

    input('''I have added another 4 recipes: 1 starter, 2 lunch and 1 dessert.
Let's use the get_recipes_by_types to see their's names...

    print("Starter:", book.get_recipes_by_types("Starter"))
    print("Lunch:", book.get_recipes_by_types("Lunch"))
    print("Dessert:", book.get_recipes_by_types("Dessert"))
''')
    print("Starter:", book.get_recipes_by_types("Starter"))
    print("Lunch:", book.get_recipes_by_types("Lunch"))
    print("Dessert:", book.get_recipes_by_types("Dessert"))

    input('''Now let's use the get_recipes_by_name to print each one...''')
    book.get_recipe_by_name('water')
    input("Next?")
    clear()
    book.get_recipe_by_name('caipirinha')
    input("Next?")
    clear()
    book.get_recipe_by_name('salad')
    input("Next?")
    clear()
    book.get_recipe_by_name('pasta')
    input("Next?")
    clear()
    book.get_recipe_by_name('chocolate')
    input("Done! You have seen all the recipes and all functionality that is on this book! Feel free to ask me anything and create any test you want! Cheers!")
    clear()
    pass

if __name__ == "__main__":
    history()
