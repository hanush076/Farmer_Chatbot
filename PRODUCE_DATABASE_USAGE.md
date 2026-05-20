# How to Use the Produce Database

## Quick Start Guide

### 1. Accessing Produce Data

```python
import json

# Load the complete produce database
with open('data/produce_database.json', 'r') as f:
    produce_db = json.load(f)

# Get information about a specific vegetable
tomato_data = produce_db['vegetables']['tomato']
print(f"Tomato growing season: {tomato_data['growing_season']}")
print(f"Water requirement: {tomato_data['water_requirement']}")
print(f"Diseases: {', '.join(tomato_data['diseases'])}")

# Get fruit information
mango_data = produce_db['fruits']['mango']
print(f"Mango yield: {mango_data['yield']}")
print(f"Market price: {mango_data['market_price_range']}")
```

---

### 2. Using Knowledge Base

```python
# Load expanded knowledge base
with open('data/knowledge_base_expanded.json', 'r') as f:
    kb = json.load(f)

# Get crop-specific guidance
tomato_guide = kb['produce_guide']['vegetables']['tomato']
print(f"Fertilizer: {tomato_guide['fertilizer']}")
print(f"Ideal climate: {tomato_guide['ideal_climate']}")
print(f"Harvesting: {tomato_guide['harvesting']}")

# Get disease management
disease_info = kb['crop_diseases']['tomato']
for disease in disease_info:
    print(f"Disease: {disease['disease']}")
    print(f"Symptoms: {disease['symptoms']}")
    print(f"Treatment: {disease['treatment']}")
```

---

### 3. Training Data for Chatbot

```python
# Load training data
with open('data/training_data_produce.json', 'r') as f:
    training_data = json.load(f)

# Example: Get all patterns for crop growing season
for intent in training_data:
    if intent['intent'] == 'crop_growing_season':
        patterns = intent['patterns']
        for pattern in patterns:
            print(f"Pattern: {pattern}")
        
        # Get training examples
        for example in intent['training_data']:
            print(f"Q: {example.get('crop')} - {pattern}")
            print(f"A: {example.get('response')}\n")
```

---

### 4. Sample Queries & Responses

#### Query 1: Growing Season
```
User: "When should I plant tomato?"
Database lookup: produce_db['vegetables']['tomato']['growing_season']
Response: "Tomato can be grown year-round with controlled conditions, but optimal 
season is March-June and September-November. Temperature should be 20-28°C."
```

#### Query 2: Disease Management
```
User: "Tomato has brown spots on leaves"
Lookup: kb['crop_diseases']['tomato'] + produce_db['vegetables']['tomato']['diseases']
Response: "This looks like Early Blight. Symptoms include brown spots on lower 
leaves with yellow halos. Remove affected leaves immediately and apply 
copper-based fungicide every 7-10 days."
```

#### Query 3: Profitability
```
User: "What profit from tomato farming?"
Lookup: training_data['profitability_analysis']
Response: "Tomato costs ₹3-4 lakh/hectare. With 40-50 tons yield at ₹25 average 
price, gross income ₹10-12.5 lakh. Net profit ₹5-7 lakh/hectare."
```

#### Query 4: Market Price
```
User: "Current price of mango?"
Lookup: produce_db['fruits']['mango']['market_price_range']
Response: "Mango price ranges ₹50-150 per kg. Premium varieties command higher 
prices. Check AGMARKNET for daily market rates in your region."
```

---

### 5. Data Structure Reference

```json
{
  "vegetables": {
    "tomato": {
      "name": "Tomato",
      "type": "vegetable",
      "growing_season": "Year-round with controlled conditions",
      "climate": "Warm season, 20-28°C",
      "soil_type": "Well-drained fertile loamy soil",
      "fertilizer": "15 tons FYM/hectare, N:P:K 100:100:100 kg/hectare",
      "ph_range": "6.0-6.8",
      "water_requirement": "500-700 mm",
      "diseases": ["Early Blight", "Late Blight", "Wilt"],
      "pests": ["Fruit Borer", "Leaf Roller", "Aphids"],
      "yield": "40-50 tons/hectare",
      "market_price_range": "20-40 per kg",
      "storage_life": "7-10 days at 20°C",
      "nutrition_per_100g": {
        "calories": 18,
        "protein": "0.9g",
        "vitamin_c": "13.7mg",
        "lycopene": "2573 mcg"
      },
      "harvesting_tips": "Pick at breaker stage or full ripe"
    }
  }
}
```

---

### 6. Chatbot Integration Example

