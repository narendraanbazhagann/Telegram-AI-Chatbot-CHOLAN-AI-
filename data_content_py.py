"""
Static content data for Cholan AI bot
"""

from typing import List, Dict

# Farming jokes
jokes: List[str] = [
    "😂 Why do cows have hooves instead of feet? Because they lactose!",
    "🌾 Why did the scarecrow win an award? Because he was outstanding in his field!",
    "🌴 What kind of tree fits in your hand? A palm tree!",
    "🐔 Why don't farmers tell chicken jokes? Because they would be poultry in motion!",
    "🌽 What do you call a grumpy farmer? A snap pea!",
    "🥕 Why did the farmer bury his money? To make his soil rich!",
    "🍅 What's a tomato's favorite game? Squash!",
    "🐄 What do you call a cow with no legs? Ground beef!"
]

# Agriculture trivia questions
trivia_questions: List[Dict[str, any]] = [
    {
        "question": "What process do plants use to make food from sunlight?",
        "options": ["Respiration", "Photosynthesis", "Transpiration", "Germination"],
        "answer": "Photosynthesis"
    },
    {
        "question": "Which nutrient is most essential for plant growth?",
        "options": ["Protein", "Carbohydrate", "Nitrogen", "Fat"],
        "answer": "Nitrogen"
    },
    {
        "question": "What is the primary gas that plants absorb during photosynthesis?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "answer": "Carbon Dioxide"
    },
    {
        "question": "Which part of the plant is responsible for absorbing water?",
        "options": ["Leaves", "Stem", "Roots", "Flowers"],
        "answer": "Roots"
    },
    {
        "question": "What is the ideal pH range for most crops?",
        "options": ["4.0-5.0", "6.0-7.0", "8.0-9.0", "9.0-10.0"],
        "answer": "6.0-7.0"
    }
]

# Would you rather questions
would_you_rather_questions: List[str] = [
    "Would you rather have a pet cow 🐄 or a pet chicken 🐔?",
    "Would you rather plant a tree 🌳 or grow a vegetable garden 🥕?",
    "Would you rather grow rice 🌾 or grow wheat?",
    "Would you rather have a farm in the mountains 🏔️ or by the sea 🌊?",
    "Would you rather grow organic vegetables 🥬 or beautiful flowers 🌺?",
    "Would you rather have a tractor 🚜 or a greenhouse 🏠?",
    "Would you rather grow bananas 🍌 or mangoes 🥭?",
    "Would you rather raise goats 🐐 or sheep 🐑?"
]

# Emoji responses for keywords
emoji_responses: Dict[str, str] = {
    "happy": "😊",
    "sad": "😢",
    "angry": "😡",
    "love": "❤️",
    "plant": "🌱",
    "harvest": "🌾",
    "farm": "🚜",
    "crop": "🌽",
    "water": "💧",
    "sun": "☀️",
    "rain": "🌧️",
    "soil": "🪨",
    "seed": "🌱",
    "flower": "🌸",
    "fruit": "🍎",
    "vegetable": "🥕",
    "cow": "🐄",
    "chicken": "🐔",
    "pig": "🐷",
    "goat": "🐐",
    "sheep": "🐑"
}
