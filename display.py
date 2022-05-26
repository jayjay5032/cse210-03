import re
from shutil import register_unpack_format


class Display:
    def __init__(self):
        self.Guess_result_in_list = []
        self.Life_pic_in_list = []
        self.message_to_display = str
    def content_to_display(self, the_answer, user_input):
        '''
        Responsibility: determined the content to display on the screen
        '''

        return self.message_to_display