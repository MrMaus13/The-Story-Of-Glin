
import os
import re

CONFIG_FILE = "config.py"

def load_config():
    """Load the config file and extract variables."""
    config = {}
    if not os.path.exists(CONFIG_FILE):
        print(f"Error: {CONFIG_FILE} not found.")
        return config

    with open(CONFIG_FILE, 'r') as f:
        for line in f:
            match = re.match(r"(\w+)\s*=\s*(\d+(\.\d+)?)", line)
            if match:
                key, value = match.group(1), float(match.group(2)) if '.' in match.group(2) else int(match.group(2))
                config[key] = value
    return config

def save_config(config):
    """Save the updated variables back to the config file."""
    with open(CONFIG_FILE, 'w') as f:
        f.write("# config.py\n\n")
        for key, value in config.items():
            f.write(f"{key} = {value}\n")
    print("Config updated successfully.")

def display_menu(config):
    """Display a simple menu to edit config variables."""
    while True:
        print("\nCurrent Configuration:")
        for i, (key, value) in enumerate(config.items(), start=1):
            print(f"{i}. {key} = {value}")

        print("\nEnter the number of the variable to edit (or 'q' to quit):")
        choice = input(">> ").strip()
        if choice.lower() == 'q':
            break

        if choice.isdigit() and 1 <= int(choice) <= len(config):
            var_name = list(config.keys())[int(choice) - 1]
            new_value = input(f"Enter new value for {var_name} (current: {config[var_name]}): ").strip()
            if new_value.replace('.', '', 1).isdigit():  # Check if it's a valid number
                config[var_name] = float(new_value) if '.' in new_value else int(new_value)
            else:
                print("Invalid input. Please enter a numeric value.")
        else:
            print("Invalid choice. Please try again.")

    save_config(config)

def main():
    config = load_config()
    if not config:
        return
    display_menu(config)

if __name__ == "__main__":
    main()
