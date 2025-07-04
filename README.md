# Time Calculator
A simple Python script to add time durations to a given start time, with support for 12-hour and 24-hour formats and optional weekday calculations.

## Features
- **Flexible Time Addition**: Add any duration (hours and minutes) to a start time in 12-hour format (e.g., "8:30 AM").
- **12h/24h Conversion**: Handles conversions between 12-hour (AM/PM) and 24-hour formats.
- **Weekday Tracking**: Optionally specify a starting day to calculate the resulting day after adding time (e.g., "Monday" → "Tuesday").
- **Clean Output**: Returns formatted time with proper AM/PM, minutes padded with zeros, and day information (e.g., "next day" or "3 days later").

## Usage
Run the script with a start time, duration, and optional starting day:
```python
add_time("8:30 AM", "2:45")  # Returns "11:15 AM"
add_time("11:30 PM", "3:45", "Monday")  # Returns "3:15 AM, Tuesday (next day)"
```

## How It Works
- **Input Parsing**: Takes a start time (e.g., "8:30 AM"), duration (e.g., "2:45"), and optional weekday (e.g., "Monday").
- **Time Calculation**: Converts the start time to 24-hour format, adds the duration, and handles minute/hour overflow.
- **Day Tracking**: If a weekday is provided, calculates the resulting day based on the duration (e.g., adds days if time exceeds 24 hours).
- **Output Formatting**: Returns the result in 12-hour format with proper AM/PM and day information.

## Example
```python
print(add_time("3:00 PM", "3:10"))  # Output: "6:10 PM"
print(add_time("11:30 AM", "2:32", "Monday"))  # Output: "2:02 PM, Monday"
print(add_time("11:59 PM", "24:05", "Wednesday"))  # Output: "12:04 AM, Friday (2 days later)"
```

## Notes
- The script assumes valid input formats (e.g., "HH:MM AM/PM" for start time, "HH:MM" for duration).
- Weekdays are case-insensitive (e.g., "monday" or "Monday" both work).
- Built with ❤️ by Ehsan for quick and reliable time calculations.
