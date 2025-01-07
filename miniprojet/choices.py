import random

class Choice():
    def __init__(self, possible_choices: list, valid_choice):
        self.possible_choices = possible_choices
        self.valid_choice = valid_choice
        index_match = {"a": 0, "b": 1, "c": 2}
        valid_index = index_match[self.valid_choice]
        valid_str = possible_choices[valid_index]
        random.shuffle(possible_choices)
        for i in range(len(possible_choices)):
            if possible_choices[i] == valid_str:
                self.valid_choice = chr(97 + (i))

        print(f"debug: generated choices={possible_choices}")
        print(f"debug: expected valid_choice={valid_choice} \n")





