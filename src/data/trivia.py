"""
Agricultural trivia questions for Cholan AI Bot
"""

import random
from typing import List, Dict, Any

# ========== TRIVIA QUESTIONS ==========
TRIVIA_QUESTIONS: List[Dict[str, Any]] = [
    {
        "question": "What process do plants use to make food using sunlight?",
        "options": ["Respiration", "Photosynthesis", "Transpiration", "Germination"],
        "answer": "Photosynthesis",
        "category": "plant_biology",
        "difficulty": "easy"
    },
    {
        "question": "Which nutrient is most essential for plant growth and green color?",
        "options": ["Phosphorus", "Potassium", "Nitrogen", "Calcium"],
        "answer": "Nitrogen",
        "category": "plant_nutrition",
        "difficulty": "easy"
    },
    {
        "question": "What is the ideal pH range for most crops?",
        "options": ["4.0-5.0", "6.0-7.0", "8.0-9.0", "9.0-10.0"],
        "answer": "6.0-7.0",
        "category": "soil_science",
        "difficulty": "medium"
    },
    {
        "question": "Which farming practice helps prevent soil erosion?",
        "options": ["Monoculture", "Contour plowing", "Deep tillage", "Bare fallowing"],
        "answer": "Contour plowing",
        "category": "soil_conservation",
        "difficulty": "medium"
    },
    {
        "question": "What does NPK stand for in fertilizers?",
        "options": ["Nitrogen, Phosphorus, Potassium", "Nitrate, Phosphate, Potash", "Natural Plant Killer", "New Plant Knowledge"],
        "answer": "Nitrogen, Phosphorus, Potassium",
        "category": "plant_nutrition",
        "difficulty": "easy"
    },
    {
        "question": "Which crop is known as 'Queen of Cereals'?",
        "options": ["Rice", "Wheat", "Maize", "Barley"],
        "answer": "Maize",
        "category": "crops",
        "difficulty": "medium"
    },
    {
        "question": "What is crop rotation primarily used for?",
        "options": ["Increasing yield", "Soil fertility management", "Pest control", "All of the above"],
        "answer": "All of the above",
        "category": "crop_management",
        "difficulty": "medium"
    },
    {
        "question": "Which is the most water-efficient irrigation method?",
        "options": ["Flood irrigation", "Sprinkler irrigation", "Drip irrigation", "Furrow irrigation"],
        "answer": "Drip irrigation",
        "category": "irrigation",
        "difficulty": "easy"
    },
    {
        "question": "What is the green revolution associated with?",
        "options": ["Organic farming", "High-yielding varieties", "Sustainable agriculture", "Traditional farming"],
        "answer": "High-yielding varieties",
        "category": "agricultural_history",
        "difficulty": "medium"
    },
    {
        "question": "Which pest management approach uses natural enemies?",
        "options": ["Chemical control", "Biological control", "Cultural control", "Mechanical control"],
        "answer": "Biological control",
        "category": "pest_management",
        "difficulty": "medium"
    },
    {
        "question": "Which hormone is responsible for fruit ripening?",
        "options": ["Auxin", "Gibberellin", "Ethylene", "Cytokinin"],
        "answer": "Ethylene",
        "category": "plant_biology",
        "difficulty": "hard"
    },
    {
        "question": "What is the most abundant gas in Earth's atmosphere that plants cannot directly use?",
        "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"],
        "answer": "Nitrogen",
        "category": "plant_biology",
        "difficulty": "medium"
    },
    {
        "question": "Which part of the plant conducts water upward?",
        "options": ["Phloem", "Xylem", "Cambium", "Epidermis"],
        "answer": "Xylem",
        "category": "plant_anatomy",
        "difficulty": "medium"
    },
    {
        "question": "What is the term for growing plants without soil?",
        "options": ["Aeroponics", "Hydroponics", "Aquaponics", "Geoponics"],
        "answer": "Hydroponics",
        "category": "modern_agriculture",
        "difficulty": "easy"
    },
    {
        "question": "Which country is the largest producer of rice in the world?",
        "options": ["India", "China", "Thailand", "Vietnam"],
        "answer": "China",
        "category": "global_agriculture",
        "difficulty": "medium"
    },
    {
        "question": "What is the primary cause of yellowing leaves in plants?",
        "options": ["Overwatering", "Nitrogen deficiency", "Too much sunlight", "Root rot"],
        "answer": "Nitrogen deficiency",
        "category": "plant_health",
        "difficulty": "medium"
    },
    {
        "question": "Which insect is considered most beneficial for crop pollination?",
        "options": ["Butterfly", "Bee", "Ladybug", "Dragonfly"],
        "answer": "Bee",
        "category": "beneficial_insects",
        "difficulty": "easy"
    },
    {
        "question": "What does 'organic farming' primarily avoid using?",
        "options": ["Water", "Natural fertilizers", "Synthetic chemicals", "Crop rotation"],
        "answer": "Synthetic chemicals",
        "category": "organic_farming",
        "difficulty": "easy"
    },
    {
        "question": "Which soil type retains water best?",
        "options": ["Sandy soil", "Clay soil", "Loamy soil", "Rocky soil"],
        "answer": "Clay soil",
        "category": "soil_science",
        "difficulty": "medium"
    },
    {
        "question": "What is the process of removing excess water from soil called?",
        "options": ["Irrigation", "Drainage", "Mulching", "Composting"],
        "answer": "Drainage",
        "category": "soil_management",
        "difficulty": "easy"
    }
]

