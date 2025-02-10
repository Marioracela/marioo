# Program using four-digit year format
def calculate_age_fixed(birth_year):
    current_year = 2099  # Simulating the year 2099
    age = current_year - birth_year
    return age

# Simulate the year 2100
def simulate_y2k_fix():
    birth_year = 1970  # Simulating someone born in 1970
    age = calculate_age_fixed(birth_year)
    print(f"Age in 2099: {age}")

    # Simulate the year 2100
    current_year = 2100  # Simulating the year 2100
    age = current_year - birth_year
    print(f"Age in 2100: {age}")

simulate_y2k_fix()