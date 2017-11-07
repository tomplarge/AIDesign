import random
import numpy as np

team_num = 3
feat_num = 2
round_count = 1
team_count = 0
# students = [{'feat_1':.15842}, {'feat_1':.28832}, {'feat_1':.35483}, {'feat_1':.44372}, {'feat_1':.55693},
#                                 {'feat_1':.65632}, {'feat_1':.77154}, {'feat_1':.84038}, {'feat_1':.91327}]

students = [{'feat_1':.15842, 'feat_2':.11582}, {'feat_1':.28832, 'feat_2':.22845}, {'feat_1':.35483, 'feat_2':.33574},
            {'feat_1':.42372, 'feat_2':.44683}, {'feat_1':.55693, 'feat_2':.55293}, {'feat_1':.65632, 'feat_2':.66492},
            {'feat_1':.73154, 'feat_2':.77482}, {'feat_1':.84038, 'feat_2':.88102}, {'feat_1':.91327, 'feat_2':.99230}]
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
    max_var = 0
    update_student = 0
    update_team = 0
    update_member = 0
    
    # iterates all students left
    for student in students:
        # iterates newly-built team
        for team in teams:
            team_var = 0
            # iterates each members inside the team
            for member in team:
                indiv_var = 0
                
#                 for feat in range(0, feat_num):
#                     print (feat)
#                     value = next(v for i, v in enumerate(student.items()) if i == feat )
#                     print (value)
                    
                    
#                 for k, v in student.items():
#                     print (k, v)
                # iterates each features inside the individual
#                 for k, v in student.items():
#                     print (k, v)
#                     val1 = next( v for i, v in enumerate(student.items()) if i == 0 )
#                     val2 = [k for (k, v) in student.items() if v == 0]
#                     print (val1, val2)
#                     print (member.values())
#                     indiv_var += np.var([student['']])
                    
                team_var += np.var([student['feat_1'], member['feat_1']]) + np.var([student['feat_2'], member['feat_2']])
                
            if max_var < team_var:
                max_var = team_var
                update_student = student
                update_team = team
                update_member = member
#                     print (np.var([student['feat_1'], member['feat_1']]))
#                     print (update_student, ",", update_team, ",", update_member)

#     print (teams)
#     print (students)
#     print (update_student)
#     print (update_team)
#     print (update_member)
#     print (max_var)
#     print ("update")
    teams[team_count % team_num].append(update_student)
    students.remove(update_student)
    show_team(teams, round_count)    
    team_count += 1
    round_count += 1

#     print (teams)
#     print (students)
#     break


