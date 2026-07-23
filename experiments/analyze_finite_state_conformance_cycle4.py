from __future__ import annotations
import base64, gzip, hashlib, json, statistics
from collections import Counter, defaultdict
from pathlib import Path
from templex_zero.finite_state_conformance.schema import canonical_bytes, sha256_hex
try:
    from experiments.run_finite_state_conformance_cycle3 import build_files
except ModuleNotFoundError:
    from run_finite_state_conformance_cycle3 import build_files
DATA=Path('research/studies/004-finite-state-conformance/data')
PART_GLOB='cycle3_raw_results_v1.json.gz.b64.part*'
EXPECTED_GZIP_SHA='3f01b7346b1b5c690fd7dcd63c25ae0db1c874f369aea6e36c38a6d32bdf7679'
EXPECTED_JSON_SHA='a725f287b3d3a09b5d8e991e82daf9cb8f6a719c528a2e4047524cfd289bfc3c'
EXPECTED_PAYLOAD_SHA='bb34844aee696cde0ea19de9c48a5bd5ec8faf66391a492bc6277bf24ac69927'
OUTPUT=DATA/'final_analysis_v1.json'
def rate(n,d): return {'numerator':n,'denominator':d,'percent':f'{100*n/d:.6f}'}
def reconstruct():
 parts=sorted(DATA.glob(PART_GLOB)); assert len(parts)==8
 encoded=''.join(p.read_text() for p in parts); assert len(encoded)==39200
 g=base64.b64decode(encoded,validate=True); j=gzip.decompress(g); payload=json.loads(j)
 assert sha256_hex(g)==EXPECTED_GZIP_SHA and sha256_hex(j)==EXPECTED_JSON_SHA
 complete=dict(payload); recorded=complete.pop('payload_sha256'); assert recorded==EXPECTED_PAYLOAD_SHA==sha256_hex(canonical_bytes(complete))
 return g,j,payload
