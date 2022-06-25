#!/bin/false
# Not for execution


def unfuck_state(state):
    old_per_user = state['per_user']
    # JSON doesn't allow numbers as keys, so we have to convert them manually back:
    new_per_user = {int(k): v for k, v in old_per_user.items()}
    state['per_user'] = new_per_user
    return state


def default_state():
    return dict(per_user=dict(), highest_count=dict(number=0, by_first='???', by_id=0), plopps=0)


def default_user_dict():
    return dict(counts=0)


def compute_plopp(state, argument, sender_id, sender_username, sender_firstname):
    state['plopps'] += 1
    return True, ('plopp', sender_firstname, state['plopps'])


def compute_roll(state, argument, sender_id, sender_username, sender_firstname):
    return False, ('roll', sender_firstname)


def compute_count(state, argument, sender_id, sender_username, sender_firstname):
    per_user = state['per_user']
    if sender_id not in per_user:
        per_user[sender_id] = default_user_dict()
    user_dict = per_user[sender_id]

    user_dict['counts'] += 1
    highscore = state['highest_count']
    overtaken = False
    old_best_firstname = highscore['by_first']
    if user_dict['counts'] > highscore['number']:
        highscore['number'] = user_dict['counts']
        highscore['by_first'] = sender_firstname
        highscore['by_id'] = sender_id
        overtaken = True

    if user_dict['counts'] == 1:
        return True, ('count_first', sender_firstname)
    if user_dict['counts'] < 10:
        if overtaken:
            if highscore['by_first'] != old_best_firstname:
                return True, ('count_subten_overtaken', sender_firstname, user_dict['counts'], old_best_firstname)
            else:
                return True, ('count_subten_better', sender_firstname, user_dict['counts'])
        else:
            return True, ('count_subten', sender_firstname, user_dict['counts'])
    if overtaken:
        if highscore['by_first'] != old_best_firstname:
            return True, ('count_high_overtaken', sender_firstname, user_dict['counts'], old_best_firstname)
        else:
            return True, ('count_high_better', sender_firstname, user_dict['counts'])
    else:
        if user_dict['counts'] == highscore['number']:
            return True, ('count_high_equal', sender_firstname, user_dict['counts'], old_best_firstname)
        else:
            return True, ('count_high', sender_firstname, user_dict['counts'], old_best_firstname, highscore['number'])


def compute_bin_ich_toll(state, argument, sender_id, sender_username, sender_firstname):
    return False, ('sehr_toll', sender_firstname, sender_username)


def handle(state, command, argument, sender_id, sender_username, sender_firstname):
    if command == 'roll':
        return compute_roll(state, argument, sender_id, sender_username, sender_firstname)
    elif command == 'plopp':
        return compute_plopp(state, argument, sender_id, sender_username, sender_firstname)
    elif command == 'count':
        return compute_count(state, argument, sender_id, sender_username, sender_firstname)
    elif command == 'bin_ich_toll':
        return compute_bin_ich_toll(state, argument, sender_id, sender_username, sender_firstname)
    else:
        return False, ('unknown_command', sender_firstname)
