"""Combine lawful QR construction with source-occurrence reuse; never worsen incumbent."""
import argparse,csv,json,hashlib,sys
from pathlib import Path
try:
    from prta_elf.core import load_puzzles,load_programs,validate
    from prta_elf.ssa_reuse import optimize_ssa
except ModuleNotFoundError:
    sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
    from prta_elf.core import load_puzzles,load_programs,validate
    from prta_elf.ssa_reuse import optimize_ssa

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--puzzles',required=True)
    ap.add_argument('--source',required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    puzzles=load_puzzles(a.puzzles); programs=load_programs(a.source)
    if set(puzzles)!=set(programs): raise ValueError('puzzle IDs mismatch')
    selected={}; improved=failed=original=total=0
    for pid,puzzle in puzzles.items():
        src=programs[pid]
        if not validate(puzzle,src)['valid']: raise ValueError('source invalid: '+pid)
        original+=len(src)
        try:
            candidate=optimize_ssa(puzzle,src)
            if len(candidate)<len(src):
                src=candidate; improved+=1
        except (AssertionError,ValueError): failed+=1
        if not validate(puzzle,src)['valid']: raise AssertionError(pid)
        selected[pid]=src;total+=len(src)
    f=Path(a.out);f.parent.mkdir(parents=True,exist_ok=True)
    with f.open('w',newline='',encoding='utf8') as stream:
        w=csv.writer(stream); w.writerow(['id','program'])
        w.writerows((pid,json.dumps(seq,separators=(',',':'))) for pid,seq in selected.items())
    received=load_programs(f)
    assert set(received)==set(puzzles)
    assert sum(validate(puzzles[pid],seq)['instruction_count'] for pid,seq in received.items())==total
    assert all(validate(puzzles[pid],seq)['valid'] for pid,seq in received.items())
    print(json.dumps({'original':original,'optimized':total,'saved':original-total,
        'improved_puzzles':improved,'failures':failed,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()},indent=2))
if __name__=='__main__':main()
