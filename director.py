from puzzle import Puzzle
from terminal import Terminal
from compare import Compare
from display import Display

class Director:
    def __init__(self):
        self.puzzle = Puzzle()
        self.is_playing = True
        self.terminal = Terminal()
        self.user_input = str
        self.compare = Compare()
        self.remain_lifes = 4
        self.display = Display()
        self.cAns = []
        self.message_to_display = []
        
    def start_game(self):
        self.puzzle.generate_answer()
        while self.is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        self.user_input = input("\nGuess a letter [a-z]: ")
        self.terminal.get_user_input(self.user_input)
    def _do_updates(self):
        self.remain_lifes = self.compare.good_or_bad_guess(self.puzzle.get_answer(), self.remain_lifes, self.user_input)
        
        
    def _do_outputs(self):

        self.message_to_display, self.cAns = self.display.content_to_display(self.cAns,self.puzzle.get_answer(), self.user_input, self.remain_lifes)
        
        for i in self.message_to_display:
            self.terminal.print_to_screen(i)
            
        if self.remain_lifes == 0:
            print("Game over!")
            self.is_playing = False
