class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        hashmap = {}
        supplies_set = set(supplies)
        
        # Build a mapping of recipes to their ingredients
        for i in range(len(recipes)):
            hashmap[recipes[i]] = ingredients[i]
        
        ans = []
        # To keep track of which recipes we can already make
        can_make = set(supplies_set)
        
        # Iterate over recipes and check if we can make them
        while True:
            made_any = False  # Flag to check if any recipe was made in this round
            for recipe in recipes:
                if recipe not in can_make:
                    ingredient = hashmap[recipe]
                    # Check if all ingredients are in supplies or can be made
                    if all(ingredient_item in can_make for ingredient_item in ingredient):
                        can_make.add(recipe)
                        ans.append(recipe)
                        made_any = True
            if not made_any:  # No new recipe was made in this round, break out
                break
        
        return ans
