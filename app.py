print("Welcome to my Python program!")    # Greet the user

hours = input("How many hours did you study today? ")   # Ask for hours studied today

hours = float(hours) # Convert input to float

weekly_hours = hours * 7 # Calculate weekly study hours

print(f"You are on track to study {weekly_hours} hours this week.") # Display weekly study hours

try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")  # Handle invalid input
    exit() 
