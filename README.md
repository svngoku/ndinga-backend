# Building 


> docker build -t flask-tutorial:latest .


```py
@app.route('/api/v1/kg_fr', methods=['POST'])
def add_translation():
  kg = request.json['ki']
  fr = request.json['fr']
  translation_id = kg_fr_collection.insert({'ki': kg, 'fr': fr})
  new_translation = kg_fr_collection.find_one({'_id': translation_id })
  output = {'ki' : new_translation['ki'], 'fr' : new_translation['fr']}
  return jsonify({'result' : output})

```