from datetime import datetime 

class Food:
    def __init__(self, name, protein, carbs, fat, cals):
        self.name = name
        self.protein = protein
        self.carbs = carbs
        self.fat = fat
        self.cals = cals

    def __repr__(self):
        return f"<Food({self.name} - P: {self.protein}, C: {self.carbs}, F: {self.fat}, Calories: {self.cals}>"

class Meal:

    def __init__(self, name, foods:list):
        self.name = name
        #self.foods = foods
        self.protein = 0
        self.carbs = 0
        self.fat = 0
        self.cals = 0

        for food in foods:
            self.protein += food["protein"]
            self.carbs += food["carbs"]
            self.fat += food["fat"]
            self.cals += food["cals"]

    def __repr__(self):
        return f"<Meal({self.name} - P: {self.protein}, C: {self.carbs}, F: {self.fat}, Calories: {self.cals}>"


if __name__ == "__main__":
    test_food_1 = Food("Food 1", 20, 10, 5, 500)
    test_food_2 = Food("Food 2", 40, 20, 10, 1000)

    test_meal_1 = Meal("Meal 1", [test_food_1.__dict__, test_food_2.__dict__])

    print(test_food_1)
    print(test_food_2)
    print(test_meal_1)

    print(test_food_1.__dict__)




