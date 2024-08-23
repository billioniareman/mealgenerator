from flask import Flask, request, jsonify
import random
app = Flask(__name__)

meals = {
    "vegetarian": {
        "weight_loss": {
            "breakfast": ["Poha with Vegetables", "Oats Upma", "Vegetable Dalia", "Vegetable Idli",
                          "Multigrain Toast with Avocado", "Methi Thepla with Low-fat Curd"],
            "lunch": ["Moong Dal with Brown Rice", "Mixed Dal with Roti", "Khichdi with Sautéed Veggies",
                      "Vegetable Stir-Fry with Tofu", "Baingan Bharta with Bajra Roti",
                      "Zucchini Noodles with Tomato Sauce"],
            "snacks": ["Fruit Salad", "Roasted Makhana", "Chana Chaat", "Cucumber Sticks with Hummus",
                       "Oats and Flaxseed Crackers", "Tomato and Cucumber Sandwich (Whole Wheat)"],
            "dinner": ["Palak Paneer with Tofu", "Stuffed Capsicum", "Vegetable Soup",
                       "Lauki (Bottle Gourd) Sabzi with Roti", "Grilled Tofu with Veggies", "Spinach and Lentil Soup"]
        },
        "muscle_gain": {
            "breakfast": ["Paneer Paratha", "Besan Chilla", "Protein Smoothie", "Moong Dal Cheela with Stuffed Paneer",
                          "Whole Grain Pancakes with Peanut Butter", "Soy Milk Smoothie with Almonds"],
            "lunch": ["Dal with Brown Rice", "Rajma with Quinoa", "Tofu Stir-Fry", "Paneer Tikka with Millet Roti",
                      "Vegetable Pulao with Soya Chunks", "Sambar with Quinoa"],
            "snacks": ["Greek Yogurt with Nuts", "Chana Chaat", "Peanut Butter Toast", "Homemade Protein Bars",
                       "Trail Mix with Almonds and Walnuts", "Protein-packed Hummus with Carrot Sticks"],
            "dinner": ["Paneer Bhurji with Roti", "Vegetable Biryani", "Dal Makhani", "Soybean Curry with Brown Rice",
                       "Stuffed Paratha with Low-fat Yogurt", "Quinoa and Vegetable Stir-Fry"]
        },
        "staying_fit": {
            "breakfast": ["Vegetable Dalia", "Besan Chilla", "Oatmeal with Nuts", "Masala Oats with Veggies",
                          "Ragi Pancakes with Honey", "Spinach and Mushroom Omelette (Vegetarian)"],
            "lunch": ["Mixed Dal with Roti", "Khichdi with Veggies", "Chana Masala with Quinoa",
                      "Vegetable Subji with Roti", "Curd Rice with Cucumber Raita",
                      "Tofu Bhurji with Multigrain Bread"],
            "snacks": ["Fruit Salad", "Roasted Peanuts", "Sprouts Salad", "Carrot and Cucumber Sticks with Yogurt Dip",
                       "Low-fat Yogurt with Berries", "Whole Wheat Crackers with Cottage Cheese"],
            "dinner": ["Stuffed Capsicum", "Tofu Curry with Roti", "Vegetable Soup", "Palak Dal with Brown Rice",
                       "Grilled Vegetables with Tofu", "Broccoli and Lentil Soup"]
        }
    },
    "vegan": {
        "weight_loss": {
            "breakfast": ["Vegan Upma", "Chia Pudding", "Vegetable Poha", "Vegan Smoothie Bowl with Berries",
                          "Sweet Potato Hash with Avocado", "Oats with Almond Milk and Berries"],
            "lunch": ["Chana Dal with Brown Rice", "Vegan Khichdi", "Mixed Vegetable Curry with Quinoa",
                      "Baked Tofu with Stir-Fried Vegetables", "Pumpkin Soup with Whole Wheat Bread",
                      "Cabbage Salad with Chickpeas"],
            "snacks": ["Fresh Fruit", "Roasted Chana", "Vegan Smoothie", "Apple Slices with Almond Butter",
                       "Cucumber and Tomato Salad", "Baked Sweet Potato Fries"],
            "dinner": ["Tofu and Vegetable Stir-Fry", "Vegan Dal", "Stuffed Bell Peppers",
                       "Grilled Vegetables with Lentils", "Spiced Quinoa with Roasted Vegetables",
                       "Broccoli and Mushroom Stir-Fry"]
        },
        "muscle_gain": {
            "breakfast": ["Tofu Scramble", "Vegan Protein Smoothie", "Chickpea Pancakes", "Quinoa Porridge with Nuts",
                          "Buckwheat Pancakes with Almond Butter", "Lentil Pancakes with Spinach"],
            "lunch": ["Lentil Curry with Brown Rice", "Vegan Tofu Biryani", "Chickpea and Spinach Stew",
                      "Vegan Burrito Bowl with Quinoa", "Soya Chunks with Mixed Vegetables",
                      "Mushroom and Bean Stir-Fry"],
            "snacks": ["Almonds", "Chia Seed Pudding", "Vegan Yogurt with Nuts", "Homemade Energy Bars",
                       "Hummus with Carrot and Celery Sticks", "Roasted Chickpeas"],
            "dinner": ["Vegan Paneer Bhurji", "Mixed Vegetable Curry with Millet Roti", "Lentil Soup",
                       "Vegan Shepherd’s Pie with Lentils", "Tofu Tikka Masala with Brown Rice",
                       "Soya Bean Curry with Quinoa"]
        },
        "staying_fit": {
            "breakfast": ["Vegan Paratha with Avocado", "Chia Seed Pudding", "Vegetable Poha",
                          "Ragi Porridge with Almond Milk", "Oats Pancakes with Fresh Fruit",
                          "Vegan Omelette with Mushrooms"],
            "lunch": ["Mixed Lentil Soup with Brown Rice", "Vegan Tofu Salad", "Chana Masala with Whole Wheat Roti",
                      "Stuffed Bell Peppers with Quinoa", "Vegetable Wrap with Avocado", "Pumpkin and Lentil Stew"],
            "snacks": ["Fruit Salad", "Roasted Nuts", "Vegan Yogurt with Fruit", "Rice Cakes with Almond Butter",
                       "Veggie Sticks with Guacamole", "Vegan Protein Balls"],
            "dinner": ["Stuffed Bell Peppers", "Tofu and Veggie Stir-Fry", "Lentil and Vegetable Soup",
                       "Spinach and Lentil Curry with Millet", "Grilled Tofu with Roasted Veggies",
                       "Zucchini Noodles with Tomato Sauce"]
        }
    }
}


def generate_meal_plan(dietary_pref, goal):
    try:
        meal_plan = {
            "breakfast": random.choice(meals[dietary_pref][goal]["breakfast"]),
            "lunch": random.choice(meals[dietary_pref][goal]["lunch"]),
            "snacks": random.choice(meals[dietary_pref][goal]["snacks"]),
            "dinner": random.choice(meals[dietary_pref][goal]["dinner"])
        }
        return meal_plan
    except KeyError:
        return "Meal plan not available for the selected options."


@app.route('/get_meal', methods=['GET'])
def get_meal():
    dietary_preference = request.args.get('dietary_preference')
    goal = request.args.get('goal')

    if not dietary_preference or not goal:
        return jsonify({"error": "Invalid request parameters"}), 400

    meal_plan = generate_meal_plan(dietary_preference, goal)
    if isinstance(meal_plan, str):
        return jsonify({"error": meal_plan}), 404
    else:
        return jsonify(meal_plan)


if __name__ == '__main__':
    app.run(debug=True)