class Parachute:
    """Where we create and change the tries of the parachute
    
    """
    def __init__(self):
        """Constructs the parachute"""

        self._parachutes = 0
        self._parachute = 0

    def show_parachute(self, tries):
        """
        Method to show condition of parachute accordingly to the number of left attempts
        
        Args:
        self: an instance of Parachute
        tries: number of attempts left
        """
        
        stages = [  # final state: No parachute left 
            """
             x 
            /|\ 
            / \ 
       ^^^^^^^^^^^^^
            """,
            # Small strings (1 attempt left)
            """
            \ /
             O
            /|\ 
            / \ 
       ^^^^^^^^^^^^^
            """,
            # Medium strings (2 attempts left)
            """
           \   /
            \ /
             O
            /|\ 
            / \ 
       ^^^^^^^^^^^^^
            """,
            # Long strings (3 attempts left)
            """
          \     /
           \   /
            \ /
             O
            /|\ 
            / \ 
       ^^^^^^^^^^^^^
            """,
            # middle of chute (4 attempts left)
            """
          /_____\ 
          \     /
           \   /
            \ /
             O
            /|\ 
            / \ 
       ^^^^^^^^^^^^^
            """,
            # Initial state (5 attempts)
            """
           _____
          /_____\ 
          \     /
           \   /
            \ /
             O
            /|\ 
            / \ 
       ^^^^^^^^^^^^^
            """,
            ]
        return print(stages[tries])
    
