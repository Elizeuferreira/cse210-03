""" The game package contains specific classes for playing jumper.
"""

class Director:
    
    #Elizeu Silva
    #Shawn yang
    pass

class Jumper:
    #Brenner

    #Code that Will Construct the Jumper.
    def init_jumper():
        global head,arms,legs
        head=("   O")
        arms=("  /|\ ")
        legs=("  / \ ")
        print(head)
        print(arms)
        print(legs)
    
    #Code that will first check
    def fail_check():
        lives=-1
        if  lives >=0:
            return True
        else:
            head=("   X")
            print(head)
            print(arms)
            print(legs)
            print()
            print("Game Over!")
            return False

class parachute:
    
    #Alexander
    
    pass

class word:
    lives=-1
    #Josefini
    
    pass
    
Jumper.init_jumper()
Jumper.fail_check()