def build_analysis():
 stored_g,stored_j,d=reconstruct(); rerun_g,rerun_manifest=build_files(); assert rerun_g==stored_g
 rows=d['benchmark_rows']; methods=d['methods']; budgets=d['budgets']; n=d['counts']['distinguishable']
 detection=[]; efficiency=[]
 for b in budgets:
  for m in methods:
   rs=[r for r in rows if r['budget']==b and r['method']==m]; detected=[r for r in rs if r['detected']]
   detection.append({'method':m,'budget':b,'count':len(detected),'rate':rate(len(detected),n)})
   lens=[r['failing_trace_length'] for r in detected]
   efficiency.append({'method':m,'budget':b,'actions_total':sum(r['actions_executed'] for r in rs),'actions_mean':f"{statistics.mean(r['actions_executed'] for r in rs):.6f}",'resets_total':sum(r['resets'] for r in rs),'resets_mean':f"{statistics.mean(r['resets'] for r in rs):.6f}",'transition_coverage_mean':f"{statistics.mean(r['transition_coverage_count'] for r in rs):.6f}",'transition_pair_coverage_mean':f"{statistics.mean(r['transition_pair_coverage_count'] for r in rs):.6f}",'failing_trace_length_mean':None if not lens else f'{statistics.mean(lens):.6f}','failing_trace_length_median':None if not lens else f'{statistics.median(lens):.6f}','failing_trace_length_min':None if not lens else min(lens),'failing_trace_length_max':None if not lens else max(lens)})
 def dc(m,b,op=None): return sum(r['detected'] for r in rows if r['method']==m and r['budget']==b and (op is None or r['operator']==op))
 h1_r=dc('uniform-random',256); h1_g=dc('transition-coverage-guided',256)
 h1={'disposition':'unsupported','random':rate(h1_r,n),'guided':rate(h1_g,n),'guided_minus_random_percentage_points':f'{100*(h1_g-h1_r)/n:.6f}','required_percentage_points':'10.000000'}
 h2_classes=[]
 for op in sorted({r['operator'] for r in rows}):
  b=dc('lexicographic-breadth',1024,op); g=dc('transition-coverage-guided',1024,op)
  h2_classes.append({'operator':op,'breadth':rate(b,24),'guided':rate(g,24),'guided_minus_breadth_percentage_points':f'{100*(g-b)/24:.6f}'})
 h2_b=dc('lexicographic-breadth',1024); h2_g=dc('transition-coverage-guided',1024)
 h2={'disposition':'supported','breadth':rate(h2_b,n),'guided':rate(h2_g,n),'guided_minus_breadth_percentage_points':f'{100*(h2_g-h2_b)/n:.6f}','mutation_classes':h2_classes}
 by=defaultdict(list)
 for r in rows:
  if r['detected']: by[r['mutant_id']].append(r)
 order={(b,m):i for i,(b,m) in enumerate(( (b,m) for b in budgets for m in methods))}
 any_exact=sum(any(x['reduction']['exact_length_match'] for x in rs) for rs in by.values())
 all_exact=sum(all(x['reduction']['exact_length_match'] for x in rs) for rs in by.values())
 earliest_exact=sum(sorted(rs,key=lambda x:order[(x['budget'],x['method'])])[0]['reduction']['exact_length_match'] for rs in by.values())
 shortest_input_exact=sum(sorted(rs,key=lambda x:(x['failing_trace_length'],order[(x['budget'],x['method'])]))[0]['reduction']['exact_length_match'] for rs in by.values())
 exact_rows=sum(1 for r in rows if r['detected'] and r['reduction']['exact_length_match']); detected_rows=sum(1 for r in rows if r['detected'])
 invalid=sum(1 for r in rows if r['detected'] and (r['reduction'] is None or not r['reduction']['trace']))
 h3={'disposition':'unresolved','reason':'The frozen hypothesis defines a unique-mutant union denominator but does not freeze how multiple reducer outputs for one mutant are aggregated. Plausible rules cross the 90% threshold.','union_detected_mutants':len(by),'threshold_percent':'90.000000','invalid_reducer_outputs':invalid,'sensitivity':{'at_least_one_exact_output':rate(any_exact,len(by)),'all_detected_outputs_exact':rate(all_exact,len(by)),'earliest_detection_in_frozen_grid_exact':rate(earliest_exact,len(by)),'shortest_detected_input_row_exact':rate(shortest_input_exact,len(by)),'row_level_exact_outputs':rate(exact_rows,detected_rows)}}
 classification={}
 for dim in ('operator','family','state_count'):
  vals=[]
  for key in sorted({r[dim] for r in d['classification']},key=str):
   rs=[r for r in d['classification'] if r[dim]==key]; vals.append({'value':key,'distinguishable':sum(not r['equivalent'] for r in rs),'equivalent':sum(r['equivalent'] for r in rs)})
  classification[dim]=vals
 pairwise=[]
 for b in budgets:
  counts={m:dc(m,b) for m in methods}
  for left,right in [('transition-coverage-guided','uniform-random'),('transition-coverage-guided','lexicographic-breadth'),('lexicographic-breadth','uniform-random')]:
   pairwise.append({'budget':b,'left':left,'right':right,'count_difference':counts[left]-counts[right],'percentage_point_difference':f'{100*(counts[left]-counts[right])/n:.6f}'})
 result={'schema_version':1,'study':'Study 004 — Finite-State Conformance Counterexamples','cycle':4,'reproduction':{'byte_identical':True,'gzip_bytes':len(stored_g),'json_bytes':len(stored_j),'gzip_sha256':sha256_hex(stored_g),'json_sha256':sha256_hex(stored_j),'payload_sha256':d['payload_sha256'],'transport_part_count':8},'classification':classification,'shortest_length_distribution':{str(k):v for k,v in sorted(Counter(r['shortest_length'] for r in d['classification']).items())},'detection':detection,'pairwise_detection_differences':pairwise,'efficiency_and_trace_metrics':efficiency,'hypotheses':{'H1':h1,'H2':h2,'H3':h3},'study_disposition':'partial result','full_methodological_success':False,'limitations':['synthetic complete benchmark, not a population sample','same operator designed corpus, methods, fixtures, and analysis','fresh checkout and full historical regression unavailable','H3 aggregation was not frozen and is therefore unresolved','no transfer, novelty, security, or production claim']}
 result['analysis_payload_sha256']=sha256_hex(canonical_bytes(result)); return result
def main():
 r=build_analysis(); OUTPUT.write_bytes(canonical_bytes(r)); print(OUTPUT,len(OUTPUT.read_bytes()),sha256_hex(OUTPUT.read_bytes()),r['analysis_payload_sha256'])
if __name__=='__main__': main()
