import random
username=input("Enter Username : ")
print('Welcome {} to the game.'.format(username.title()))
att_l=[]
def score():
    if len(att_l)<=0:
        print('No High score found')
    else:
        print("Your high score is {}".format(min(att_l)))

first=int(input("Enter first num : "))
last=int(input("Enter last num : "))
print('Random Number is b/w the range given by You')
random_num=random.randint(first, last)
#print ('Your Num is :',random_num)
attempt=0
score()
while True:
    num=int(input("Guess the number : "))
    if num==random_num:
        print('* Found It *')
        attempt+=1
        att_l.append(attempt)
        print('It took {} attemps'.format(attempt))
        res=input("Want to play Again ? (Yes/No) : ")
        if res.lower()=='no':
            print('Thank You For Playing')
            score()
            break
        else:
            attempt=0
            random_num = random.randint(first, last)
#            print('New Number is :',random_num)

    elif num<random_num:
        print(' Guess higher ')
        attempt += 1
    elif num>random_num:
        print(' Guess lower ')
        attempt += 1

