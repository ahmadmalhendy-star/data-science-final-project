# IBM HR Analytics & Attrition Analysis — Data Science Final Project

## Project Overview
This project processes, cleans, and analyzes employee demographics and retention factors from the IBM HR Analytics dataset. Built using modular Python components, object-oriented concepts, and custom numerical calculations.

## Structure
- `src/classes.py`: Defines Object-Oriented representations of employee tiers (`BaseEmployee`, `TechnicalEmployee`, `ExecutiveEmployee`).
- `src/exceptions.py`: Custom error handling for invalid dataset attributes (`InvalidEmployeeDataError`).
- `src/utils.py`: Reusable data transformation utilities.
- `main.ipynb`: End-to-end execution notebook.
- `reports/Project_Report.xlsx`: Multi-sheet output deliverable containing raw cleaned data, aggregate tables, and executive summaries.

## Instructions
1. Ensure `kaggle.json` is located in your default Kaggle directory (`~/.kaggle/`).
2. Install requirements: `pip install -r requirements.txt`.
3. Open and run all cells in `main.ipynb`.