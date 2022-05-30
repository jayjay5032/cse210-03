class Compare:
    def good_or_bad_guess(index, the_answer, remain_lifes, user_input):
        '''
        Responsibility: compare the user input with the answer. If correct, return user input and set life_lost Boolean to FALSE, vice versa. Guess wrong also result in lost 1 life.
        '''
        for character in the_answer:
            if character == user_input:
                return remain_lifes
        return remain_lifes - 1