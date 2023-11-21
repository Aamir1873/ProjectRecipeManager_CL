import json
def add_recipe(recipe_name, ingredients, instructions, rating):
    if int(rating) and 1 <= int(rating) <= 5:
        recipe = {
            "name": recipe_name,
            "ingredients": ingredients,
            "instructions": instructions,
            "rating": int(rating)
        }
        recipes.append(recipe)
        #update_recipe_list()
        #add_to_database(recipe)
        Final = "Recipe " + recipe_name + " added!"
        return str(Final)
    else:
        return "Invalid rating value. Please enter a number between 1 and 5."
    
    def import_recipes_input():
        file_path = input(
        "Enter the file path to import recipes from (e.g., recipes.json): ")
    return import_recipes(file_path)


def import_recipes(file_path):
    if file_path:
        with open(file_path, 'r') as file:
            loaded_recipes = json.load(file)
            recipes.extend(loaded_recipes)
            update_recipe_list()
        return "Recipes imported from JSON file."
    
    
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
            # print(edit_recipe_input())
            pass
        elif choice == "4":
            # print(delete_recipe_input())
            pass
        elif choice == "5":
            print(export_recipes_input())
            pass
        elif choice == "6":
             print(import_recipes_input())
            pass
        elif choice == "7":
            pass
            # filtered_recipes = filter_recipes_input()
            # for recipe in filtered_recipes:
            #     print(recipe["name"])
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
    print("hi")
