#!/usr/bin/env python3
# Run as: ./tests.py

import bot  # check whether the file parses
import logic
import msg  # check keyset
import unittest


class TestSequences(unittest.TestCase):
    def check_sequence(self, sequence):
        state = logic.default_state()
        for i, (query, expected_save, expected_response) in enumerate(sequence):
            with self.subTest(step=i):
                actual_save, actual_response = logic.handle(state, *query)
                # command, argument, sender_id, sender_username, sender_firstname
                self.assertEqual(expected_save, actual_save)
                self.assertEqual(expected_response, actual_response)
                self.assertIn(expected_response[0], msg.MESSAGES.keys())
                if expected_response == actual_response and expected_response[0] in msg.MESSAGES.keys():
                    template_list = msg.MESSAGES[expected_response[0]]
                    self.assertTrue(template_list)
                    # Check that all templates all work:
                    for template in template_list:
                        self.assertTrue(template.format(*expected_response[1:]))

    def test_empty(self):
        self.check_sequence([])

    def test_start(self):
        self.check_sequence([
            (('start', '', 123, 'usna', 'fina'), False, ('unknown_command', 'fina')),
        ])

    def test_roll(self):
        self.check_sequence([
            (('roll', '', 123, 'usna', 'fina'), False, ('roll', 'fina')),
        ])

    def test_plopp(self):
        self.check_sequence([
            (('plopp', '', 123, 'usna', 'fina'), False, ('plopp', 'fina')),
        ])


if __name__ == '__main__':
    unittest.main()
