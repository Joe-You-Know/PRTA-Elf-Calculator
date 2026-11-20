import unittest
from prta_elf.core import Puzzle, validate
from prta_elf.ssa_reuse import optimize_ssa


class SSATests(unittest.TestCase):
    def test_duplicate_source_occurrences(self):
        p = Puzzle("duplicates", (2, 3), (5, 10, 15), 100, 5)
        program = [["+", 0, 1, 2], ["+", 0, 1, 3],
                   ["+", 2, 3, 4], ["+", 4, 2, 4]]
        result = optimize_ssa(p, program)
        self.assertTrue(validate(p, result)["valid"])
        self.assertEqual(len(result), 3)

    def test_mixed_source_overwrite(self):
        p = Puzzle("overwrites", (3, 5), (8, 16, 19), 100, 3)
        program = [["+", 0, 1, 2], ["+", 2, 2, 1], ["+", 1, 0, 2]]
        result = optimize_ssa(p, program)
        self.assertTrue(validate(p, result)["valid"])
        self.assertLessEqual(len(result), len(program))

    def test_original_example(self):
        p = Puzzle("example", (3,), (1, 2, 5, 8), 9, 48)
        program = [["/",0,0,1], ["-",0,1,2], ["+",0,2,3], ["+",0,3,4]]
        self.assertTrue(validate(p, optimize_ssa(p, program))["valid"])


if __name__ == "__main__":
    unittest.main()
