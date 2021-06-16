
from copy import copy, deepcopy


# initialization
def init():

    list = [2, 1, 5, 0, 8, 4, 10, 0, 20, 10]
    return list


# calculating cost
def calc_cost(state):

    state1 = deepcopy(state)
    state_len = len(state1)
    num = 0
    i = 0

    while i < state_len:
        j = i + 1

        while j < state_len:

            if state1[j] < state1[i]:
                num = num + 1

            j = j + 1

        i = i + 1

    return num


# stat generation
def state_generation(current_state, current_state_cost):

    c_state = []
    list_main = []
    arr = []
    len1 = len(current_state)
    i = 0

    while i < len1:

        c_state = deepcopy(current_state)
        j = i + 1

        while j < len1:

            c_state[i], c_state[j] = c_state[j], c_state[i]
            new_cost = calc_cost(c_state)
            arr.append(new_cost)
            list_main.append(c_state)
            c_state = deepcopy(current_state)
            j = j + 1

        i = i + 1

    main_cost = min(arr)
    x = arr.index(main_cost)
    main_state = list_main[x]

    if main_cost < current_state_cost:
        return main_state, main_cost

    else:
        return current_state, None


# goal test
def goal_test(state1):

    if calc_cost(state1) == 0:
        return True

    else:
        return False


# main
state = init()
cost = calc_cost(state)

while not goal_test(state):

    state, cost = state_generation(state, cost)

    if cost is None:
        break

print("Steepest_Hill climbing:", state)
