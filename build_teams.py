import numpy as np

def build_teams(num_teams, people, features):
    # initialize team list
    teams = []
    l = len(people)
    for t in range(num_teams):
        teams.append([])

    init_teams(teams, people, num_teams)
    assert(len(people) + num_teams == l)

    team_choices = range(num_teams)

    while len(people) > 0:
        max_var = 0
        max_var_idx = 0

        # if we've gone through the round, reshuffle the teams
        if len(team_choices) == 0:
            team_choices = range(num_teams)
            np.random.shuffle(team_choices)

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

    return teams

def init_teams(teams, people, num_teams):
    # might change later
    for i in range(num_teams):
        np.random.shuffle(people)
        p = people.pop()
        teams[i].append(p)

def calc_var(team, features):
    var = 0
    for f in features:
        vals = []
        for p in team:
            vals.append(p[f])

        var += np.var(vals)

    var /= len(team)

    return var


if __name__ == '__main__':
    people = [{'feat_1':.15842, 'feat_2':.11582}, {'feat_1':.28832, 'feat_2':.22845}, {'feat_1':.35483, 'feat_2':.33574},
                {'feat_1':.42372, 'feat_2':.44683}, {'feat_1':.55693, 'feat_2':.55293}, {'feat_1':.65632, 'feat_2':.66492},
                {'feat_1':.73154, 'feat_2':.77482}, {'feat_1':.84038, 'feat_2':.88102}, {'feat_1':.91327, 'feat_2':.99230}]
    features = ['feat_1', 'feat_2']
    num_teams = 2
    make_teams(num_teams, people, features)
