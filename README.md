# Dirty Data, Real Decisions

## Problem
Case closure times have drifted and the available evidence comes from an old system export.  
This prototype performs a small data-quality assessment and answers three operational questions from the available data.

## What the prototype does
- Loads a CSV export.
- Detects duplicate case IDs.
- Detects missing values.
- Detects invalid negative closure times.
- Removes unusable/duplicate records for analysis.
- Calculates average and median closure time.
- Compares Rural and Urban closure times.
- Clearly states what the data cannot establish.

## Requirements
- Python 3.9+
- No external packages

## Run
```bash
python app.py
```

## Expected output
The program prints a data-quality assessment, operational findings, and limitations.

## Project structure
```text
dirty_data_hackathon/
├── app.py
├── data.csv
├── README.md
├── DECISIONS.md
└── AI-USAGE.md
```

## Scope
This is intentionally a small, reliable prototype. The focus is on getting a clean end-to-end data assessment running rather than building a UI.
