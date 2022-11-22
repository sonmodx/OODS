def findTotalScore(team) :
    total = int(team[1])*3 + int(team[3])
    return total

def findDiffGoal(team) :
    return int(team[4]) - int(team[5])

def specialSort(teams) :
    for i in range(0,len(teams)) :
        for j in range(0,len(teams)-i-1) :
            totalScoreOfFirstTeam = findTotalScore(teams[j])
            totalScoreOfSecondTeam = findTotalScore(teams[j+1])
            if totalScoreOfFirstTeam < totalScoreOfSecondTeam :
                teams[j],teams[j+1] = teams[j+1],teams[j]
            if totalScoreOfFirstTeam == totalScoreOfSecondTeam :
                if findDiffGoal(teams[j]) < findDiffGoal(teams[j+1]) :
                    teams[j],teams[j+1] = teams[j+1],teams[j]

if __name__ =='__main__' :
    inp = input("Enter Input : ").split('/')
    teams  = []
    for item in inp :
        teams.append(item.split(','))
    specialSort(teams)
    print("== results ==")
    for team in teams :
        print(f"['{team[0]}'," +" {" + f"'points': {findTotalScore(team)}" + "}, " + "{" + f"'gd': {findDiffGoal(team)}" + "}" + "]")