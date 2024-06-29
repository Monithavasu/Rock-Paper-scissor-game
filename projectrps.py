import random
def rps(computer,mine):
    if(computer==mine):
        return None
    if(computer=='rock' and mine=='paper'):
        return True
    elif(computer=='paper' and mine=='scissor'):
        return True
    elif(computer=='scissor' and mine=='rock'):
        return True
    else:
        return False
    
choice=['rock','paper','scissor']
computer=random.randint(0,2)
computer=choice[computer]
mine=input('enter your choice either rock,paper or scissor:')

win=rps(computer,mine)
print(f"you choose {mine} and computer choose {computer}")
if win is None:
    print('match drawn')
if win :
    print('you won')
else:
    print('you lose')

