import random
#https://www.reddit.com/r/dailyprogrammer/comments/8s0cy1/20180618_challenge_364_easy_create_a_dice_roller/
challengeInput = ['5d12', '6d4', '1d2', '1d8', '3d6', '4d20', '100d100']
result =[]
def rollDie(number, counter):
    action =  random.randint(1,number)
    #print(str(counter+1)+': ', action)
    return action
def rollDieMulti(noRolls, number):
    for x in range(noRolls):
       t = rollDie(number, x)
       result.append(t)
for x in range(len(challengeInput)):
    #print(challengeInput[x])
    command = challengeInput[x]
    dataN = command.split('d')
    for y in range(len(dataN)):
        noRolls = int(dataN[0])
        numberFaces = int(dataN[1]) 
    rollDieMulti(noRolls,numberFaces)
    total = sum(result)
    print(str(total)+":" ,result)


      






