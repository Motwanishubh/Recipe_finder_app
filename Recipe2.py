import tkinter as tk
from tkinter import ttk

class RecipeFinder:
    def __init__(self):
        self.recipes = [
            {"name": "Pancakes", "ingredients": ["flour", "milk", "egg", "sugar"], "type": "Breakfast"},
            {"name": "Caesar Salad", "ingredients": ["lettuce", "croutons", "parmesan", "chicken"], "type": "Lunch"},
            {"name": "Spaghetti Bolognese", "ingredients": ["spaghetti", "tomato", "beef", "garlic"], "type": "Dinner"},
            {"name": "Omelette", "ingredients": ["egg", "cheese", "bell pepper"], "type": "Breakfast"},
            {"name": "Grilled Cheese Sandwich", "ingredients": ["bread", "cheese", "butter"], "type": "Lunch"},
            {"name": "Fruit Salad", "ingredients": ["apple", "banana", "orange", "grapes"], "type": "Breakfast"},
            {"name": "Chicken Curry", "ingredients": ["chicken", "curry powder", "coconut milk", "onion"], "type": "Dinner"}
        ]

    def search_recipes(self, ingredients):
        return [r for r in self.recipes if all(i in r['ingredients'] for i in ingredients)]

    def filter_recipes_by_type(self, recipe_type):
        return [r for r in self.recipes if r['type'].lower() == recipe_type.lower()]

    def filter_ingredients_in_recipe(self, recipe, available_ingredients):
        return [i for i in recipe['ingredients'] if i in available_ingredients]

class RecipeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Recipe Finder")

        # Initialize RecipeFinder instance
        self.recipe_finder = RecipeFinder()

        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        # Label for ingredients input
        self.ingredients_label = tk.Label(self.root, text="Enter ingredients (comma-separated):")
        self.ingredients_label.pack()

        # Entry box for ingredients
        self.ingredients_entry = tk.Entry(self.root)
        self.ingredients_entry.pack()

        # Button to search recipes
        self.search_button = tk.Button(self.root, text="Search Recipes", command=self.search_recipes)
        self.search_button.pack()

        # Label for recipe type drop-down
        self.type_label = tk.Label(self.root, text="Select recipe type:")
        self.type_label.pack()

        # Drop-down menu for recipe type selection
        self.recipe_type_var = tk.StringVar()
        self.recipe_type_menu = ttk.Combobox(self.root, textvariable=self.recipe_type_var)
        self.recipe_type_menu['values'] = ("Breakfast", "Lunch", "Dinner")
        self.recipe_type_menu.pack()

        # Button to filter recipes by selected type
        self.filter_button = tk.Button(self.root, text="Filter Recipes by Type", command=self.filter_by_type)
        self.filter_button.pack()

        # Text box for displaying results
        self.results_text = tk.Text(self.root, height=10, width=50)
        self.results_text.pack()

    def search_recipes(self):
        # Get user input
        ingredients = self.ingredients_entry.get().strip().split(",")
        available_ingredients = [i.strip() for i in ingredients]

        # Find matching recipes
        results = self.recipe_finder.search_recipes(available_ingredients)

        # Display the results
        self.display_results(results, available_ingredients)

    def filter_by_type(self):
        # Get user input for ingredients
        ingredients = self.ingredients_entry.get().strip().split(",")
        available_ingredients = [i.strip() for i in ingredients]

        # Get the selected recipe type from the drop-down menu
        recipe_type = self.recipe_type_var.get()

        # Filter recipes based on type and available ingredients
        results = self.recipe_finder.filter_recipes_by_type(recipe_type)

        # Further filter the results to show only those with available ingredients
        results = [r for r in results if any(i in available_ingredients for i in r['ingredients'])]

        # Display the results
        self.display_results(results, available_ingredients)

    def display_results(self, results, available_ingredients):
        # Clear the text box before displaying new results
        self.results_text.delete(1.0, tk.END)

        if results:
            for r in results:
                filtered_ingredients = self.recipe_finder.filter_ingredients_in_recipe(r, available_ingredients)
                self.results_text.insert(tk.END, f"- {r['name']} ({', '.join(filtered_ingredients)})\n")
        else:
            self.results_text.insert(tk.END, "No recipes found with the available ingredients.\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = RecipeApp(root)
    root.mainloop()
