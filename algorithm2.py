import random
import numpy as np

team_num = 3 # parameters for the number of teams
feat_num = 3 # parameters for the number of features
feat_param = ['feat_1', 'feat_2', 'feat_3'] # parameters for the features
team_count = 0
round_count = 1

# students = [{'feat_1':.15842, 'feat_2':.11582}, {'feat_1':.28832, 'feat_2':.22845}, {'feat_1':.35483, 'feat_2':.33574},
#             {'feat_1':.42372, 'feat_2':.44683}, {'feat_1':.55693, 'feat_2':.55293}, {'feat_1':.65632, 'feat_2':.66492},
#             {'feat_1':.73154, 'feat_2':.77482}, {'feat_1':.84038, 'feat_2':.88102}, {'feat_1':.91327, 'feat_2':.99230}]

students = [{'feat_1':.15842, 'feat_2':.11582, 'feat_3':.14323},
            {'feat_1':.28832, 'feat_2':.22845, 'feat_3':.24323},
            {'feat_1':.35483, 'feat_2':.33574, 'feat_3':.34323},
            {'feat_1':.42372, 'feat_2':.44683, 'feat_3':.44323},
            {'feat_1':.55693, 'feat_2':.55293, 'feat_3':.54323},
            {'feat_1':.65632, 'feat_2':.66492, 'feat_3':.64323},
            {'feat_1':.73154, 'feat_2':.77482, 'feat_3':.74323},
            {'feat_1':.84038, 'feat_2':.88102, 'feat_3':.84323},
            {'feat_1':.91327, 'feat_2':.99230, 'feat_3':.94323}]
teams = []

def show_team(teams, round_count):
    print ("\n" + "===== Team Status (round " + str(round_count) + ") =====")
    for i in range(0, team_num):
        print ("Team " + str(i) + ". " + str(teams[i]))
    
print ("===== Before Initial Team Status =====")
print (teams)

# constructing & initializing team
for i in range(0, team_num):
    teams.append([])
    teams[i].append(students[0])
    students.remove(students[0])

show_team(teams, round_count)    
round_count += 1

# print ("===== Looping Through Each Students =====")

while students != []:
    update_student = 0
    update_team = 0
    update_member = 0
    
    # iterates newly-built team
    for team in teams:
        team_var = 0
        max_var = 0
        # iterates all students left
        for student in students:
            # iterates each members inside the team
            for member in team:
                indiv_var = 0
                
                # get the team var based on features
                for f in feat_param:
                    team_var += np.var([student[f], member[f]])
            
            team_var /= len(teams)
            team_var /= feat_num
            
            if max_var < team_var:
                max_var = team_var
                update_student = student
                update_team = team
                update_member = member

        teams[team_count % team_num].append(update_student)
        students.remove(update_student)
        show_team(teams, round_count)    
        team_count += 1
        round_count += 1


