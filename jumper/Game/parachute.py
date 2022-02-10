def showParachute(n):

    parachute0 = "\
      ___ \n \
    /___\ \n \
    \   / \n \
     \ / \n \
      0 \n \
     /|\  \n \
     / \ \n "

    parachute1 = "\
     /___\ \n \
    \   / \n \
     \ / \n \
      0 \n \
     /|\  \n \
     / \ \n "
    
    parachute2 = "\
     \   / \n \
     \ / \n \
      0 \n \
     /|\  \n \
     / \ \n "

    parachute3 = "\
      \ / \n \
      0 \n \
     /|\  \n \
     / \ \n "

    parachute4 = "\
       x \n \
     /|\  \n \
     / \ \n "

    dictParachute = {
        "0" : parachute0,
        "1": parachute1,
        "2": parachute2,
        "3": parachute3,
        "4": parachute4,
    }

    print(dictParachute[n])
    
