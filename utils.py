import os, sys
import requests
import json
from watson_developer_cloud import *
import matplotlib.pyplot as plt

def plot_traits(profiles, show = True, save = False):
    values = {}
    needs = {}
    personality = {}

    first = True
    for p in profiles:
        if first:
            for value in p['values']:
                values[value['name']] = []
            for need in p['needs']:
                needs[need['name']] = []
            for category in p['personality']:
                personality[category['name']] = {}
                for trait in category['children']:
                    personality[category['name']][trait['name']] = []

        for value in p['values']:
            values[value['name']].append(value['raw_score'])
        for need in p['needs']:
            needs[need['name']].append(need['raw_score'])
        for category in p['personality']:
            for trait in category['children']:
                personality[category['name']][trait['name']].append(trait['raw_score'])

        first = False

    # plots histogram of traits - 6 per graph
    for value_name in values.keys():
        plt.hist(values[value_name], 'auto', histtype = "step", label = value_name)

    plt.title('Values')
    plt.legend()

    if show:
        plt.show()
    if save:
        plt.savefig('Values.png')

    plt.close()

    for need_name in needs.keys()[0:6]:
        plt.hist(needs[need_name], 'auto', histtype = "step", label = need_name)

    plt.title('Needs - 1')
    plt.legend()

    if show:
        plt.show()
    if save:
        plt.savefig('Needs_1.png')
    plt.close()

    for need_name in needs.keys()[6:]:
        plt.hist(needs[need_name], 'auto', histtype = "step", label = need_name)

    plt.title('Needs - 2')
    plt.legend()

    if show:
        plt.show()
    if save:
        plt.savefig('Needs_2.png')

    plt.close()

    for category_name in personality.keys():
        for trait_name in personality[category_name].keys():
            plt.hist(personality[category_name][trait_name], 'auto', histtype = "step", label = trait_name)

        plt.title('Personality - %s' % category_name)
        plt.legend()

        if show:
            plt.show()
        if save:
            plt.savefig('Personality_%s.png' % category_name)

        plt.close()


def get_profile(text, essay_num = None):
    # try to get from personalities.json
    try:
        f = json.load(open('profiles.json'))
        return f[essay_num]

    except:
        print "Making API request..."
        personality_insights = PersonalityInsightsV3(
            version='2017-10-13',
            username='bf854d08-a553-4339-a641-d7667a2c41aa',
            password='E7HvgPrFrDfj'
        )

        profile = personality_insights.profile(
            text, content_type='text/plain',
            raw_scores=True, consumption_preferences=True)

        return profile


def analyze_dir(text_files_dir):
    profiles = []

    for f_name in os.listdir(text_files_dir):
        file_name, file_extension = os.path.splitext(f_name)

        # only use files with .txt extension
        if file_extension != '.txt':
            continue

        text = open(os.path.join(text_files_dir, f_name)).read()
        essay_num = file_name.split('essay')[-1]

        profile = get_profile(text, essay_num = essay_num)
        profiles.append(profile)

    return profiles


def main():
    try:
        text_files_dir = sys.argv[1]
    except:
        print "You must provide a path to a directory of text files."
        sys.exit(0)

    profiles = analyze_dir(text_files_dir)
    plot_traits(profiles, save = True, show = False)

if __name__ == '__main__':
    main()
