
Object: Puzzle

Responsibility: generate the puzzle from the list

State:
list_of_words
the_answer

Behaviors: 
generate answer
get answer

class: puzzle

list_of_words: string
the_answer: string

generate _answer(): none
get_answer(): string




Object: Terminal

Responsibility: take inputs from the user and print output to the screen

State:
user input

behavior:
get user input
print to screen

class: terminal

user_input: string

get_user_input(): string
print_to_screen(): none




Object: Compare

Responsibility: compare the user input with the answer. If correct, return user input and set life_lost Boolean to FALSE, vice versa. Guess wrong also result in lost 1 life.

State:
Life lost
Remain lifes

Behavior:
Good or bad guess

class: compare

Life_lost: bool
Remain_Lifes: int

good_or_bad_guess(): bool, string, int




Object: is ended

Responsibility: determined if the game is ended: the user guessed the word or loses all the life

Behavior:
Is ended

class: is_ended

is_ended(): bool




Object: display

Responsibility: determined the content to display on the screen

State:
Guess result in list
Life pic in list
Message to display

Behavior:
Content to display

class:display

Guess_result_in_list: list
Life_pic_in_list: list
Message_to_display: string

Content_to_display: list, string


