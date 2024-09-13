class NetworkDevice:
    """
    A class to represent a network device.

    Attributes:
        name (str): The name of the device.
        device_type (str): The type of the device (e.g., Router, Switch, Firewall).
        cost (float): The cost of the device in USD.
        specifications (dict): A dictionary containing device specifications.
    """

    def __init__(self, name: str, device_type: str, cost: float, specifications: dict):
        """
        Initialize a new NetworkDevice instance.

        Args:
            name (str): The name of the device.
            device_type (str): The type of the device.
            cost (float): The cost of the device.
            specifications (dict): A dictionary containing specifications of the device.
        """
        self.name = name
        self.device_type = device_type
        self.cost = cost
        self.specifications = specifications

    def device_info(self) -> str:
        """
        Generate a formatted string containing detailed information about the device.

        Returns:
            str: A formatted string with device information.
        """
        info = f"Device: {self.name}\nType: {self.device_type}\nCost: ${self.cost}\n"
        info += "Specifications:\n"
        for key, value in self.specifications.items():
            info += f"  {key}: {value}\n"
        return info

    def __repr__(self) -> str:
        """
        Return a string representation of the NetworkDevice object.

        Returns:
            str: A string representation of the device.
        """
        return f"NetworkDevice(name={self.name}, type={self.device_type}, cost={self.cost})"
