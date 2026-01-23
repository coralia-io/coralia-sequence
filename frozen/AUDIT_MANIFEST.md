# Audit Manifest

This file documents the frozen reproducibility artifacts for the Coralia Classification trilogy (Papers I–III).

## Purpose

These files are frozen to ensure reproducibility of the classification result. They should not be modified after publication.

## File Checksums (SHA-256)

```
0910fa57f3c197deb2e2092356ed2ce573a070eaae9705599bd1ea0635c7295a  frozen/code/axiom_drop.py
9fdee17f0c28e38e670bb613285a54f4468cd6e6cd2161301d9f613973ff4297  frozen/code/cascade_triple_enum.py
efff6a3aa1839ab25e909d9e092fe0046711bf4506091482873c6071bdda095b  frozen/code/ceiling_scan.py
8dddad1141f4c714196bfc17e7319a637f33f7ac2e67f6413f3f560efa17dc69  frozen/code/enumeration_core.py
f3a7d19c86ae389756f9161f383d34e6b7b98dcf18a05f2be53765dbc79e77ea  frozen/data/survivor_tables.csv
```

## Verification

To verify file integrity:

```bash
cd frozen
sha256sum -c <<EOF
0910fa57f3c197deb2e2092356ed2ce573a070eaae9705599bd1ea0635c7295a  code/axiom_drop.py
9fdee17f0c28e38e670bb613285a54f4468cd6e6cd2161301d9f613973ff4297  code/cascade_triple_enum.py
efff6a3aa1839ab25e909d9e092fe0046711bf4506091482873c6071bdda095b  code/ceiling_scan.py
8dddad1141f4c714196bfc17e7319a637f33f7ac2e67f6413f3f560efa17dc69  code/enumeration_core.py
f3a7d19c86ae389756f9161f383d34e6b7b98dcf18a05f2be53765dbc79e77ea  data/survivor_tables.csv
EOF
```

## File Descriptions

| File | Description |
|------|-------------|
| `code/enumeration_core.py` | Exhaustive search proving uniqueness under axioms C1–C9 |
| `code/cascade_triple_enum.py` | Enumerates valid terminal gap triples (8,7,5) |
| `code/ceiling_scan.py` | Verifies ceiling=35 is necessary for uniqueness |
| `code/axiom_drop.py` | Tests axiom independence by counting survivors |
| `data/survivor_tables.csv` | Survivor counts for each axiom-drop scenario |

## Reproducibility

All scripts are standalone Python 3 with no external dependencies.

```bash
python frozen/code/enumeration_core.py   # Should output: Solutions: 1
python frozen/code/ceiling_scan.py       # Shows uniqueness at ceiling=35
python frozen/code/axiom_drop.py         # Shows axiom independence
```

## Zenodo DOIs

- Paper I: [10.5281/zenodo.18121785](https://doi.org/10.5281/zenodo.18121785)
- Paper II: [10.5281/zenodo.18150002](https://doi.org/10.5281/zenodo.18150002)
- Paper III: [10.5281/zenodo.18346226](https://doi.org/10.5281/zenodo.18346226)
