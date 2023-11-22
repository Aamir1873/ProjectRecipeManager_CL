import json

def add_recipe_input():
    recipe_name = input("Enter the recipe name: ")
    if recipe_name:
        ingredients = input("Enter the ingredients: ")
        instructions = input("Enter the instructions: ")
        rating = input("Enter the rating (1-5): ")

        add_recipe(recipe_name, ingredients, instructions, rating)
    else:
        return "Recipe name cannot be empty."
    
def add_recipe(recipe_name, ingredients, instructions, rating):
    if int(rating) and 1 <= int(rating) <= 5:
        recipe = {
            "name": recipe_name,
            "ingredients": ingredients,
            "instructions": instructions,
            "rating": int(rating)
        }
        recipes.append(recipe)
        update_recipe_list()
        add_to_database(recipe)
        Final = "Recipe " + recipe_name + " added!"
        return str(Final)
    else:
        return "Invalid rating value. Please enter a number between 1 and 5."

def view_recipes():
    with open("Recipes_data.json", "r") as data_file:
        data = json.load(data_file)
    return data

def edit_recipe_input():
    recipe_name = input("Enter the recipe name to edit: ")
    recipe = find_recipe_by_name(recipe_name)

    if recipe:
        ingredients = input(f"Enter the new ingredients ({recipe['ingredients']}): ")
        instructions = input(f"Enter the new instructions ({recipe['instructions']}): ")
        rating = input(f"Enter the new rating (1-5) ({recipe['rating']}): ")
        edit_recipe(recipe_name, ingredients, instructions, rating)
    else:
        return "Recipe not found."
    
def edit_recipe(recipe_name, ingredients, instructions, rating):
        recipe = find_recipe_by_name(recipe_name)
        if int(rating) and 1 <= int(rating) <= 5:
            recipe["ingredients"] = ingredients
            recipe["instructions"] = instructions

            recipe["rating"] = int(rating)
            update_recipe_list()
            return "Recipe " + recipe_name + " modified!"
        else:
            return "Invalid rating value. Please enter a number between 1 and 5."

recipes = view_recipes()

def delete_recipe_input():
    recipe_name = input("Enter the recipe name to delete: ")
    recipe = find_recipe_by_name(recipe_name)

    if recipe:
        confirm = input(f"Do you want to delete the recipe '{recipe_name}'? (yes/no): ")
        delete_recipe(recipe_name, confirm)
    else:
        return "Recipe not found."

def delete_recipe(recipe_name, confirm):
    if confirm.lower() == 'yes':
        recipes.remove(find_recipe_by_name(recipe_name))
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
    return filter_recipes(category_filter, rating_filter)

def filter_recipes(category_filter, rating_filter):
    filtered_recipes = []
    for recipe in recipes:
        if (not rating_filter or (int(rating_filter) and 1 <= int(rating_filter) <= 5 and int(rating_filter) == recipe["rating"])):
            filtered_recipes.append(recipe)

    return filtered_recipes

def update_recipe_list():
    for recipe in recipes:
        print(recipe["name"])

def add_to_database(recipe):
    with open("Recipes_data.json", "r") as data_file:
        data = json.load(data_file)
    if not data:
        data = []
    data.append(recipe)
    print(data)
    with open("Recipes_data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)

def find_recipe_by_name(name):
    print("THIS IS RUNNING")
    print(recipes)
    for recipe in recipes:
        print(recipe)
        print(name)
        if recipe["name"].lower() == name.lower():
            return recipe
    return None
    
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
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            print(add_recipe_input())
            pass
        elif choice == "2":
            print(view_recipes())
            pass
        elif choice == "3":
            print(edit_recipe_input())
            pass
        elif choice == "4":
            # print(delete_recipe_input())
            pass
        elif choice == "5":
            print(export_recipes_input())
            pass
        elif choice == "6":
            # print(import_recipes_input())
            pass
        elif choice == "7":
            pass
            filtered_recipes = filter_recipes_input()
            for recipe in filtered_recipes:
                print(recipe["name"])
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
    print("hi")
