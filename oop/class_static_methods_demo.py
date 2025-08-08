class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        This method doesn't need access to class or instance attributes.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        This method can access class-level attributes, such as 'calculation_type'.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
