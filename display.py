class Display:

    def __init__(self):
        self.Guess_result_in_list = []
        self.Life_pic_in_list = ["___", "/___\\", "\\   /", "\\ /"]
        self.character_list = []
        self.message_to_display = []
        self.answer_display = ""

    def content_to_display(self, cAns, the_answer, user_input, remaining_lives):
        '''
        Responsibility: determined the content to display on the screen
        '''

        cLives = remaining_lives
        uInput = user_input
        cAns = list(the_answer).copy()

        for i in cAns:
            self.answer_display += "_ "

        if uInput in the_answer:
            
            for i, elm in enumerate(cAns):
                if(elm == uInput):
                    self.answer_display.replace(i, f"{uInput} ")


        self.message_to_display.append("")

        if (cLives < 4):
            for i in self.Life_pic_in_list[4 - cLives:]:
                self.message_to_display.append(i)
        else:
            for i in range(4):
                self.message_to_display.append(self.Life_pic_in_list[i])

        if (cLives == 0):
            self.character_list = ["  x", " /|\\", " / \\"]     
        else:
            self.character_list = ["  o", " /|\\", " / \\"]  

        for i in self.character_list:
            self.message_to_display.append(i)

        self.message_to_display.append("^^^^^^")

        return self.message_to_display, cAns