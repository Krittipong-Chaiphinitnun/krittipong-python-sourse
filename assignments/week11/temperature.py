"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""

def get_temperatures():
    """Prompt user to enter 7 daily temperatures and return as a list."""
    temps = []
    for i in range(7):
        temp = float(input(f"Enter temperature for day {i+1}: "))
        temps.append(temp)
    return temps

def analyze_temps(temp_list):
    """Return average, highest, and lowest temperature as a tuple."""
    avg = sum(temp_list) / len(temp_list)
    high = max(temp_list)
    low = min(temp_list)
    return avg, high, low

def display_analysis(avg, high, low):
    """Print the temperature analysis in a formatted way."""
    print("Temperature Analysis for the Week:")
    print(f"Average: {avg:.1f} C")
    print(f"Highest: {high:.0f} C")
    print(f"Lowest: {low:.0f} C")

if __name__ == "__main__":
    temps = get_temperatures()
    avg, high, low = analyze_temps(temps)
    display_analysis(avg, high, low)   