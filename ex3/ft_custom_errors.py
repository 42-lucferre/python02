#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def raise_errors(days: int = 0, water_level: int = 42) -> None:
    if days > 10:
        raise PlantError("The tomato plant is wilting!")
    if water_level < 42:
        raise WaterError("Not enough water in the tank!")


def testing_plant_error(days: int) -> None:
    try:
        raise_errors(days)
    except PlantError as e:
        print(f"Caught PlantError: {e}")


def testing_water_error(water_level: int) -> None:
    try:
        raise_errors(water_level=water_level)
    except WaterError as e:
        print(f"Caught WaterError: {e}")


def testing_garden_errors(days: int, water_level: int) -> None:
    try:
        raise_errors(days, water_level)
    except GardenError as e:
        print(f"Caught GardenError: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    testing_plant_error(23)

    print("\nTesting WaterError...")
    testing_water_error(23)

    print("\nTesting catching all garden errors...")
    testing_garden_errors(23, 57)
    testing_garden_errors(9, 23)

    print("\nAll custom error types work correctly!")
