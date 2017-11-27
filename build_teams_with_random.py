import numpy as np

def build_random_teams(num_teams, people, features):
    # initialize the list of team, male, and female
    teams = []
    male = []
    female = []
    team_choices = range(num_teams)
    i = 0

    # create empty list of each team
    l = len(people)
    for t in range(num_teams):
        teams.append([])

    # determine person that maximizes variance
    while people != []:
        np.random.shuffle(people)
        p = people.pop()
        teams[i].append(p)
        i += 1
        if i == len(teams):
            i = 0
            
    return teams

# Assign individuals based on round robin
def round_robin(teams, people, team_choices, features, reversed):
    # reversed : this is to balance the number of each teams in case the number of group is not divided by the team_num
    while len(people) > 0:
        max_var = 0
        max_var_idx = 0

        # if we've gone through the round, construct the team list
        if len(team_choices) == 0:
            team_choices = range(num_teams)
            if reversed:
                team_choices = team_choices[::-1]

        curr_team = teams[team_choices[0]]
        team_choices = np.delete(team_choices, 0)

        # determine person that maximizes variance
        for i in range(len(people)):
            var = calc_var(np.append(curr_team, people[i]), features)
            if var > max_var:
                max_var = var
                max_var_idx = i

        curr_team.append(people[max_var_idx])
        people = np.delete(people, max_var_idx)

# randomly initialize teams
def init_teams(teams, people, num_teams):
    # might change later
    for i in range(num_teams):
        np.random.shuffle(people)
        p = people.pop()
        teams[i].append(p)

# calculate the variace
def calc_var(team, features):
    var = 0
    for f in features:
        vals = []
        for p in team:
            vals.append(p[f])

        var += np.var(vals)

    return var

# shows all individuals assigned to their teams
def show_team(teams):
    num = 1
    for team in teams:
        print "Team " + str(num) + ". "
        for indiv in team:
            print (indiv)
        num += 1



if __name__ == '__main__':
    # people = [{'feat_1':.15842, 'feat_2':.11582}, {'feat_1':.28832, 'feat_2':.22845}, {'feat_1':.35483, 'feat_2':.33574},
    #             {'feat_1':.42372, 'feat_2':.44683}, {'feat_1':.55693, 'feat_2':.55293}, {'feat_1':.65632, 'feat_2':.66492},
    #             {'feat_1':.73154, 'feat_2':.77482}, {'feat_1':.84038, 'feat_2':.88102}, {'feat_1':.91327, 'feat_2':.99230}]
    people = [{'feat_1':.15842, 'feat_2':.11582, 'feat_3':.14323, 'gender':'m'},
            {'feat_1':.28832, 'feat_2':.22845, 'feat_3':.24323, 'gender':'f'},
            {'feat_1':.35483, 'feat_2':.33574, 'feat_3':.34323, 'gender':'f'},
            {'feat_1':.42372, 'feat_2':.44683, 'feat_3':.44323, 'gender':'f'},
            {'feat_1':.55693, 'feat_2':.55293, 'feat_3':.54323, 'gender':'f'},
            {'feat_1':.65632, 'feat_2':.66492, 'feat_3':.64323, 'gender':'f'},
            {'feat_1':.73154, 'feat_2':.77482, 'feat_3':.74323, 'gender':'m'},
            {'feat_1':.84038, 'feat_2':.88102, 'feat_3':.84323, 'gender':'f'},
            {'feat_1':.91327, 'feat_2':.99230, 'feat_3':.94323, 'gender':'m'}]
    features = ['feat_1', 'feat_2', 'feat_3']
    num_teams = 3


    team = build_random_teams(num_teams, people, features)
    show_team(team)
