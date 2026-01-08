# DPG – Gilded Rose Refactoring Kata (Python)

This repository contains my implementation and refactoring of the **Gilded Rose Refactoring Kata** in Python.

The objective of this exercise is to improve a legacy codebase by applying clean code principles and object-oriented design, while **preserving existing behavior through automated tests**.

This project is structured and documented to reflect a real-world refactoring workflow and is suitable for technical interviews and code reviews.

---

## Repository Structure


```text
DPG/
├── python/
│   ├── gilded_rose.py
│   ├── texttest_fixture.py
│   ├── tests/
│   ├── requirements.txt
│   ├── README.md
│   └── venv/
└── README.md
```

- The root README (this file) provides a high-level overview.
- The python/ directory contains the full implementation, tests, and detailed instructions.

---

## Python Implementation

The Python implementation lives under the `python/` directory and includes:

- A refactored version of `gilded_rose.py`
- Removal of magic strings using constants
- Improved readability and separation of responsibilities
- Logic structured to enable future extension (polymorphism-ready design)
- Approval tests to guarantee unchanged behavior

Detailed setup and execution instructions are available in:

python/README.md

---

## What This Project Demonstrates

- Safe refactoring of legacy code
- Replacement of complex conditional logic with cleaner structure
- Use of constants instead of magic strings
- Design aligned with the Open/Closed Principle
- Use of Approval Tests to lock behavior before refactoring
- Professional project and Git workflow

---

## Quick Start (Python)

```bash
cd python  
python -m venv venv  
source venv/bin/activate  
pip install -r requirements.txt  
pytest  
```
All tests should pass successfully.

---

## Testing Strategy

This project uses multiple testing approaches:

- pytest as the test runner
- ApprovalTests.Python to verify that refactoring did not change output
- Legacy TextTest fixture for historical behavior comparison

Approval tests ensure confidence when refactoring by comparing current output with an approved baseline

## References - Gilded Rose Refactoring Kata 

https://github.com/emilybache/GildedRose-Refactoring-Kata 

https://github.com/approvals/ApprovalTests.Python"
