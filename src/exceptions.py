class InvalidEmployeeDataError(Exception):
    """
    Custom exception raised when an employee data record violates 
    domain constraints (e.g., negative monthly income or invalid working years).
    """
    def __init__(self, field_name: str, value: object, message: str = "Invalid employee attribute provided."):
        self.field_name = field_name
        self.value = value
        self.message = f"{message} Field '{field_name}' received invalid value: {value}"
        super().__init__(self.message)