



class OOPDunderMethods:
    """
        Constructor method in python.
        Args:
            self (OOPDunderMethods): The same instance.
        Returns:
            None
        Raises:
            None
    """
    def __init__(self) -> None:
        self.title = "OOP Dunder Methods"

    """
        Method to control what the print() method will do when passing it this object.
        Args:
            self (...): ...
        Return:
            str: Message printed via print() method.
        Raises:
            None
    """
    def __str__(self) -> str: 
        return "Wow! You used the __str__ dunder method! I'm so proud of you :')"

    """
        Method similar to __str__, but is called when on debugging settings or by calling the object
        directly.
        Args:
            self (...): ...
        Return:
            str: Message to be printed when the instance is called.
        Raises:
            None
    """
    def __ref__(self) -> str:
        return "DEBUG: You just used __ref__! Nice job :D"

    """
        Allows the usage of == operator among two objects based on something (typically object properties and content)
        
    """
    def __eq__(self, other):
        if isinstance(other, OOPDunderMethods):
            return self.is_equal == other.is_equal
        return NotImplemented






