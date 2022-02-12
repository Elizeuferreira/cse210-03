<<<<<<< HEAD
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
=======

>>>>>>> 2d957382239fbc9f5f51c5b8eb2dbc56efb7ada5
