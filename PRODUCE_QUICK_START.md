# 🚀 Quick Start - Load Your Produce Database

## 30-Second Setup

### Step 1: Load the Data
```python
import json

# Load produce database
with open('data/produce_database.json', 'r') as f:
    produce_db = json.load(f)

# Load knowledge base
with open('data/knowledge_base_expanded.json', 'r') as f:
    kb = json.load(f)

# Load training data
with open('data/training_data_produce.json', 'r') as f:
    training_data = json.load(f)

print("✅ All databases loaded successfully!")
```

---

## Common Queries

### 1. Get Tomato Information
```python
tomato = produce_db['vegetables']['tomato']
print(f"Growing Season: {tomato['growing_season']}")
print(f"Water Need: {tomato['water_requirement']}")
print(f"Fertilizer: {tomato['fertilizer']}")
print(f"Yield: {tomato['yield']}")
print(f"Price: {tomato['market_price_range']}")
```

**Output:**
```
Growing Season: Year-round with controlled conditions
Water Need: 500-700 mm
Fertilizer: 15 tons FYM/hectare, N:P:K 100:100:100 kg/hectare
Yield: 40-50 tons/hectare
Price: ₹20-40 per kg
```

---

### 2. Get Mango Information
```python
mango = produce_db['fruits']['mango']
print(f"Season: {mango['growing_season']}")
print(f"Climate: {mango['climate']}")
print(f"Diseases: {', '.join(mango['diseases'])}")
print(f"Pests: {', '.join(mango['pests'])}")
print(f"Price: {mango['market_price_range']}")
```

**Output:**
```
Season: Spring flowering, summer fruiting
Climate: Tropical to subtropical, 24-30°C
Diseases: Anthracnose, Powdery Mildew, Stem Canker
Pests: Fruit Fly, Leaf Hopper, Shoot Borer
Price: ₹50-150 per kg
```

---

### 3. Get Disease Information
```python
# Get all diseases for tomato
diseases = kb['crop_diseases']['tomato']
for disease in diseases:
    print(f"\n🦠 {disease['disease']}")
    print(f"   Symptoms: {disease['symptoms']}")
    print(f"   Treatment: {disease['treatment']}")
```

**Output:**
```
🦠 Early Blight
   Symptoms: Brown spots on lower leaves, yellow halos, progressive upward
   Treatment: Remove affected leaves, apply copper-based fungicide every 7-10 days

🦠 Late Blight
   Symptoms: Water-soaked lesions on leaves and stems, white mold on undersides
   Treatment: Apply mancozeb or metalaxyl fungicide

🦠 Powdery Mildew
   Symptoms: White powder-like coating on leaves and stems
   Treatment: Spray sulfur or neem oil every 7 days
```

---

### 4. Get Fertilizer Info
```python
# Get fertilizer for different crops
crops = ['tomato', 'potato', 'onion', 'carrot']

for crop in crops:
    if crop in kb['produce_guide']['vegetables']:
        guide = kb['produce_guide']['vegetables'][crop]
        print(f"{crop.capitalize()}: {guide['fertilizer']}")
```

**Output:**
```
Tomato: 15 tons FYM/hectare, N:P:K 100:100:100 kg/hectare
Potato: 20 tons FYM/hectare, N:P:K 80:80:120 kg/hectare
Onion: 10 tons FYM/hectare, N:P:K 80:60:60 kg/hectare
Carrot: 10 tons FYM/hectare, N:P:K 50:100:50 kg/hectare
```

---

### 5. Get All Vegetables
```python
vegetables = list(produce_db['vegetables'].keys())
print(f"Total Vegetables: {len(vegetables)}")
print(f"List: {', '.join(vegetables)}")
```

**Output:**
```
Total Vegetables: 24
List: beans, bhindi, bitter gourd, bottle gourd, brinjal, broccoli, cabbage, 
capsicum, carrot, cauliflower, chili, coriander, cucumber, garlic, ladies finger, 
lettuce, okra, onion, pea, potato, pumpkin, radish, ridge gourd, spinach, 
squash, tomato
```

---

### 6. Get All Fruits
```python
fruits = list(produce_db['fruits'].keys())
print(f"Total Fruits: {len(fruits)}")
print(f"List: {', '.join(fruits)}")
```

**Output:**
```
Total Fruits: 15
List: amla, apple, apricot, banana, coconut, grape, guava, jackfruit, lemon, 
mango, orange, papaya, pineapple, pomegranate, strawberry, watermelon
```

---

### 7. Search for Crop
```python
def search_crop(query, db):
    query_lower = query.lower()
    results = []
    
    # Search vegetables
    for crop_name, crop_data in db['vegetables'].items():
        if query_lower in crop_name:
            results.append({'crop': crop_name, 'type': 'vegetable'})
    
    # Search fruits
    for crop_name, crop_data in db['fruits'].items():
        if query_lower in crop_name:
            results.append({'crop': crop_name, 'type': 'fruit'})
    
    return results

# Search examples
print(search_crop('gourd', produce_db))
```

---

## API Endpoints to Build

```python
from flask import Flask, jsonify

app = Flask(__name__)

# Load data
with open('data/produce_database.json') as f:
    db = json.load(f)

@app.route('/api/crop/<crop_name>')
def get_crop(crop_name):
    crop_name = crop_name.lower()
    if crop_name in db['vegetables']:
        return jsonify(db['vegetables'][crop_name])
    if crop_name in db['fruits']:
        return jsonify(db['fruits'][crop_name])
    return jsonify({'error': 'Crop not found'}), 404
```

---

## Files Available

📁 **Data Files:**
- `data/produce_database.json` - Main database
- `data/knowledge_base_expanded.json` - Knowledge base
- `data/training_data_produce.json` - Training data

📖 **Documentation:**
- `PRODUCE_DATABASE_INDEX.md` - Quick reference
- `PRODUCE_DATABASE_SUMMARY.md` - Overview
- `PRODUCE_DATABASE_USAGE.md` - Full guide
- `DATA_COMPLETION_REPORT.md` - Project report

---

**Start using the data now! 🎉**
