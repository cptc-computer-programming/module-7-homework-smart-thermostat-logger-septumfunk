# Constants
MIN_VALID_TEMP = 40
MAX_VALID_TEMP = 100
COLD_LIMIT = 68
WARM_LIMIT = 76

# I wrote a helper function since that's what we went over this week
# and I got this in pretty late
def get_int(name, min, max = None):
    read = int(input(f"Enter {name.lower()}: "))
    while read < min or (max != None and read > max):
        if max == None:
            print(f"Error: {name} must be greater than {min-1}.")
        else:
            print(f"Error: {name} must be between {min} and {max}.")
        read = int(input(f"Enter {name.lower()}: "))
    return read

# Collect the readings
num_readings = get_int("The number of temperature readings", 1)

# Cumulative variables
total_temp = 0
too_cold_count = 0
too_warm_count = 0

for i in range(1, num_readings + 1):
    temp = get_int(f"Temperature reading {i}", MIN_VALID_TEMP, MAX_VALID_TEMP)
    total_temp += temp
    if temp < COLD_LIMIT:
        too_cold_count += 1
    elif temp > WARM_LIMIT:
        too_warm_count += 1

average_temp = total_temp / num_readings

print("Smart Thermostat Summary\n------------------------")
print(f"Average temperature: {average_temp:.1f}") # I like f strings
print("Readings below comfort range:", too_cold_count)
print("Readings above comfort range:", too_warm_count)