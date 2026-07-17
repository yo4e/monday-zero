# Study 002 Cycle 5 Verification

_Date: 2026-07-17 (Asia/Tokyo)_

## Formal artifacts

- Random experiment commit: `970b5a7b35b40806b8962c4a73d3841804a95e7a`
- Targeted-test commit: `62cdbb8efd7edc39424396d74b7a00c2cbdad890`
- Random data commit: `df0c3d27c26dab304c6dc3579ce87453a952fd0d`
- Analysis commit: `adba359c045213797a45b300f4ce25d49338373d`

## Local verification

- The reconstructed manifest produced the frozen SHA-256 `cff3a75a58442b843134cd05a337e2af3166e1c1e035c15fc890f576e0495cee` and all 18 frozen IDs in manifest order.
- `tests/test_exact_first_random_screen.py`: **4 passed**.
- `python -m compileall -q src experiments tests`: completed without error.
- The final locally executed experiment source had Git blob SHA `051ab0fa3de409c38adf35d327ade8111ae597d8`, identical to the live GitHub experiment file.
- Two complete executions each ran 36,000 games and produced deterministic SHA-256 `d3726b0dff560befc4bbc86fa69b7f9aa889d0e41d16f2a54a3b1acc0df7960e`.

## Execution interruption

An initial attempt to run both complete screens inside one foreground command exceeded the outer command timeout and produced no completed output file. It was excluded. The final evidence uses two later runs that each completed and wrote a valid result file.

## Limitations

- The experiment script itself was byte-identical to GitHub.
- The schema and manifest dependencies were functionally reconstructed and reproduced the frozen manifest hash, but byte-identical identity of every dependency is not claimed.
- Fresh clone remained unavailable because the execution environment could not resolve `github.com`.
- The repository has no recorded GitHub Actions workflow.
