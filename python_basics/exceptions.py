"""
Topic:
    Exception Handling

Concepts:
    try
    except
    finally
    raise

Approach:
    Handle expected runtime errors without allowing the
    entire program to terminate unexpectedly.
"""


def check_age(age):
    try:
        # An age below 18 is considered invalid for this example.
        if age < 18:
            raise ValueError("Age must be 18 or above.")

        print("Age is valid.")

    except ValueError as error:
        # Handle the validation error and show a useful message.
        print(f"Error: {error}")

    finally:
        # This block executes regardless of whether an error occurred.
        print("Age validation completed.")


check_age(20)
check_age(16)