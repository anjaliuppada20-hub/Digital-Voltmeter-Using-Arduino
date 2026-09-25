# Digital Voltmeter - Python

voltage = float(input("Enter measured voltage (V): "))

print("\n--- Digital Voltmeter ---")
print("Measured Voltage:", round(voltage, 2), "V")

if voltage < 0:
    print("Invalid voltage!")
elif voltage > 5:
    print("Warning: Voltage is above 5V!")
else:
    print("Voltage is within range.")
