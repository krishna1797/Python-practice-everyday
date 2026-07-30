#practice for if/elif/else by project of learn how to cook

RECIPES = {
    "paneer": {
        "ingredients": ["1 kg paneer", "masala", "salt", "1 cup water", "vegetables"],
        "steps": [
            "Cut the paneer into cubes.",
            "Add masala and salt to the paneer.",
            "Add 1 cup water and the vegetables.",
            "Cook until everything is well combined.",
        ],
    },
    "pasta": {
        "ingredients": ["pasta", "water", "maggi masala", "cheese"],
        "steps": [
            "Take a bowl and add water and pasta to it.",
            "Add maggi masala and cheese.",
            "Cook until the pasta is soft.",
        ],
    },
    "chicken": {
        "ingredients": ["chicken", "spices of choice"],
        "steps": [
            "Wash the chicken thoroughly.",
            "Cook the chicken with your favourite spices.",
        ],
    },
    "pizza": {
        "ingredients": ["pizza base", "cheese", "toppings of choice"],
        "steps": [
            "Take a pizza base.",
            "Add a generous layer of cheese.",
            "Add extra cheese if you like it cheesy.",
            "Bake and enjoy!",
        ],
    },
}
 
 
def show_recipe(name: str) -> None:
    """Print ingredients and steps for a recipe in a numbered, readable format."""
    recipe = RECIPES[name]
 
    print(f"\n===== {name.title()} Recipe =====")
    print("\nIngredients:")
    for item in recipe["ingredients"]:
        print(f"  - {item}")
 
    print("\nSteps:")
    for i, step in enumerate(recipe["steps"], start=1):
        print(f"  {i}. {step}")
 
    print("\nDONE! Now go enjoy your", name, ":)\n")
 
 
def main() -> None:
    print("Hello! Welcome to my recipe program.")
    print("Today I'll teach you how to make your favourite dish.\n")
    print(f"Available dishes: {', '.join(RECIPES.keys())}")
 
    while True:
        choice = input("\nEnter your favourite dish (or 'no' to quit): ").strip().lower()
 
        if choice == "no":
            print("Thanks for cooking with me. Bye!")
            break
 
        if choice in RECIPES:
            show_recipe(choice)
        else:
            print("I don't know that one yet... order from Zomato instead! 🍽️")
 
 
if __name__ == "__main__":
    main()toooo ")
