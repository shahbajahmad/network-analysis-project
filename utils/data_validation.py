def validate_device_data(devices: list) -> bool:
    """
    Validate the device data to ensure it contains the required fields.

    Args:
        devices (list): A list of devices to validate.

    Returns:
        bool: True if all devices are valid, False otherwise.
    """
    required_fields = ['name', 'type', 'cost', 'specifications']
    for device in devices:
        for field in required_fields:
            if field not in device:
                print(f"Error: Missing field '{field}' in device data.")
                return False
    return True
