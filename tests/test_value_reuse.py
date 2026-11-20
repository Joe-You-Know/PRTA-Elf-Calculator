import unittest
from prta_elf.core import Puzzle, validate
from prta_elf.value_reuse import reuse_values, safe_reuse_values


class ValueReuseTests(unittest.TestCase):
    def test_repeated_value_reused_across_registers(self):
        puzzle = Puzzle("shared", (2, 3), (5, 10, 15), 100, 5)
        source = [["+", 0, 1, 2], ["+", 0, 1, 3],
                  ["+", 2, 3, 4], ["+", 4, 2, 4]]
        compiled = reuse_values(puzzle, source)
        self.assertEqual(len(compiled), 3)
        self.assertTrue(validate(puzzle, compiled)["valid"])

    def test_protect_overwritten_input_needed_later(self):
        puzzle = Puzzle("overwritten", (3, 5), (8, 16, 11), 100, 3)
        source = [["+", 0, 1, 2], ["+", 2, 2, 2], ["+", 2, 0, 2]]
        with self.assertRaises(ValueError):
            reuse_values(puzzle, source)

    def test_original_example(self):
        puzzle = Puzzle("example", (3,), (1, 2, 5, 8), 9, 48)
        src = [["/",0,0,1], ["-",0,1,2], ["+",0,2,3], ["+",0,3,4]]
        self.assertTrue(validate(puzzle, reuse_values(puzzle, src))["valid"])

    def test_safe_reuse_not_worse(self):
        puzzle = Puzzle("test", (2, 3), (5, 10), 100, 48)
        src = [["+", 0, 1, 2], ["+", 2, 2, 3]]
        result, method = safe_reuse_values(puzzle, src)
        self.assertTrue(validate(puzzle, result)["valid"])
        self.assertLessEqual(len(result), len(src))
        self.assertEqual(method, "value_reuse")


if __name__ == "__main__": unittest.main()
