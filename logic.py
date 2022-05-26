#!/bin/false
# Not for execution


def default_state():
    return dict(per_user=dict(), per_group=dict())


def handle(state, command, argument, sender_id, sender_username, sender_firstname):
    if False:
        pass
    else:
        return False, ('unknown_command', sender_firstname)
