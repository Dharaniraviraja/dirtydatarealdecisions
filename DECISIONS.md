# DECISIONS.md

## Chosen approach
I chose a simple Python CLI because the problem is primarily a data/analytics problem and a CLI is sufficient for demonstrating the workflow.

## What I built
1. Load the system export.
2. Profile data quality.
3. Remove duplicate and unusable records.
4. Calculate operational metrics.
5. Compare closure times by region.
6. State limitations explicitly.

## What I rejected
- A web frontend: not necessary for the core analytical task.
- A database: unnecessary for a small CSV prototype.
- A machine-learning model: the available sample is too small and the objective is data quality/decision support.
- Complex deployment: the prototype has no external service dependency.

## Cut due to time
- Interactive charts.
- Automated report export.
- Historical trend analysis.
- Statistical significance testing.
- Data-quality scoring dashboard.

## What the solution does not do
It does not prove why closure times changed. It identifies quality problems and describes patterns visible in the supplied sample.

## First improvement
The first improvement would be to connect multiple historical exports and build a month-over-month closure-time trend, while preserving the same data-quality checks.
The prototype was kept dependency-free so it can run in a clean Python environment.
