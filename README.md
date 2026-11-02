# Blood Donor Near Me

A Python, MySQL, and Streamlit project that helps identify and rank potential blood donors for a blood request using red-cell blood-group compatibility, donor eligibility filters, geographic distance, and a Top-K ranking algorithm.

> **Important:** This is an academic/project matching tool, not a medical decision system. Blood-bank staff and qualified medical professionals must confirm donor eligibility, compatibility, testing, and availability before any donation.

## Features

- Blood-group compatibility lookup for the eight common ABO/Rh blood groups.
- Donor eligibility filtering using the project's configurable rules.
- Distance calculation using the Haversine formula.
- Donor ranking using a weighted score.
- Top-K donor selection using a heap.
- Streamlit interface for the project pages.
- MySQL storage and basic donor/request analytics.
- Pytest unit tests for compatibility, eligibility, and ranking.

## Technology

- Python 3
- Streamlit
- MySQL
- `mysql-connector-python`
- Pytest

## Project structure

```text
Blood-Donor-Near-Me/
├── app.py
├── config.py
├── database.py
├── matcher.py
├── requirements.txt
├── README.md
├── .gitignore
├── algorithms/
│   ├── __init__.py
│   ├── compatibility.py
│   ├── eligibility.py
│   ├── location.py
│   ├── scoring.py
│   ├── donor_ranking.py
│   └── donor_search.py
├── tests/
│   ├── __init__.py
│   ├── test_compatibility.py
│   ├── test_eligibility.py
│   └── test_ranking.py
└── scripts/
    └── seed_test_data.py  # optional development-only sample data script
```

## Requirements

- Python 3.10 or newer recommended.
- MySQL Server.
- A MySQL database created using the project's schema.
- pip.

## Setup and run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/blood-donor-near-me.git
cd blood-donor-near-me
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Create the MySQL database

Create the database and tables using the SQL schema prepared for this project. The application expects the following tables:

- `users`
- `donors`
- `blood_requests`
- `matches`
- `blood_compatibility` (if using the compatibility lookup table in the database query)

Make sure the table and column names match the SQL queries in `database.py`.

### 5. Configure database access

Set your local MySQL connection values in `config.py`, or adapt the file to read environment variables.

Example configuration shape:

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "YOUR_LOCAL_PASSWORD",
    "database": "blood_donor_near_me"
}
```

Do not commit real passwords, API keys, or other secrets to GitHub. For a public repository, use environment variables or a local `.env` file that is excluded by `.gitignore`.

### 6. Start the application

```bash
streamlit run app.py
```

Streamlit will print a local URL, usually `http://localhost:8501`.

## Run tests

From the project root:

```bash
python -m pytest -v
```

The tests cover the current compatibility, eligibility, and donor-ranking logic. They do not test a live MySQL server or every Streamlit interaction.

## Algorithms and data structures

### 1. Blood-group compatibility — dictionary / hash map

`algorithms/compatibility.py` stores the supported red-cell donor-to-recipient compatibility mapping in a Python dictionary. Lookup is typically O(1) on average.

### 2. Eligibility filtering — rule-based filtering

`algorithms/eligibility.py` checks the project's rules, including availability, age, weight, and time since last donation. Filtering each donor is O(1), so filtering n donors is O(n).

The age threshold, weight threshold, and 90-day interval are **project assumptions for demonstration**. They are not universal clinical rules and must not be used to decide real-world donor eligibility.

### 3. Geographic distance — Haversine formula

`algorithms/location.py` calculates the great-circle distance between two latitude/longitude coordinates. This is useful for estimating distance between a donor and a hospital.

### 4. Weighted scoring — ranking heuristic

`algorithms/scoring.py` calculates a project score using factors such as distance, urgency, and donation recency. This is a demonstration ranking heuristic, not a medical suitability score. Hard eligibility and compatibility checks should happen before ranking.

### 5. Top-K donor selection — min-heap

`algorithms/donor_ranking.py` uses a min-heap to keep the best K donors while processing n candidates. Time complexity is O(n log K), and additional heap space is O(K).

### 6. Donor grouping — dictionary / hash map

`algorithms/donor_search.py` can group donors by blood group to make candidate lookup more efficient.

## Current implementation notes

Check these points against the code before describing the project as production-ready:

- The current Streamlit donor-registration and blood-request forms may be UI-only and may not save records to MySQL yet.
- The View Matches page may still be a placeholder unless it has been connected to `matcher.py`.
- Basic analytics can read donor and request counts from MySQL if the database functions and schema are configured.
- Admin pages should be protected by authentication before deployment.
- Sample donor records are for local testing only. Do not publish fake personal data as real donor records.

## Before publishing

- Remove test donor rows and test-only accounts from the database.
- Remove `sample_data.py`, or move it to `scripts/seed_test_data.py` and clearly label it as development-only.
- Keep automated tests in `tests/`.
- Remove `.venv/`, `__pycache__/`, and `.pytest_cache/` from the repository.
- Keep database credentials out of Git.
- Verify that the README matches the actual schema and current app functionality.
- Run the tests and start the Streamlit app locally.

## Disclaimer

This project is intended for learning and demonstration. It does not replace professional blood-bank processes, laboratory testing, medical history review, or clinical decisions. A displayed match is only a potential contact suggestion; the blood bank must independently confirm all requirements.
