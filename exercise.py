print('please enter your percent score')

def accepts_percentage(percentage):
    if int(percentage) >= 97:
        print('you got A+')
    elif 97 > int(percentage) >93:
        print('you got an A')
    elif 93 > int(percentage) >90:
        print('you got an A-')
    elif 90 > int(percentage) >85:
        print('you got a B+')
    elif 85 > int(percentage) >80:
        print('you got a B')
    elif 80 > int(percentage) >75:
        print('you got a B-')
    elif 75 > int(percentage) >70:
        print('you got a C+')
    elif 70 > int(percentage) >65:
        print('you got a C')
    elif 65> int(percentage) >60:
        print('you got a C-')
    elif 60 > int(percentage) >55:
        print('you got a D+')
    elif 55 > int(percentage) >53:
        print('you got a D')
    elif 53 > int(percentage) >50:
        print('you got a D-')
    else:
        print('sorry you failed')
accepts_percentage(input())



