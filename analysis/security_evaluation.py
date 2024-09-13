from models.network_device import NetworkDevice

class SecurityEvaluation:
    """
    A class to evaluate the security of network devices.
    """

    def __init__(self, devices: list[NetworkDevice]):
        self.devices = devices

    def evaluate_security(self) -> dict:
        """
        Evaluate the security of each device and calculate a security score.

        Returns:
            dict: A dictionary containing device names and their respective security scores.
        """
        security_scores = {}
        for device in self.devices:
            score = self._calculate_security_score(device)
            security_scores[device.name] = score
        return security_scores

    def _calculate_security_score(self, device: NetworkDevice) -> int:
        """
        Calculate the security score for a given device based on its type and specifications.

        Args:
            device (NetworkDevice): The network device to calculate the score for.

        Returns:
            int: The calculated security score (out of 100).
        """
        base_score = 80
        
        if 'Firewall' in device.device_type:
            base_score += 15
        if 'Security Software' in device.device_type or 'Security Hardware' in device.device_type:
            base_score += 10
        
        if device.specifications.get('Advanced Malware Protection', False):
            base_score += 10
        if device.specifications.get('Intrusion Prevention', False):
            base_score += 5
        if device.specifications.get('Threat Protection', False):
            base_score += 5
        if device.specifications.get('VPN Support', False):
            base_score += 3

        return min(base_score, 100)

    def security_report(self, security_scores: dict) -> str:
        """
        Generate a formatted security report based on the calculated security scores.

        Args:
            security_scores (dict): A dictionary containing device names and their security scores.

        Returns:
            str: A formatted string representing the security evaluation report.
        """
        report = "Network Security Evaluation:\n"
        report += "=" * 50 + "\n"
        for device, score in security_scores.items():
            report += f"{device}: Security Score = {score}/100\n"
        return report
