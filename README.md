# Python B2 fixture: create.py

This repository contains the unmodified `create.py` B2 resource-creation fixture for checkpoint 1.5 pipeline validation.

## Provenance

- Source repository: `Xyton-semi/Xycode`
- Source revision: `83204a74ee270cc2f000016f548552ab83563219`
- Source path: `hardening/b2_stress_fixtures/python/create.py`
- Source bytes: `3887`
- Source SHA-256: `178076df5f8f7d67f7d51d018c84352e2b18b67cf59dbed7128523aeed2d23b2`

The original source bytes are preserved. The README and pyproject.toml are packaging metadata added for this repository. The module uses Python standard-library APIs only and exposes resource-creation examples; it has no command-line main. Do not invoke the resource-opening example functions as a smoke test.

## Build and analysis

The analysis entry module is `create.py`. Project distribution name is `python-create` and the importable module is `create`. Use the governed Python runtime selected by the pipeline request. The optional wheel build uses the pinned setuptools backend declared in pyproject.toml; there are no project runtime dependencies.

This corpus is an R1-observable static fixture with OPEN/CLOSED examples. Its presence does not claim all producer stages or B2 semantic qualification have passed; pipeline results are recorded separately.
