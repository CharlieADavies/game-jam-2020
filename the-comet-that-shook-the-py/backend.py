import random


def get_r1_attrs(count=3):
    directory_list = []

    # query directory for r1*.png into directory_list
    r1_attrs = random.sample(directory_list, count)
    return r1_attrs


def get_r2_attrs(count=3):
    directory_list = []

    # query directory for r2*.png into directory_list
    r2_attrs = random.sample(directory_list, count)
    return r2_attrs


def get_r3_attrs(count=3):
    directory_list = []

    # query directory for r3*.png into directory_list

    r3_attrs = random.sample(directory_list, count)
    return r3_attrs


def get_new_game():
    solution_list = get_r1_attrs() + get_r2_attrs() + get_r3_attrs()
    return solution_list


X = {'a1': 'Tom', 'a2': 'Dick', 'a3': 'Harry',
     'f1': 'Grapes', 'f2': 'Cherries', 'f3': 'Blueberries',
     'c1': 'Red', 'c2': 'White', 'c3': 'Blue'}

Y = ["{a1:} live next to the person who likes {f1:}",
     "The person in the {c2:} house likes {f2:}",
     "The person who likes {f1:} lives in the {c1:} house",
     "The person who likes {a3:} doesn't live next to the person who likes {f2:}",
     "{a2:}'s house is {c2:}",
     "{a1:} lives to the left of the {c2:} house."]

def get_puzzle_clues(solution_list, fact_templates):
    return [fact.format(**solution_list) for fact in fact_templates]

def get_fact_template():
    # need some storage for these and choose one group at random
    # instead of a list of 9 Nones :)
    template_list = [None] * 9
    return template_list


def check_results(result, solution_list):
    return result == solution_list


def start_new_game():
    solution_list = get_new_game()
    shuffled_list = solution_list[:]
    random.shuffle(shuffled_list)
    fact_templates = get_fact_template()
    clue_list = get_puzzle_clues(solution_list, fact_templates)
    # real return value
    # return solution_list, shuffled_list, clue_list

    # bogus test code follows:
    solution_list = ['Tom', 'Dick', 'Harry', 'Grapes', 'Cherries', 'Blueberries', 'Red', 'White', 'Blue']
    clue_list = ["Tom live next to the person who likes cherries",
                 "The person in the blue house likes blueberries",
                 "The person who likes cherries lives in the white house",
                 "The person who likes grapes doesn't live next to the person who likes bluberries",
                 "Harry's house is blue"]
    shuffled_list = solution_list[:]
    random.shuffle(shuffled_list)

    return solution_list, shuffled_list, clue_list
