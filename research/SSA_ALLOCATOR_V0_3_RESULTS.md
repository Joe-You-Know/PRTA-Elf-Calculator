# Santa 2026 Elf Calculator — SSA allocation experiment

Date: 2026-11-18 (local research session; official Kaggle confirmation pending).

## Question

Can the earlier value-reuse compiler's 646 register-allocation fallbacks be
eliminated by retaining actual source-occurrence identities rather than treating
every future use of a numerical value as one persistent register obligation?

## Method

Compile the original legal sample programs into an SSA-like occurrence ledger:
each write is distinct even when its numerical output equals an earlier result.
Before an event, its operand occurrences must already have been constructed.
The physical machine retains at least one resident copy of each numerically
distinct currently live source value. An existing equal result can witness a
later occurrence without emitting a redundant calculator operation.

The allocator counts remaining uses of **constructed** occurrences, not future
occurrences which have not yet been produced. It emits only real legal
arithmetic instructions and independently verifies target coverage. If its
program is not shorter than the accepted prior submission, retain the prior
program. No competition data is committed.

## Results

Full comparison of 1,000 scored puzzle IDs from the user-provided
`santa-2026.zip`. The user reported a Kaggle-accepted score of **1,433,802**
for the previous `submission_reuse.csv`. This new version is so far **local**.

| Measure | Instructions / count |
| --- | ---: |
| Original sample submission | 1,490,379 |
| Prior Kaggle-accepted submission | 1,433,802 |
| New occurrence-aware combined submission | **1,350,568** |
| Saved over prior accepted submission | **83,234** |
| Saved over original | **139,811** |
| Puzzles improved over prior | 646 |
| Puzzles retaining prior | 354 |
| Allocator failures | 0 |
| Independently validated final programs | 1,000 / 1,000 |
| Local unit tests | 11 passing |
| CSV SHA-256 | `4eb48218e271aab30e0f08db2a9e7cb381cd0a0a573fc274c4eb16e711d7b763` |

The reduction against the previous accepted submission is approximately 5.805%.
This beats the 1,400,000 target by 49,432 instructions.

## Reproduction

```bash
python3 -m pip install -e .
python3 -m unittest discover -s tests -v
python3 scripts/benchmark_ssa.py \
  --puzzles data/puzzles.csv \
  --baseline data/sample_submission.csv \
  --prior results/submission_reuse.csv \
  --out results/submission_ssa.csv
```

Expected independently validated score: `1350568`.

Then submit (only after confirming current daily quota and Kaggle rules):

```bash
kaggle competitions submit -c santa-2026 \
  -f results/submission_ssa.csv \
  -m "SSA source-occurrence reuse v0.3 - 1350568 local instructions"
```

## Interpretation

The earlier failure to distinguish historical occurrences from currently
required values produced avoidable artificial register pressure. Correcting
that bookkeeping removes the fallbacks and produces a measurable score gain.
**These are conventional common-subexpression and liveness optimizations, not
empirical proof of PRTA-specific geometric savings.** A future independent
PRTA three-contact rotation planner must be compared against this baseline.
