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
            (('plopp', '', 123, 'usna', 'fina'), True, ('plopp', 'fina', 1)),
        ])

    def test_plopp_many(self):
        self.check_sequence([
            (('plopp', '', 123, 'usna', 'fina'), True, ('plopp', 'fina', 1)),
            (('plopp', '', 123, 'usna', 'fina'), True, ('plopp', 'fina', 2)),
            (('plopp', '', 123, 'usna', 'fina'), True, ('plopp', 'fina', 3)),
            (('plopp', '', 123, 'usna', 'fina'), True, ('plopp', 'fina', 4)),
            (('plopp', '', 123, 'usna', 'fina'), True, ('plopp', 'fina', 5)),
            (('plopp', '', 123, 'usna', 'fina'), True, ('plopp', 'fina', 6)),
            (('plopp', '', 123, 'usna', 'fina'), True, ('plopp', 'fina', 7)),
            (('plopp', '', 456, 'usnb', 'finb'), True, ('plopp', 'finb', 8)),
        ])

    def test_count_latejoin(self):
        self.check_sequence([
            (('count', '', 123, 'usna', 'fina'), True, ('count_first', 'fina')),
            (('count', '', 123, 'usna', 'fina'), True, ('count_subten_better', 'fina', 2)),
            (('count', '', 123, 'usna', 'fina'), True, ('count_subten_better', 'fina', 3)),
            (('count', '', 123, 'usna', 'fina'), True, ('count_subten_better', 'fina', 4)),
            (('count', '', 123, 'usna', 'fina'), True, ('count_subten_better', 'fina', 5)),
            (('count', '', 123, 'usna', 'fina'), True, ('count_subten_better', 'fina', 6)),
            (('count', '', 123, 'usna', 'fina'), True, ('count_subten_better', 'fina', 7)),
            (('count', '', 123, 'usna', 'fina'), True, ('count_subten_better', 'fina', 8)),
            (('count', '', 123, 'usna', 'fina'), True, ('count_subten_better', 'fina', 9)),
            (('count', '', 123, 'usna', 'fina'), True, ('count_high_better', 'fina', 10)),
            (('count', '', 123, 'usna', 'fina'), True, ('count_high_better', 'fina', 11)),
            (('count', '', 123, 'usna', 'fina'), True, ('count_high_better', 'fina', 12)),
            (('count', '', 123, 'usna', 'fina'), True, ('count_high_better', 'fina', 13)),
            (('count', '', 123, 'usna', 'fina'), True, ('count_high_better', 'fina', 14)),
            (('count', '', 123, 'usna', 'fina'), True, ('count_high_better', 'fina', 15)),
            (('count', '', 123, 'usna', 'fina'), True, ('count_high_better', 'fina', 16)),
            (('count', '', 123, 'usna', 'fina'), True, ('count_high_better', 'fina', 17)),
            (('count', '', 123, 'usna', 'fina'), True, ('count_high_better', 'fina', 18)),
            (('count', '', 456, 'usnb', 'finb'), True, ('count_first', 'finb')),
            (('count', '', 456, 'usnb', 'finb'), True, ('count_subten', 'finb', 2)),
            (('count', '', 456, 'usnb', 'finb'), True, ('count_subten', 'finb', 3)),
            (('count', '', 456, 'usnb', 'finb'), True, ('count_subten', 'finb', 4)),
            (('count', '', 456, 'usnb', 'finb'), True, ('count_subten', 'finb', 5)),
            (('count', '', 456, 'usnb', 'finb'), True, ('count_subten', 'finb', 6)),
            (('count', '', 456, 'usnb', 'finb'), True, ('count_subten', 'finb', 7)),
            (('count', '', 456, 'usnb', 'finb'), True, ('count_subten', 'finb', 8)),
            (('count', '', 456, 'usnb', 'finb'), True, ('count_subten', 'finb', 9)),
            (('count', '', 456, 'usnb', 'finb'), True, ('count_high', 'finb', 10, 'fina', 18)),
            (('count', '', 456, 'usnb', 'finb'), True, ('count_high', 'finb', 11, 'fina', 18)),
            (('count', '', 456, 'usnb', 'finb'), True, ('count_high', 'finb', 12, 'fina', 18)),
            (('count', '', 456, 'usnb', 'finb'), True, ('count_high', 'finb', 13, 'fina', 18)),
            (('count', '', 456, 'usnb', 'finb'), True, ('count_high', 'finb', 14, 'fina', 18)),
            (('count', '', 456, 'usnb', 'finb'), True, ('count_high', 'finb', 15, 'fina', 18)),
            (('count', '', 456, 'usnb', 'finb'), True, ('count_high', 'finb', 16, 'fina', 18)),
        ])

    def test_count_overtaking(self):
        self.check_sequence([
            (('count', '', 123, '', 'fina'), True, ('count_first', 'fina')),
            (('count', '', 456, '', 'finb'), True, ('count_first', 'finb')),
            (('count', '', 456, '', 'finb'), True, ('count_subten_overtaken', 'finb', 2, 'fina')),
            (('count', '', 456, '', 'finb'), True, ('count_subten_better', 'finb', 3)),
            (('count', '', 123, '', 'fina'), True, ('count_subten', 'fina', 2)),
            (('count', '', 123, '', 'fina'), True, ('count_subten', 'fina', 3)),
            (('count', '', 123, '', 'fina'), True, ('count_subten_overtaken', 'fina', 4, 'finb')),
            (('count', '', 123, '', 'fina'), True, ('count_subten_better', 'fina', 5)),
            (('count', '', 456, '', 'finb'), True, ('count_subten', 'finb', 4)),
            (('count', '', 456, '', 'finb'), True, ('count_subten', 'finb', 5)),
            (('count', '', 456, '', 'finb'), True, ('count_subten_overtaken', 'finb', 6, 'fina')),
            (('count', '', 456, '', 'finb'), True, ('count_subten_better', 'finb', 7)),
            (('count', '', 123, '', 'fina'), True, ('count_subten', 'fina', 6)),
            (('count', '', 123, '', 'fina'), True, ('count_subten', 'fina', 7)),
            (('count', '', 123, '', 'fina'), True, ('count_subten_overtaken', 'fina', 8, 'finb')),
            (('count', '', 123, '', 'fina'), True, ('count_subten_better', 'fina', 9)),
            (('count', '', 456, '', 'finb'), True, ('count_subten', 'finb', 8)),
            (('count', '', 456, '', 'finb'), True, ('count_subten', 'finb', 9)),
            (('count', '', 456, '', 'finb'), True, ('count_high_overtaken', 'finb', 10, 'fina')),
            (('count', '', 456, '', 'finb'), True, ('count_high_better', 'finb', 11)),
            (('count', '', 123, '', 'fina'), True, ('count_high', 'fina', 10, 'finb', 11)),
            (('count', '', 123, '', 'fina'), True, ('count_high_equal', 'fina', 11, 'finb')),
            (('count', '', 123, '', 'fina'), True, ('count_high_overtaken', 'fina', 12, 'finb')),
            (('count', '', 123, '', 'fina'), True, ('count_high_better', 'fina', 13)),
            (('count', '', 456, '', 'finb'), True, ('count_high', 'finb', 12, 'fina', 13)),
            (('count', '', 456, '', 'finb'), True, ('count_high_equal', 'finb', 13, 'fina')),
            (('count', '', 456, '', 'finb'), True, ('count_high_overtaken', 'finb', 14, 'fina')),
            (('count', '', 456, '', 'finb'), True, ('count_high_better', 'finb', 15)),
            (('count', '', 123, '', 'fina'), True, ('count_high', 'fina', 14, 'finb', 15)),
            (('count', '', 123, '', 'fina'), True, ('count_high_equal', 'fina', 15, 'finb')),
            (('count', '', 123, '', 'fina'), True, ('count_high_overtaken', 'fina', 16, 'finb')),
            (('count', '', 123, '', 'fina'), True, ('count_high_better', 'fina', 17)),
        ])


if __name__ == '__main__':
    unittest.main()
