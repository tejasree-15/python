import random
def choose():
    words=["rainbow","computer","mathematics","statistics","calculation","childhood","responsible","communication","engineering","electronics","history","python","programming","specialisation"]
    pick=random.choice(words)
    return pick
def jumble(words):
    jumbled="".join(random.sample(words,len(words)))
    return jumbled
def thank(p1name,p2name,pp1,pp2):
    print(p1name,"your score is :",pp1)
    print(p2name,"your score is :",pp2)
    print("thankyou for playingg:)")
    print("have a nice day ._.")
def play():
    p1name=input("player1.. please enter your name: ")
    p2name=input("player2.. please enter your name: ")
    pp1=0
    pp2=0
    turn=0
    while(1):
        #computers task
        picked_word=choose()
        #create question
        qn=jumble(picked_word)
        print(qn)
        #player1
        if turn%2==0:
            print(p1name,"its your turn..")
            ans=input("what is on my mind?  : ")
            if ans==picked_word:
                print("you are right!!")
                pp1=pp1+1 
                print("your score is: ",pp1)
            else:
                print("better luck next time. I though ",picked_word)
            c=int(input("click 1 to continue or click 0 to quit : "))
            if c==0:
                thank(p1name,p2name,pp1,pp2)
                break
        else:
            print(p2name,"its your turn..")
            ans=input("what is on my mind?  : ")
            if ans==picked_word:
                print("you are right!!")
                pp2=pp2+1 
                print("your score is: ",pp2)
            else:
                print("better luck next time. I though ",picked_word)
            c=int(input("click 1 to continue or click 0 to quit : "))
            if c==0:
                thank(p1name,p2name,pp1,pp2)
                break
        turn=turn+1
play()