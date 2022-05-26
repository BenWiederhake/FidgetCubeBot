#!/usr/bin/env false

import secret

MESSAGES = {
    'roll': [  # {0} is sender_firstname
        'Eine 4.',
        'Du hast eine 4 gewürfelt, {0}.',
        'Es wurde eine 4.',
        '4 Augen, {0}.',
        'Es sind 4 Augen, {0}.',
        '{0}, es ist eine 4.',
        '{0}, du wirst es kaum glauben: Es ist eine 4!',
        'OMG, wie machst du das?! Es ist eine 4!',
    ],
    'unknown_command': [  # {0} is sender_firstname
        'Häh?',
        'Bittewas, {0}?',
        'Bestimmt weiß ich eines Tages, was das bedeuten soll, {0}.',
        'Ich habe nicht genügend Erfahrung, um diese Aufgabe auszuführen.',
    ],
}
