class Jumper:
    def __init__(self):
        
        self.line0 = ("")
        self.line1 = ("  ___")
        self.line2 = (" /___\ ")
        self.line3 = (" \   /")
        self.line4 = ("  \ /")
        self.line5 = ("   0")
        self.line6 = ("  /|\ ")
        self.line7 = ("  / \ ")
        self.line8 = ("")
        self.line9 = ("^^^^^^^" )
        self.is_playing = True

    

    def display_parachute(self, number_of_mistakes):

        lines = [self.line0,self.line1,self.line2,self.line3,self.line4,self.line5,self.line6,self.line7,self.line8,self.line9]
      
        for line in lines:
            index = lines.index(line)
            if index < (number_of_mistakes+1):
                line = ""
            print(line)
        if number_of_mistakes >= 4:
            print("Game over\n")
            self.is_playing = False

jumper = Jumper()
jumper.display_parachute(4)

        "2": parachute2,
        "3": parachute3,
        "4": parachute4,
    }

    print(dictParachute[n])
    
