"""
Dirty Data, Real Decisions
Minimal hackathon prototype.

Run:
    python app.py

No external dependencies.
"""

import csv
from pathlib import Path
from statistics import mean, median

DATA = Path(__file__).parent / "data.csv"

def load_data():
    with open(DATA, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def quality_report(rows):
    columns = rows[0].keys()
    missing = {c: sum(1 for r in rows if not r[c].strip()) for c in columns}
    duplicate_keys = len(rows) - len({r["case_id"] for r in rows})
    invalid_days = sum(
        1 for r in rows
        if r["closure_days"].strip() and int(r["closure_days"]) < 0
    )
    return missing, duplicate_keys, invalid_days

def clean_rows(rows):
    # Remove exact duplicate case IDs, then keep records with usable closure time.
    seen = set()
    cleaned = []
    for r in rows:
        if r["case_id"] in seen:
            continue
        seen.add(r["case_id"])
        if not r["closure_days"].strip():
            continue
        if int(r["closure_days"]) < 0:
            continue
        cleaned.append(r)
    return cleaned

def answer_questions(rows):
    closed = [r for r in rows if r["status"] == "Closed" and r["closure_days"].strip()]
    rural = [r for r in closed if r["region"] == "Rural"]
    urban = [r for r in closed if r["region"] == "Urban"]

    avg = mean(int(r["closure_days"]) for r in closed)
    rural_avg = mean(int(r["closure_days"]) for r in rural)
    urban_avg = mean(int(r["closure_days"]) for r in urban)

    return {
        "closed_cases": len(closed),
        "average_closure_days": avg,
        "median_closure_days": median(int(r["closure_days"]) for r in closed),
        "rural_average": rural_avg,
        "urban_average": urban_avg,
        "slower_region": "Rural" if rural_avg > urban_avg else "Urban",
    }

def main():
    rows = load_data()
    missing, duplicates, invalid = quality_report(rows)
    cleaned = clean_rows(rows)
    q = answer_questions(cleaned)

    print("\n=== DIRTY DATA, REAL DECISIONS ===")
    print("\nDATA QUALITY ASSESSMENT")
    print(f"Rows loaded:              {len(rows)}")
    print(f"Duplicate case IDs:       {duplicates}")
    print(f"Invalid negative days:    {invalid}")
    print(f"Missing closure days:     {missing['closure_days']}")
    print(f"Missing benefit amounts:  {missing['benefit_amount']}")
    print(f"Rows after cleaning:      {len(cleaned)}")

    print("\nOPERATIONAL QUESTIONS")
    print(f"1. Average closure time:  {q['average_closure_days']:.1f} days")
    print(f"2. Median closure time:   {q['median_closure_days']:.1f} days")
    print(f"3. Slower region:         {q['slower_region']}")
    print(f"   Rural average:         {q['rural_average']:.1f} days")
    print(f"   Urban average:         {q['urban_average']:.1f} days")

    print("\nLIMITATION")
    print("The dataset is synthetic and only contains a short sample.")
    print("It can show differences in closure time, but it cannot establish")
    print("the root cause of the drift without historical/system metadata.")

    print("\nSTATUS: Prototype completed successfully.")

if __name__ == "__main__":
    main()
