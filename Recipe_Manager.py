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
            # print(add_recipe_input())
            pass
        elif choice == "2":
            # print(view_recipes())
            pass
        elif choice == "3":
            # print(edit_recipe_input())
            pass
        elif choice == "4":
            # print(delete_recipe_input())
            pass
        elif choice == "5":
            # print(export_recipes_input())
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
