import csv, json

colors = {
    'Needs': '#6F2DBD',
    'Values': '#BF1A2F',
    'Emotional range': '#F00699',
    'Openness': '#018E42',
    'Extraversion': '#F7D002',
    "Agreeableness": '#E86806',
    'Conscientiousness': '#1E54C9'
}
traits_json = {}
with open('static/traits.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        traits_json[row['id']] = {'label': row['label'], 'color': colors[row['category']]}

json.dump(traits_json, open('traits.json','w'), indent=2)
