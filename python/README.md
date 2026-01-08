# Test Validation Guide (Gilded Rose – Python)

This document describes the exact steps used to validate the refactored **Version A** of the Gilded Rose kata, ensuring behavior preservation and test correctness.

---

## 1. Create and activate a virtual environment (recommended)

Using a virtual environment isolates dependencies and avoids conflicts.

```bash
python -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt after activation.

---

## 2. Install project dependencies

Install all required dependencies listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

This installs `pytest` and `ApprovalTests`.

---

## 3. Remove the placeholder unit test

The file `tests/test_gilded_rose.py` contains a deliberately failing placeholder test (`test_foo`) as part of the kata starter code.

**Action taken:**

* The placeholder test was removed or commented out
* The file itself was kept

This is expected and correct behavior for the kata.

---

## 4. Run the full test suite using pytest

From the **project root directory**, run:

```bash
pytest
```

Notes:

* `pytest` also runs any `unittest`-based tests
* Running pytest from the project root is required for test discovery

---

## 5. Handle ApprovalTests (first run only)

On the first run, the ApprovalTests test generates a file:

```
*.received.txt
```

located in:

```
tests/approved_files/
```

This file contains the full output of the TextTest fixture.

### Validation step

* Review the contents of the `.received.txt` file
* Confirm that it matches the expected Gilded Rose behavior

---

## 6. Approve the output

Once verified, approve the output by renaming the file:

```bash
mv tests/approved_files/*.received.txt \
   tests/approved_files/test_gilded_rose_approvals.test_gilded_rose_approvals.approved.txt
```

This establishes the approved baseline for future runs.

---

## 7. Run tests again

```bash
pytest
```

Expected result:

```
============================================================================================== test session starts ===============================================================================================
platform darwin -- Python 3.14.2, pytest-9.0.2, pluggy-1.6.0
rootdir: /Users/luiz.prina/Desktop/DPG/python
plugins: approvaltests-0.2.4, approvaltests-16.2.1
collected 1 item                                                                                                                                                                                                 

tests/test_gilded_rose_approvals.py .                                                                                                                                                                      [100%]

=============================================================================================== 1 passed in 0.01s ================================================================================================
```

All tests should now pass successfully.

---

## Notes

* The external TextTest GUI setup is optional and was not required
* ApprovalTests internally executes `texttest_fixture.py`
* Python 3.10–3.12 are recommended; Python 3.14 was used successfully here



This concludes the test validation process.
