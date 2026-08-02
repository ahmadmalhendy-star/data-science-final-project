def summarize_employee_record(emp_dict: dict) -> str:
    """
    Custom reusable function with docstring to format employee dictionary entries.
    """
    age = emp_dict.get('Age', 'N/A')
    role = emp_dict.get('JobRole', 'N/A')
    income = emp_dict.get('MonthlyIncome', 0)
    return f"Role: {role:<22} | Age: {age} | Monthly Income: ${income:,.2f}"