
# LeadGuard — CRM Lead Validation & Prioritization

LeadGuard is a Python-based prototype that automates customer lead validation, duplicate detection, and lead prioritization.

The project demonstrates how Python can be used to process customer data, apply business rules, and generate structured reports.

## Features

- Validate customer names, emails, and budgets
- Detect missing or invalid budget values
- Identify duplicate phone numbers among accepted leads
- Assign priority levels based on customer budgets
- Store processing results in structured dictionaries
- Generate summary statistics
- Group valid leads by priority

## Priority Rules

| Budget | Priority |
|--------|----------|
| 4000+ | High |
| 2000–3999 | Medium |
| 1–1999 | Low |

## Technologies

- Python 3
- Lists and dictionaries
- Sets
- Functions
- Conditional statements
- Loops

No external libraries are required.

## Project Structure

    LeadGuard/
    ├── main.py
    └── README.md

## How to Run

1. Install Python 3.
2. Download the project.
3. Open a terminal in the LeadGuard directory.
4. Run:

    python main.py

## Example Output

    alex - Valid Low
    bob - Invalid Missing budget
    jery - Valid Medium
    coil - Invalid Missing email
    vasya - Duplicate
    kate - Valid High

    Valid: 3
    Invalid: 2
    Duplicate: 1

    === HIGH PRIORITY LEADS ===
    kate

    High: ['kate']
    Medium: ['jery']
    Low: ['alex']

## Current Limitations

- Uses predefined sample data
- Does not fully validate email or phone formats
- Does not handle every unexpected input type
- Does not persist data between runs
- Duplicate detection is applied after basic validation

## Future Improvements

- CSV and JSON file processing
- Advanced data validation
- Automated unit tests
- REST API with FastAPI
- PostgreSQL database integration
- Docker containerization

## Project Purpose

Built as a practical Python learning project focused on data processing, validation logic, and business workflow automation.