# ========== ADVANCED TRIVIA QUESTIONS ==========
ADVANCED_TRIVIA: List[Dict[str, Any]] = [
    {
        "question": "What is the C4 photosynthesis pathway primarily adapted for?",
        "options": ["Cold climates", "Hot, dry climates", "Wet conditions", "Low light conditions"],
        "answer": "Hot, dry climates",
        "category": "plant_physiology",
        "difficulty": "hard"
    },
    {
        "question": "Which element is essential for chlorophyll formation?",
        "options": ["Iron", "Magnesium", "Zinc", "Copper"],
        "answer": "Magnesium",
        "category": "plant_nutrition",
        "difficulty": "hard"
    },
    {
        "question": "What is allelopathy in agriculture?",
        "options": ["Cross-pollination", "Chemical inhibition between plants", "Soil compaction", "Water competition"],
        "answer": "Chemical inhibition between plants",
        "category": "plant_ecology",
        "difficulty": "hard"
    }
]

def get_random_trivia() -> Dict[str, Any]:
    """Get a random trivia question"""
    return random.choice(TRIVIA_QUESTIONS)

def get_trivia_by_difficulty(difficulty: str) -> Dict[str, Any]:
    """Get trivia question by difficulty level"""
    filtered_questions = [q for q in TRIVIA_QUESTIONS if q["difficulty"] == difficulty.lower()]
    if not filtered_questions:
        return get_random_trivia()
    return random.choice(filtered_questions)

def get_trivia_by_category(category: str) -> Dict[str, Any]:
    """Get trivia question by category"""
    filtered_questions = [q for q in TRIVIA_QUESTIONS if q["category"] == category.lower()]
    if not filtered_questions:
        return get_random_trivia()
    return random.choice(filtered_questions)

def get_easy_trivia() -> Dict[str, Any]:
    """Get an easy trivia question"""
    return get_trivia_by_difficulty("easy")

def get_medium_trivia() -> Dict[str, Any]:
    """Get a medium difficulty trivia question"""
    return get_trivia_by_difficulty("medium")

def get_hard_trivia() -> Dict[str, Any]:
    """Get a hard trivia question"""
    hard_questions = [q for q in TRIVIA_QUESTIONS + ADVANCED_TRIVIA if q["difficulty"] == "hard"]
    return random.choice(hard_questions) if hard_questions else get_random_trivia()

# ========== TRIVIA CATEGORIES ==========
TRIVIA_CATEGORIES = {
    "plant_biology": "Plant Biology & Physiology",
    "plant_nutrition": "Plant Nutrition",
    "soil_science": "Soil Science",
    "soil_conservation": "Soil Conservation", 
    "crops": "Crop Knowledge",
    "crop_management": "Crop Management",
    "irrigation": "Irrigation & Water Management",
    "agricultural_history": "Agricultural History",
    "pest_management": "Pest Management",
    "plant_anatomy": "Plant Anatomy",
    "modern_agriculture": "Modern Agriculture",
    "global_agriculture": "Global Agriculture",
    "plant_health": "Plant Health",
    "beneficial_insects": "Beneficial Insects",
    "organic_farming": "Organic Farming",
    "soil_management": "Soil Management",
    "plant_physiology": "Advanced Plant Physiology",
    "plant_ecology": "Plant Ecology"
}

def get_available_categories() -> Dict[str, str]:
    """Get all available trivia categories"""
    return TRIVIA_CATEGORIES

def get_trivia_stats() -> Dict[str, Any]:
    """Get statistics about trivia questions"""
    total_questions = len(TRIVIA_QUESTIONS) + len(ADVANCED_TRIVIA)
    difficulty_counts = {"easy": 0, "medium": 0, "hard": 0}
    category_counts = {}
    
    all_questions = TRIVIA_QUESTIONS + ADVANCED_TRIVIA
    
    for question in all_questions:
        difficulty_counts[question["difficulty"]] += 1
        category = question["category"]
        category_counts[category] = category_counts.get(category, 0) + 1
    
    return {
        "total_questions": total_questions,
        "difficulty_breakdown": difficulty_counts,
        "category_breakdown": category_counts,
        "categories_available": len(category_counts)
    }

def create_custom_trivia(question: str, options: List[str], answer: str, 
                        category: str = "custom", difficulty: str = "medium") -> Dict[str, Any]:
    """Create a custom trivia question"""
    return {
        "question": question,
        "options": options,
        "answer": answer,
        "category": category,
        "difficulty": difficulty
    }

# ========== SEASONAL TRIVIA ==========
def get_seasonal_trivia(season: str) -> Dict[str, Any]:
    """Get season-specific trivia questions"""
    season_lower = season.lower()
    
    seasonal_questions = {
        "spring": [
            {
                "question": "Which is the best time to plant most annual flowers?",
                "options": ["Early spring", "Late spring", "After last frost", "Mid-winter"],
                "answer": "After last frost",
                "category": "seasonal_farming",
                "difficulty": "easy"
            }
        ],
        "summer": [
            {
                "question": "What is the main challenge for crops during summer?",
                "options": ["Too much water", "Water stress", "Cold damage", "Lack of sunlight"],
                "answer": "Water stress",
                "category": "seasonal_farming", 
                "difficulty": "easy"
            }
        ],
        "autumn": [
            {
                "question": "Why is autumn called 'harvest season'?",
                "options": ["Crops are planted", "Crops mature and are ready to harvest", "Animals hibernate", "Soil is prepared"],
                "answer": "Crops mature and are ready to harvest",
                "category": "seasonal_farming",
                "difficulty": "easy"
            }
        ],
        "winter": [
            {
                "question": "What farming activity is commonly done in winter?",
                "options": ["Planting crops", "Harvesting", "Planning and equipment maintenance", "Pest control"],
                "answer": "Planning and equipment maintenance",
                "category": "seasonal_farming",
                "difficulty": "easy"
            }
        ]
    }
    
    if season_lower in seasonal_questions:
        return random.choice(seasonal_questions[season_lower])
    
    return get_random_trivia()
