import json

def view_recipes():
    with open("Recipes_data.json", "r") as data_file:
        data = json.load(data_file)
    return data

recipes = view_recipes()

def export_recipes_input():
    file_path = input("Enter the file path to export recipes (e.g., recipes.json): ")
    return export_recipes(file_path)

def export_recipes(file_path):
    if file_path:
        with open(file_path, 'w') as file:
            json.dump(recipes, file)
        return "Recipes exported to JSON file."

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
            # print(add_recipe_input())
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
            # print(import_recipes_input())
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
