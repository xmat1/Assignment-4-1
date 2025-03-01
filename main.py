"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
# Charge for this sign.
charge = 0.00
# Number of characters.
numChars = 18
# Color of characters.
color = "black"
# Type of wood.
woodType = "oak"

# Write assignment and if statements here as appropriate.
charge += 35.00

if numChars > 5:
    charge += (numChars - 5) * 4.00

if woodType.lower() == "oak":
    charge += 20.00

if color.lower() == "gold":
    charge += 15.00

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