```python
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load databases
with open('data/produce_database.json', 'r') as f:
    produce_db = json.load(f)

with open('data/knowledge_base_expanded.json', 'r') as f:
    kb = json.load(f)

with open('data/training_data_produce.json', 'r') as f:
    training_data = json.load(f)

@app.route('/api/produce/<crop_name>', methods=['GET'])
def get_produce_info(crop_name):
    crop_name = crop_name.lower().replace(' ', '_')
    
    # Check vegetables
    if crop_name in produce_db['vegetables']:
        return jsonify(produce_db['vegetables'][crop_name])
    
    # Check fruits
    if crop_name in produce_db['fruits']:
        return jsonify(produce_db['fruits'][crop_name])
    
    return jsonify({'error': 'Produce not found'}), 404

@app.route('/api/disease/<crop>/<disease>', methods=['GET')
def get_disease_info(crop, disease):
    crop = crop.lower()
    disease = disease.lower()
    
    if crop in kb['crop_diseases']:
        for disease_info in kb['crop_diseases'][crop]:
            if disease_info['disease'].lower() == disease:
                return jsonify(disease_info)
    
    return jsonify({'error': 'Disease information not found'}), 404

@app.route('/api/fertilizer/<crop>', methods=['GET'])
def get_fertilizer_info(crop):
    crop = crop.lower()
    
    # Check vegetables
    if crop in kb['produce_guide']['vegetables']:
        fertilizer = kb['produce_guide']['vegetables'][crop]['fertilizer']
        return jsonify({'crop': crop, 'fertilizer': fertilizer})
    
    # Check fruits
    if crop in kb['produce_guide']['fruits']:
        fertilizer = kb['produce_guide']['fruits'][crop]['fertilizer']
        return jsonify({'crop': crop, 'fertilizer': fertilizer})
    
    return jsonify({'error': 'Crop not found'}), 404
```

---

### 7. API Response Examples

#### GET /api/produce/tomato
```json
{
  "name": "Tomato",
  "growing_season": "Year-round with controlled conditions",
  "climate": "Warm season, 20-28°C",
  "yield": "40-50 tons/hectare",
  "market_price_range": "20-40 per kg",
  "fertilizer": "15 tons FYM/hectare, N:P:K 100:100:100 kg/hectare"
}
```

#### GET /api/disease/tomato/early%20blight
```json
{
  "disease": "Early Blight",
  "symptoms": "Brown spots on lower leaves, yellow halos, progressive upward",
  "treatment": "Remove affected leaves, apply copper-based fungicide every 7-10 days",
  "prevention": "Proper spacing, avoid overhead watering, remove dead leaves"
}
```

---

### 8. Search Functionality Example

```python
def search_produce(query, db):
    """Search for produce by name or characteristics"""
    query = query.lower()
    results = []
    
    # Search vegetables
    for crop_name, crop_data in db['vegetables'].items():
        if query in crop_name or query in crop_data.get('name', '').lower():
            results.append({'name': crop_name, 'type': 'vegetable', 'data': crop_data})
    
    # Search fruits
    for crop_name, crop_data in db['fruits'].items():
        if query in crop_name or query in crop_data.get('name', '').lower():
            results.append({'name': crop_name, 'type': 'fruit', 'data': crop_data})
    
    return results

# Usage
results = search_produce('mango', produce_db)
for result in results:
    print(f"Found: {result['name']} ({result['type']})")
```

---

### 9. Seasonal Recommendations

```python
def get_seasonal_crops(month):
    """Get crops suitable for a particular month"""
    seasons = {
        'monsoon': ['beans', 'bhindi', 'okra', 'banana'],
        'summer': ['tomato', 'chili', 'brinjal', 'watermelon'],
        'winter': ['potato', 'onion', 'carrot', 'cabbage', 'pea']
    }
    
    month_to_season = {
        6: 'monsoon', 7: 'monsoon', 8: 'monsoon', 9: 'monsoon',
        10: 'winter', 11: 'winter', 12: 'winter', 1: 'winter',
        2: 'winter', 3: 'summer', 4: 'summer', 5: 'summer'
    }
    
    season = month_to_season.get(month)
    return seasons.get(season, [])

# Usage
suitable_crops = get_seasonal_crops(6)  # June = Monsoon
print(f"Good crops for June: {suitable_crops}")
```

---

### 10. Performance & Optimization

- **File sizes**: Each JSON file < 2MB
- **Load time**: < 100ms for complete database
- **Query time**: < 10ms for single crop lookup
- **Caching**: Recommended for frequently accessed data
- **Database**: Can be migrated to MongoDB/SQL for scale

---

## Tips for Best Results

1. **Case Handling**: Convert all queries to lowercase for consistent matching
2. **Space Handling**: Replace spaces with underscores for crop names
3. **Alternative Names**: Map common names (okra = bhindi, eggplant = brinjal)
4. **Validation**: Check if crop exists before accessing data
5. **Error Handling**: Provide helpful messages when data not found
6. **Caching**: Cache frequently requested crops for performance
7. **Updates**: Update prices seasonally (quarterly recommended)
8. **Versioning**: Keep backup of data files before updates

---

## Data Maintenance

### Update Frequency:
- **Market Prices**: Weekly/Monthly
- **Diseases**: Quarterly or after new outbreaks
- **Varieties**: Annually
- **Fertilizer Data**: As recommendations change
- **Nutritional Data**: Reference data (rarely changes)

### Quality Checks:
- Validate NPK values
- Verify yields with agricultural department
- Cross-check market prices with AGMARKNET
- Review disease information with agricultural experts

---
