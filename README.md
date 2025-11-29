[![Tests](https://github.com/cmudrc/AutoBoltAgent/actions/workflows/test.yml/badge.svg)](https://github.com/cmudrc/AutoBoltAgent/actions/workflows/test.yml)

# AutoBoltAgent

AutoBoltAgent is a small Python package that provides AI-powered assistance for bolt design tasks. It aims to help engineers prototype bolt specifications and explore design options programmatically.

Key points:
- Lightweight library packaged under `autoboltagent`.
- Includes example tools for low- and high-fidelity bolt generation and helper inputs.

## Requirements
- Python 3.10+
- (Optional) Conda for easy environment setup — an `environment.yml` is included in the repository.

## Quick start
1. Create and activate a Python environment (optional, using conda):

```bash
# create (first time)
conda env create -f environment.yml
# activate
conda activate autoboltagent
```

2. Install the package in editable mode:

```bash
pip install -e .
```

3. Use the package from Python. Example (interactive):

```python
from autoboltagent import agents, prompts

# Create whatever object or call whatever function you need from the public API.
# This README shows a minimal example; check the source for available functions.
print('autoboltagent package loaded')
```

## Running tests
Run the project's test suite with pytest:

```bash
pytest -q
```

The repository includes a basic tests folder (`tests/`) with a sanity test to help ensure the package imports correctly.

## Contributing
Contributions are welcome. Keep changes small and focused, add tests for new behaviour, and run the test suite before opening a PR.

## License
This project includes a `LICENSE` file — follow the terms in that file.

---

If you'd like, I can also add a usage example that calls a specific function from the library (I can inspect `src/autoboltagent` and wire a short example).
