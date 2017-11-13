import json
import sys

people = []
f_names = open('female_names.txt').readlines()
m_names = open('male_names.txt').readlines()
names = f_names + m_names
profiles = json.load(open('profiles.json'))

for p_id in profiles:
    p_id = int(p_id)
    p = {}
    p['id'] = p_id - 1
    p['name'] = names[p_id - 1].split('\n')[0]
    prof = profiles[str(p_id)]
    for t in prof['needs']:
        trait_id = str(t['trait_id'])
        trait_val = float(t['percentile']) # maybe do percentile?
        p[trait_id] = trait_val

    for t in prof['values']:
        trait_id = str(t['trait_id'])
        trait_val = float(t['percentile']) # maybe do percentile?
        p[trait_id] = trait_val

    for t_cat in prof['personality']:
        for t in t_cat['children']:
            trait_id = str(t['trait_id'])
            trait_val = float(t['percentile']) # maybe do percentile?
            p[trait_id] = trait_val

    people.append(p)

f = open('people.json','w')
json.dump(people, f, indent = 2)
