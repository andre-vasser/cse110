#Input information
color = input("Please type your favorite color between Red, Green, Blue, Yellow, Magenta, Cyan and White:  ").lower()

# Define a dictionary to map color names to ANSI codes
color_codes = {
    "red": "\033[91m",
    "green": "\033[92m",
    "blue": "\033[94m",
    "yellow": "\033[93m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "white": "\033[97m"
}

# Get the corresponding ANSI code or set it to the default (white)
color_code = color_codes.get(color, "\033[97m")

# Capitalizar a primeira letra da cor
color = color.capitalize()

# Print screen information with the specified color

print(f"Your favorite color is {color_code}{color}\033[0m")