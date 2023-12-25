import json

with open('area_protegida.json', 'r') as f:
    content = json.load(f)

features = content['features']

parques_nacionales = [f for f in features if f['properties']['gna'] == 'Parque Nacional']

content['features'] = parques_nacionales

with open('parques_nacionales.json', 'w') as f:
    json.dump(content, f)


