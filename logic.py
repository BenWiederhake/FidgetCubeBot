#!/bin/false
# Not for execution


def default_state():
    return dict(per_user=dict(), per_group=dict())


def compute_plopp(state, argument, sender_id, sender_username, sender_firstname):
    return False, ('plopp', sender_firstname)


def compute_roll(state, argument, sender_id, sender_username, sender_firstname):
    return False, ('roll', sender_firstname)


def handle(state, command, argument, sender_id, sender_username, sender_firstname):
    if command == 'roll':
        return compute_roll(state, argument, sender_id, sender_username, sender_firstname)
    elif command == 'plopp':
        return compute_plopp(state, argument, sender_id, sender_username, sender_firstname)
    else:
        return False, ('unknown_command', sender_firstname)
