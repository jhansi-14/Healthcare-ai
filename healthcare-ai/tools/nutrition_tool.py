def analyze_nutrition(calories, protein, carbs, fats):

    total = protein*4 + carbs*4 + fats*9

    if total > calories:
        return "Macronutrient values exceed calorie limit"

    return {
        "protein_percent": (protein*4)/calories*100,
        "carbs_percent": (carbs*4)/calories*100,
        "fats_percent": (fats*9)/calories*100
    }