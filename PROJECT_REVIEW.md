# 🔎 Project Review - Movie Search CLI

**Reviewed as:** read-only audit. No source files were modified as part of
this review.

**Scope:** `main.py`, `config.py`, `movie_service.py`, `utils.py`,
`requirements.txt`, `.gitignore`, `.env.example`, `README.md`.

---

## 1. Repository File Checklist

| File | Status | Action Taken |
|---|---|---|
| `README.md` | ✅ Present (comprehensive, beginner-oriented) | Not regenerated, per instructions |
| `.gitignore` | ✅ Present and correctly excludes `.env`, `venv/`, caches | None |
| `requirements.txt` | ✅ Present, pinned versions | None |
| `.env.example` | ✅ Present, well-commented | None |
| `LICENSE` | ❌ Missing | See Section 2 |
| `pyproject.toml` | ❌ Missing | See Section 2 |

### Overall Summary

This is a **small, clean, well-organized project**. It already has strong
fundamentals: a genuinely beginner-friendly `README.md`, a correctly
configured `.gitignore` that protects secrets, sensible custom exceptions,
and a clear separation between CLI presentation (`main.py`), configuration
(`config.py`), the API client (`movie_service.py`), and shared formatting
helpers (`utils.py`). The issues below are refinements, not red flags.

---

## 2. Missing Files - Why They Should Exist

### `LICENSE` (missing)

**Why it should exist:** Without a license file, a public GitHub
repository is, by default, "all rights reserved" under copyright law -
legally, no one else may copy, modify, or redistribute the code, even
though it's visible on GitHub. A `LICENSE` file (e.g., MIT, Apache-2.0)
explicitly grants those permissions.

**Why it's useful:** It removes legal ambiguity for anyone who wants to
use, fork, or contribute to the project, and it's one of the first things
experienced developers check before using open-source code. GitHub itself
will prompt for one when creating a repo and displays a warning banner if
it's absent.

### `pyproject.toml` (missing)

**Why it should exist:** This project is currently a loose collection of
`.py` files plus a `requirements.txt`. A `pyproject.toml` is the modern,
standardized way to declare project metadata (name, version, description,
author), dependencies, and tool configuration (e.g., for `black`, `ruff`,
or `pytest`) in one place, as defined by PEP 518/621.

**Why it's useful:** It would let the project be installed as a proper
package (`pip install .`), gives it an installable console-script entry
point (e.g., a `movie-search` command instead of `python main.py`), and
is the expected convention for any modern Python project a contributor
might encounter. It's optional for a simple personal CLI script, but
becomes valuable if this project grows or is meant to be shared/installed
by others.

*(No `LICENSE` or `pyproject.toml` files were generated, per your
instructions - only this explanation was written.)*

---

## 3. Code Review Findings

### 🟥 High Severity

None found. There are no critical bugs, crashes, or security
vulnerabilities in the reviewed code.

### 🟧 Medium Severity

**M1. `REQUEST_TIMEOUT` can crash the app on startup with a bad `.env` value**
- **Where:** `config.py`, line 36 - `REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "10"))`
- **Description:** If a user edits `.env` and sets `REQUEST_TIMEOUT` to a
  non-numeric value (e.g., `REQUEST_TIMEOUT=ten`), `int()` raises an
  unhandled `ValueError` at import time, producing a raw Python traceback
  instead of the app's normal friendly error handling.
- **Why it matters:** This directly contradicts the app's own design
  philosophy (seen throughout `config.py` and `movie_service.py`) of
  never showing users a raw stack trace. It's an easy mistake for a
  beginner following the `.env.example` file to make.
- **Recommended improvement:** Wrap the conversion in a `try/except
  ValueError`, falling back to a sane default (e.g., `10`) and optionally
  printing a warning.

**M2. Brittle error detection via substring matching**
- **Where:** `movie_service.py`, lines 98 and 103 -
  `if "Invalid API key" in error_message:` / `if "Movie not found" in error_message:`
- **Description:** The app distinguishes an invalid API key from a
  "movie not found" result purely by checking for specific English
  substrings inside OMDb's free-text error message.
- **Why it matters:** If OMDb ever changes its error wording (even
  slightly), these checks silently stop matching, and both error types
  would fall through to the generic `MovieServiceError` - degrading the
  user experience without an obvious cause.
- **Recommended improvement:** Where possible, prefer matching on stable
  identifiers (OMDb doesn't provide error codes, unfortunately, so this
  is a real API limitation) - at minimum, add a short comment noting this
  fragility and consider a case-insensitive match for resilience.

**M3. No automated test suite**
- **Where:** Project-wide.
- **Description:** There are no `tests/` directory, no `pytest` (or
  other framework) dependency, and no CI configuration.
- **Why it matters:** Regressions (e.g., in `utils.clean_value()`'s
  "N/A" handling, or in argument parsing) can only be caught by manual
  testing, which doesn't scale as the project grows and is easy to skip.
- **Recommended improvement:** Add a `tests/` folder with `pytest`
  covering pure functions first (`utils.clean_value`, `build_details_table`)
  and mocked-`requests` tests for `MovieService`.

### 🟨 Low Severity

**L1. Movie search is hardcoded to `type=movie`**
- **Where:** `movie_service.py`, lines 121 and 135 - both requests pass
  `"type": "movie"`.
- **Description:** OMDb's API also supports `series` and `episode`
  types, but this app can never retrieve them.
- **Why it matters:** It's a functional limitation rather than a bug, but
  it may surprise a user searching for a well-known TV show who gets a
  "not found" message.
- **Recommended improvement:** Expose an optional `--type` CLI flag
  (`movie` / `series` / `episode`) defaulting to `movie` to preserve
  current behavior.

