from src.exceptions import InvalidEmployeeDataError

class BaseEmployee:
    """
    Parent Class modeling base employee characteristics from the IBM HR dataset.
    Demonstrates Encapsulation via private attributes.
    """
    def __init__(self, emp_id: int, age: int, department: str, monthly_income: float):
        if monthly_income < 0:
            raise InvalidEmployeeDataError("monthly_income", monthly_income, "Income cannot be negative.")
        if age < 18 or age > 100:
            raise InvalidEmployeeDataError("age", age, "Age must be between 18 and 100.")
            
        self.__emp_id = emp_id
        self.__age = age
        self.__department = department
        self.__monthly_income = monthly_income

    # Getters & Setters
    @property
    def emp_id(self) -> int:
        return self.__emp_id

    @property
    def age(self) -> int:
        return self.__age

    @property
    def department(self) -> str:
        return self.__department

    @property
    def monthly_income(self) -> float:
        return self.__monthly_income

    @monthly_income.setter
    def monthly_income(self, value: float):
        if value < 0:
            raise InvalidEmployeeDataError("monthly_income", value, "Income cannot be negative.")
        self.__monthly_income = value

    def calculate_annual_bonus(self) -> float:
        """Polymorphic method placeholder."""
        return self.__monthly_income * 0.05

    def display_info(self) -> str:
        """Base representation of employee details."""
        return f"ID: {self.__emp_id} | Dept: {self.__department} | Income: ${self.__monthly_income:,.2f}"


class TechnicalEmployee(BaseEmployee):
    """
    Child Class representing specialized technical staff (e.g., R&D, Lab Technicians).
    """
    def __init__(self, emp_id: int, age: int, department: str, monthly_income: float, research_projects: int):
        super().__init__(emp_id, age, department, monthly_income)
        self.research_projects = research_projects

    def calculate_annual_bonus(self) -> float:
        """Polymorphism implementation: Technical staff receive bonus per project."""
        base_bonus = super().calculate_annual_bonus()
        return base_bonus + (self.research_projects * 500.0)

    def display_info(self) -> str:
        base_info = super().display_info()
        return f"[Technical] {base_info} | Projects: {self.research_projects}"


class ExecutiveEmployee(BaseEmployee):
    """
    Child Class representing managerial/executive level staff.
    """
    def __init__(self, emp_id: int, age: int, department: str, monthly_income: float, leadership_level: int):
        super().__init__(emp_id, age, department, monthly_income)
        self.leadership_level = leadership_level

    def calculate_annual_bonus(self) -> float:
        """Polymorphism implementation: Bonus scaled by leadership level multiplier."""
        return self.monthly_income * (0.10 + (self.leadership_level * 0.05))

    def display_info(self) -> str:
        base_info = super().display_info()
        return f"[Executive] {base_info} | Leadership Level: {self.leadership_level}"