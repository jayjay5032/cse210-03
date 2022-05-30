class Display:

    def __init__(self):
        self.Guess_result_in_list = []
        self.Life_pic_in_list = [" ___", "/___\\", "\\   /", " \\ /"]
        self.character_list = []
        self.message_to_display = []
        self.answer_display = []

    def content_to_display(self, cAns, the_answer, user_input, remaining_lives):
        '''
        Responsibility: determined the content to display on the screen
        '''
        self.message_to_display = []
        self.answer_display = cAns
        cLives = remaining_lives
        uInput = user_input
        str_answer_display = ""
        

        if uInput in the_answer:
            for i in range(len(the_answer)):
                if(the_answer[i] == uInput):
                    self.answer_display[i] = uInput
        
        for char in self.answer_display:
            str_answer_display += char
    
        self.message_to_display.append(str_answer_display)
        self.message_to_display.append("\n")

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

        return self.message_to_display, self.answer_display