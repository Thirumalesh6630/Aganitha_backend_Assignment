# Backend Takehome Problem

## Setup
1. Install dependencies using Poetry:
   ```sh
   poetry install
   ```

2. Run the script:
   ```sh
   poetry run get-papers-list --query "machine learning"
   ```

## Description
- Fetches research papers from PubMed.
- Filters out non-academic authors.
- Saves results as a CSV file.
