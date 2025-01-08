def km_to_miles(km):
    return km * 0.621371

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print("Unit Converter:")
print("1. KM to Miles  2. Celsius to Fahrenheit")
choice = input("Choose conversion (1/2): ")

if choice == '1':
    km = float(input("Enter kilometers: "))
    print(f"{km} km = {km_to_miles(km):.2f} miles")
elif choice == '2':
    c = float(input("Enter Celsius: "))
    print(f"{c}°C = {celsius_to_fahrenheit(c):.2f}°F")
else:
    print("Invalid choice!")
