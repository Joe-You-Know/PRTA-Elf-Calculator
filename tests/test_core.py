import unittest
from prta_elf.core import Puzzle, validate
from prta_elf.optimize import prune_provenance

class CoreTests(unittest.TestCase):
    def setUp(self):
        self.p = Puzzle("example", (3,), (1, 2, 5, 8), 9, 48)
        self.program = [["/",0,0,1],["-",0,1,2],["+",0,2,3],["+",0,3,4]]

    def test_worked_example(self):
        self.assertTrue(validate(self.p, self.program)["valid"])

    def test_exact_division_required(self):
        with self.assertRaisesRegex(ValueError, "inexact"):
            validate(self.p, [["+",0,0,1],["/",1,0,2],["/",1,2,3]])

    def test_prune_unused_event(self):
        noisy = self.program + [["+",0,0,5]]
        self.assertEqual(prune_provenance(self.p, noisy), self.program)

    def test_overwritten_source_before_read(self):
        q = Puzzle("overlap", (3,), (1, 2, 5), 9, 48)
        prog = [["/",0,0,1],["-",0,1,2],["+",0,2,3],["+",0,0,3]]
        self.assertEqual(len(prune_provenance(q, prog)), 3)

if __name__ == "__main__": unittest.main()
