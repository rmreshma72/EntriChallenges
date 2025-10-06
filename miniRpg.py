# Mini RPG Battle Simulator
import random
player=input("\nEnter your name:").upper()
e=['GOBLIN👺','ORC👾','SKELETON💀','GHOST👻']
enemy=random.choice(e)
print(f"\nHai {player}🦸. Your enemy is {enemy}\n\n")
turn = 1
playerhp=100
enemyhp=100
p=['ATTACK','DEFEND','HEAL']
while (playerhp >=0 and enemyhp>=0):
    print("\n\nTURN",turn)
    print(f"⚔....{enemy} ATTACK....⚔")

    playerch=random.choice(p) #Selecting player's strategy

    if(playerch=='ATTACK'): #Enemy and Player attacking each other
        print(f"⚔....{player}🦸 ATTACK....⚔")
        enemyhp-=random.randint(10,30)
        playerhp-=random.randint(10,35)
        print(f"{player}🦸 Health:", playerhp)
        print(f"{enemy} Health:", enemyhp)
        
    elif(playerch=='DEFEND'): #Enemy attacking. Player defending
        print(f"🗡....{player}🦸 DEFEND....🗡")
        playerhp-=random.randint(10,35)//2
        print(f"{player}🦸 Health:", playerhp)
        print(f"{enemy} Health:", enemyhp)

    elif(playerch=='HEAL'): #Enemy attacking. Player Healing
        playerhp-=random.randint(10,35)
        print(f"{player}🦸 Health:", playerhp)
        print(F"😌....{player} HEALING....😌")
        playerheal=random.randint(10,25)
        if(playerhp+playerheal<100):
            playerhp+=playerheal
        print(f"{player}🦸 Health:", playerhp)
        print(f"{enemy} Health:", enemyhp)
    turn+=1



if (playerhp>enemyhp):
    print(f"\n\nGAME OVER...\n{player}🦸 WINS   😄.....!!!!!!!")
else:
    print(f"\n\nGAME OVER....\n{enemy} WINS 🙁....")


    
