#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)
    pass


class PlantError(GardenError):
    pass


def water_plant(plant_name: str) -> None:
    if str.capitalize(plant_name) == plant_name:
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    valid_plant_list: list[str] = ["Tomato", "Lettuce", "Carrots"]
    invalid_plant_list: list[str] = ["Tomato", "lettuce", "Carrots"]
    print("\nTesting valid plants...")
    try:
        print("Opening watering system")
        for plant in valid_plant_list:
            water_plant(plant)
        print("Closing watering system")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        print("Closing watering system")

    print("\nTesting invalid plants...")
    try:
        print("Opening watering system")
        for plant in invalid_plant_list:
            water_plant(plant)
        print("Closing watering system")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        print("Closing watering system")
    finally:
        print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===")

    test_watering_system()
