import unittest

from logger_rate_limiter import RequestLogger


def run_sequence(time_limit, sequence):
    rl = RequestLogger(time_limit)
    results = []
    for ts, msg, _ in sequence:
        results.append(rl.message_request_decision(ts, msg))
    return results


class TestRequestLogger(unittest.TestCase):
    def test_parametrized_sequences(self):
        cases = [
            # simple accept then reject then accept after time_limit
            (
                5,
                [
                    (1, "m", True),
                    (3, "m", False),
                    (6, "m", True),
                ],
            ),
            # different messages independent
            (
                10,
                [
                    (1, "a", True),
                    (2, "b", True),
                    (5, "a", False),
                    (12, "a", True),
                    (13, "b", True),
                ],
            ),
            # exact time_limit should be accepted
            (
                7,
                [
                    (1, "x", True),
                    (8, "x", True),
                ],
            ),
            # zero time_limit accepts same-timestamp duplicates
            (
                0,
                [
                    (1, "z", True),
                    (1, "z", True),
                ],
            ),
            # float timestamps
            (
                1.5,
                [
                    (1.0, "f", True),
                    (2.4, "f", False),
                    (2.6, "f", True),
                ],
            ),
            # negative timestamps
            (
                5,
                [
                    (-10, "n", True),
                    (-6, "n", False),
                    (-5, "n", True),
                ],
            ),
            # many rapid alternations and multiple messages
            (
                3,
                [
                    (0, "a", True),
                    (1, "b", True),
                    (2, "a", False),
                    (3, "b", False),
                    (4, "a", True),
                    (6, "b", True),
                ],
            ),
        ]

        for time_limit, sequence in cases:
            with self.subTest(time_limit=time_limit, sequence=sequence):
                expected = [s[2] for s in sequence]
                self.assertEqual(run_sequence(time_limit, sequence), expected)

    def test_message_map_updates_only_on_accept(self):
        rl = RequestLogger(4)
        self.assertTrue(rl.message_request_decision(1, "keep"))
        # rejected within limit, map should still have original timestamp
        self.assertFalse(rl.message_request_decision(3, "keep"))
        self.assertEqual(rl.message_map["keep"], 1)
        # now after limit, accepted and map updated
        self.assertTrue(rl.message_request_decision(5, "keep"))
        self.assertEqual(rl.message_map["keep"], 5)

    def test_multiple_unique_messages_do_not_interfere(self):
        rl = RequestLogger(2)
        messages = ["m1", "m2", "m3"]
        timestamps = [1, 1, 1]
        for t, m in zip(timestamps, messages):
            self.assertTrue(rl.message_request_decision(t, m))
        # repeating each at t=2 should be False (within limit)
        for m in messages:
            self.assertFalse(rl.message_request_decision(2, m))


if __name__ == "__main__":
    unittest.main(verbosity=2)