**L2. No pagination for multi-result search**
- **Where:** `movie_service.py`, `search_movies()`; `main.py`,
  `display_search_results()`.
- **Description:** OMDb's search endpoint returns up to 10 results per
  page and supports a `page` parameter, which this app never sends or
  exposes.
- **Why it matters:** For a popular title with many matches, users only
  ever see the first 10 and have no way to see more.
- **Recommended improvement:** Add an optional `--page` flag or a
  "show more results?" prompt in interactive mode.

**L3. `requests.Session` is never explicitly closed**
- **Where:** `movie_service.py`, `MovieService.__init__`.
- **Description:** The session object is created but never closed via
  `.close()` or a context manager.
- **Why it matters:** For a short-lived CLI process this has no
  practical impact (the OS reclaims the socket on exit), but it's not a
  best practice if `MovieService` is ever reused in a longer-running
  context (e.g., a future web service).
- **Recommended improvement:** Implement `__enter__`/`__exit__` (or a
  `close()` method) on `MovieService` for future-proofing.

**L4. No retry/backoff for transient network failures**
- **Where:** `movie_service.py`, `_request()`.
- **Description:** A single timeout or connection error immediately
  surfaces as a `NetworkError` with no automatic retry.
- **Why it matters:** Minor, flaky Wi-Fi hiccups will force the user to
  manually re-run their search rather than the app silently retrying
  once or twice.
- **Recommended improvement:** Consider `requests`' built-in `Retry`
  adapter (via `HTTPAdapter`) for 1-2 automatic retries on connection
  errors only (not on 4xx/5xx from OMDb itself).

**L5. Minor type-hint inconsistency**
- **Where:** `main.py` - functions like `display_movie(movie: dict)` use
  bare `dict`, while `movie_service.py` consistently uses
  `Dict[str, Any]` from `typing`.
- **Why it matters:** Cosmetic only; doesn't affect behavior, but mixing
  styles slightly reduces consistency for future contributors.
- **Recommended improvement:** Standardize on `Dict[str, Any]` (or, if
  targeting Python 3.9+, the built-in generic `dict[str, Any]`)
  throughout.

**L6. Flat project layout (no `src/` package)**
- **Where:** Project-wide.
- **Description:** All modules live directly in the repository root
  rather than inside a package directory (e.g., `src/movie_search_cli/`).
- **Why it matters:** Perfectly fine and idiomatic for a small, four-file
  CLI script; would become a maintainability concern only if the project
  grows significantly (more modules, need for `pip install`-ability).
- **Recommended improvement:** No action needed now; revisit if/when
  adding `pyproject.toml` packaging.

### Not Flagged (Explicitly Reviewed and Found Acceptable)

- **Error handling:** Custom exception hierarchy
  (`MovieServiceError` -> `MovieNotFoundError` / `InvalidAPIKeyError` /
  `NetworkError`) is a clean, idiomatic pattern; `main.py` catches each
  specifically with tailored user-facing messages. ✅
- **Secrets management:** API key is loaded from `.env` via
  `python-dotenv`, never hardcoded, and `.env` is correctly gitignored. ✅
- **Documentation:** Every module and function has a clear docstring;
  `README.md` is thorough. ✅
- **Duplicate/dead code:** None found - the codebase is small and each
  function is used. ✅
- **Naming conventions:** Consistent, descriptive, PEP 8-compliant
  throughout. ✅
- **Logging:** The app intentionally uses Rich-formatted console output
  instead of the `logging` module, which is a reasonable choice for a
  small interactive CLI tool (not a long-running service) and not
  flagged as a deficiency.

---

## 4. GitHub Readiness Review

| Check | Status | Notes |
|---|---|---|
| Repository cleanliness | ✅ Good | No stray temp/cache files present in the archive |
| Documentation | ✅ Good | `README.md` is thorough; this review adds `INSTRUCTION.md` |
| Code quality | ✅ Good | See Section 3 - only minor/medium refinements suggested |
| Security / API key exposure | ✅ Good | No secrets committed; `.env` correctly ignored |
| `.gitignore` usage | ✅ Good | Covers `.env`, virtual environments, `__pycache__`, build artifacts, OS files, logs, test caches |
| Sensitive files | ✅ None found | |
| Temporary / cache / generated files | ✅ None found in the provided archive | |
| Virtual environment committed | ✅ Not present | Correctly excluded |
| License | ❌ Missing | See Section 2 |
| Package metadata (`pyproject.toml`) | ❌ Missing | See Section 2 - optional but recommended |

**Recommendation:** The project is functionally ready to publish today.
Adding a `LICENSE` file is the one item worth doing before making the
repository public, since it directly affects how others are legally
allowed to use the code. `pyproject.toml` is a nice-to-have, not a
blocker.

---

## 5. Repository Size Audit

| Metric | Result | Within Recommended Limit? |
|---|---|---|
| Total tracked files | 8 files (`main.py`, `config.py`, `movie_service.py`, `utils.py`, `README.md`, `requirements.txt`, `.gitignore`, `.env.example`) | ✅ Well under the 100-file guideline |
| Total size (excluding `venv/`, caches) | ≈ 40 KB | ✅ Well under the 20 MB guideline |

**Conclusion:** No size or file-count concerns whatsoever. This is a very
lightweight repository. No optimization is necessary. (No files were
deleted or modified as part of this audit.)

---

## 6. Final Verdict

The project is in **good shape**. It doesn't fully satisfy every item on
the file checklist (missing `LICENSE` and `pyproject.toml`), but it has
no High-severity issues, a handful of Medium-severity robustness
improvements worth making eventually (see M1-M3), and several optional
Low-severity polish items. It's safe and reasonable to publish to a
public GitHub repository as-is, ideally after adding a `LICENSE` file.
