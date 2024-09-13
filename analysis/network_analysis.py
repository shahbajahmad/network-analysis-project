import random
from models.network_device import NetworkDevice
from models.data_handler import DataHandler

class NetworkAnalysis:
    """
    A class to perform network performance analysis on network devices.
    """

    def __init__(self, devices: list[NetworkDevice], internet_speed: float):
        self.devices = devices
        self.internet_speed = internet_speed

    def simulate_performance(self) -> dict:
        """
        Simulate network performance for each device based on internet speed.

        Returns:
            dict: A dictionary with device names as keys and simulated performance (Mbps) as values.
        """
        performance = {}
        for device in self.devices:
            load_handling = random.uniform(0.8, 1.2) * self.internet_speed
            performance[device.name] = load_handling
        return performance

    def analyze_performance(self, performance_data: dict) -> str:
        """
        Generate a formatted analysis report for network performance.

        Args:
            performance_data (dict): Simulated performance data for devices.

        Returns:
            str: A formatted string representing the performance analysis.
        """
        analysis = "Network Performance Analysis:\n"
        analysis += "=" * 50 + "\n"
        for device, performance in performance_data.items():
            analysis += f"{device}: {performance:.2f} Mbps\n"
        return analysis

def main():
    devices = DataHandler.load_device_data('data/network_devices.json')
    if not devices:
        print("Failed to load devices.")
        return
    
    # Convert data to NetworkDevice objects
    device_objects = [NetworkDevice(**device) for device in devices]

    # Perform network analysis
    analysis = NetworkAnalysis(device_objects, internet_speed=100)
    performance_data = analysis.simulate_performance()
    report = analysis.analyze_performance(performance_data)

    print(report)
    DataHandler.save_report(report, 'performance_report.txt')

if __name__ == "__main__":
    main()
