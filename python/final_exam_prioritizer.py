print("Final Exam Prioritizer")

def calc_goal(target_grade, current_grade, final_pct):
    # target_grade = current_grade * (100%-final_pct) + goal * final_pct
    # then, solve for "goal"
    goal = (target_grade - current_grade * (1-final_pct)) / final_pct
    #print(goal)
    if goal <= 0:
        return "nothing"
    elif goal > 100:
        return "a miracle"
    else:
        return "to score " + str(int(goal))

again = True
while again:
    print("What is your current score? (0-100)")
    current_score = float(input())

    print("What percentage of your grade is the final?")
    final = float(input())/100

    print()
    print("To get an A, you need", calc_goal(90, current_score, final))
    print("To get an B, you need", calc_goal(80, current_score, final))
    print("To get an C, you need", calc_goal(70, current_score, final))
    print()
    
    print("Do another? y/n")
    again = (input() == 'y')
