import json

def add_recipe_input():
    recipe_name = input("Enter the recipe name: ")
    if recipe_name:
        ingredients = input("Enter the ingredients: ")
        instructions = input("Enter the instructions(add \ then n after every step): ")
        rating = input("Enter the rating (1-5): ")

        return add_recipe(recipe_name, ingredients, instructions, rating)
    else:
        return "Recipe name cannot be empty."
    
def add_recipe(recipe_name, ingredients, instructions, rating):
    if float(rating) and float(rating) >= 1 and float(rating) <= 5:
        recipe = {
            "name": recipe_name,
            "ingredients": ingredients,
            "instructions": instructions,
            "rating": float(rating)
        }
        recipes.append(recipe)
        add_to_database(recipe)
        Final = "Recipe " + recipe_name + " added!"
        return str(Final)
    else:
        return "Invalid rating value. Please enter a number between 1 and 5."

def view_recipes():
    with open("Recipes_data.json", "r") as data_file:
        data = json.load(data_file)
    return data
def view_all_recipes():
    recipeNames = []
    for i in recipes:
        recipeNames.append(i["name"])
    return recipeNames

def edit_recipe_input():
    recipe_name = input("Enter the recipe name to edit: ")
    recipe = get_recipe_details(recipe_name)

    if recipe:
        ingredients = recipe['ingredients']
        instructions = recipe['instructions']
        rating = recipe['rating']
        while True:
            print("1. Ingredients")
            print("2. Instructions")
            print("3. Rating(1-5)")
            print("4. Done")
            decision = input(f"Choose which category do you want to edit:")            
            if decision == "1":
                print(f"Current ingredients: {recipe['ingredients']}")
                ingredients = input(f"Enter the new ingredients: ")
            
            elif decision == "2":
                print(f"Current instructions: {recipe['instructions']}")
                instructions = input(f"Enter the new instructions: ")
            
            elif decision == "3":
                print(f"Current rating: {recipe['rating']}")
                rating = input(f"Enter the new rating (1-5): ")
            
            elif decision == "4":
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        return edit_recipe(recipe,ingredients, instructions, rating)
    else:
        return "Recipe not found."
    
def edit_recipe(recipe, ingredients, instructions, rating):
        if float(rating) and 1 <= float(rating) <= 5:
            recipe["ingredients"] = ingredients
            recipe["instructions"] = instructions
            recipe["rating"] = float(rating)
            update_recipe_list(recipe)
            return "Recipe " + recipe['name'] + " modified!"
        else:
            return "Invalid rating value. Please enter a number between 1 and 5."


def update_recipe_list(recipe):
    with open("Recipes_data.json", "r") as data_file:
        data = json.load(data_file)
        for a in data:
            if a['name'] == recipe['name']:
                a["ingredients"] = recipe["ingredients"]
                a["instructions"] = recipe["instructions"]
                a["rating"] = recipe["rating"]
    with open("Recipes_data.json", 'w') as file: 
        json.dump(data, file, indent=4)

recipes = view_recipes()

def delete_recipe_input():
    recipe_name = input("Enter the recipe name to delete: ")
    recipe = get_recipe_details(recipe_name)

    if recipe:
        confirm = input(f"Do you want to delete the recipe '{recipe_name}'? (yes/no): ")
        delete_recipe(recipe_name, confirm)
    else:
        return "Recipe not found."

def get_recipe_details(recipe_name):
    for x in recipes:
        if x['name'].lower() == recipe_name.lower():
            return x

def delete_recipe(recipe_name, confirm):
    if confirm.lower() == 'yes':
        recipes.remove(get_recipe_details(recipe_name))
        update_recipe_list()
        return "Recipe " + recipe_name + " deleted!"
    else:
        return "Delete cancelled"

def export_recipes_input():
    file_path = input("Enter the file path to export recipes (e.g., recipes.json): ")
    return export_recipes(file_path)

def export_recipes(file_path):
    if file_path:
        with open(file_path, 'w') as file:
            json.dump(recipes, file)
        return "Recipes exported to JSON file."
    
def import_recipes_input():
    file_path = input("Enter the file path to import recipes from (e.g., recipes.json): ")
    return import_recipes(file_path)

def import_recipes(file_path):
    if file_path:
        with open(file_path, 'r') as file:
            loaded_recipes = json.load(file)
            recipes.extend(loaded_recipes)
            update_recipe_list()
        return "Recipes imported from JSON file."
    
def filter_recipes_input():
    rating_filter = input("Enter the rating to filter (leave empty for all): ")
    return filter_recipes(rating_filter)

def filter_recipes(rating_filter):
    filtered_recipes = []
    for recipe in recipes:
        if (not rating_filter or (float(rating_filter) and 1 <= float(rating_filter) <= 5 and float(rating_filter) == recipe['rating'])):
            filtered_recipes.append(recipe)
    return filtered_recipes

def add_to_database(recipe):
    with open("Recipes_data.json", "r") as data_file:
        data = json.load(data_file)
    if not data:
        data = []
    data.append(recipe)
    with open("Recipes_data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)

def find_recipe_by_name():
    name = input("Enter recipe name: ")
    for recipe in recipes:
        if recipe["name"].lower() == name.lower():
            print(recipe["name"])
            print("ingredients")
            print(recipe["ingredients"])
            print("instructions")
            print(recipe["instructions"])
            print("rating:", recipe["rating"],"out of 5")
            return 
    print("Recipe not found")
    
def main():
    while True:
        print("\nRecipe Management System")
        print("1. Add Recipe")
        print("2. View recipe")
        print("3. Edit Recipe")
        print("4. Delete Recipe")
        print("5. Export Recipes")
        print("6. Import Recipes")
        print("7. Filter Recipes")
        print("8. View Recipe Details")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            print(add_recipe_input())
          
        elif choice == "2":
            print(view_all_recipes())
           
        elif choice == "3":
            print(edit_recipe_input())
           
        elif choice == "4":
            print(delete_recipe_input())
           
        elif choice == "5":
            print(export_recipes_input())
           
        elif choice == "6":
            print(import_recipes_input())
        elif choice == "7":
            filtered_recipes = filter_recipes_input()
            for recipe in filtered_recipes:
                print(recipe["name"])
        elif choice == "8":
            find_recipe_by_name()
        elif choice == "9":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()

