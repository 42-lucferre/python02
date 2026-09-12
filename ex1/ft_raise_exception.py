#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    if temp_int < 0:
        raise ValueError(f"{temp_int}°C is too cold for plants (min 0°C)")
    if temp_int > 40:
        raise ValueError(f"{temp_int}°C is too hot for plants (max 40°C)")
    return (temp_int)


def test_temperature() -> None:
    x: str | int
    try:
        x = "25"
        print(f"Input data is '{x}'")
        x = input_temperature("25")
        print(f"Temperature is now {x}°C")
    except ValueError:
        print(f"Caught input_temperature error: {ValueError}")
    finally:
        print("")

    try:
        x = "abc"
        print(f"Input data is '{x}'")
        x = input_temperature(x)
        print(f"Temperature is now {x}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    finally:
        print("")

    try:
        x = "100"
        print(f"Input data is '{x}'")
        x = input_temperature(x)
        print(f"Temperature is now {x}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    finally:
        print("")

    try:
        x = "-50"
        print(f"Input data is '{x}'")
        x = input_temperature(x)
        print(f"Temperature is now {x}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    finally:
        print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":

    print("=== Garden Temperature Checker ===\n")
    test_temperature()
