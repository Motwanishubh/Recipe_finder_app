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

if __name__ == "__main__":
    app = RecipeFinder()

    ingredients = input("Enter ingredients (comma-separated): ").strip().split(",")
    results = app.search_recipes([i.strip() for i in ingredients])

    print("\nMatching Recipes:")
    for r in results:
        print(f"- {r['name']} ({r['type']})")

    recipe_type = input("\nEnter recipe type (Breakfast, Lunch, Dinner): ").strip()
    results = app.filter_recipes_by_type(recipe_type)

    print("\nRecipes by Type:")
    for r in results:
        print(f"- {r['name']} ({', '.join(r['ingredients'])})")
