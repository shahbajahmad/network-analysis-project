from models.network_device import NetworkDevice

class ProposalGenerator:
    """
    A class to generate a network architecture proposal.
    """

    def __init__(self, company_name: str, devices: list[NetworkDevice], performance_data: dict, security_scores: dict):
        self.company_name = company_name
        self.devices = devices
        self.performance_data = performance_data
        self.security_scores = security_scores

    def generate_proposal(self) -> str:
        """
        Generate a comprehensive network architecture proposal.

        Returns:
            str: A formatted proposal as a string.
        """
        proposal = f"Network Architecture Proposal for {self.company_name}\n"
        proposal += "=" * 80 + "\n"
        proposal += "Device Information:\n"
        proposal += self.generate_device_details()
        proposal += "\nNetwork Performance Analysis:\n"
        proposal += self.generate_performance_analysis()
        proposal += "\nNetwork Security Evaluation:\n"
        proposal += self.generate_security_evaluation()
        proposal += "\nTotal Estimated Cost: ${:.2f}\n".format(self.calculate_total_cost())
        return proposal

    def generate_device_details(self) -> str:
        """
        Generate a formatted string of all device information.

        Returns:
            str: A formatted string containing information about all devices.
        """
        details = ""
        for device in self.devices:
            details += device.device_info() + "\n"
        return details

    def generate_performance_analysis(self) -> str:
        """
        Generate a formatted string of the network performance analysis.

        Returns:
            str: A formatted string with performance data for each device.
        """
        analysis = ""
        for device, performance in self.performance_data.items():
            analysis += f"{device}: {performance:.2f} Mbps\n"
        return analysis

    def generate_security_evaluation(self) -> str:
        """
        Generate a formatted string of the network security evaluation.

        Returns:
            str: A formatted string with security scores for each device.
        """
        evaluation = ""
        for device, score in self.security_scores.items():
            evaluation += f"{device}: Security Score = {score}/100\n"
        return evaluation

    def calculate_total_cost(self) -> float:
        """
        Calculate the total cost of all devices included in the proposal.

        Returns:
            float: The total cost of all devices.
        """
        return sum(device.cost for device in self.devices)
