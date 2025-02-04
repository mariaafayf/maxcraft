# MaxCraft

MaxCraft is a Python-based program designed to create and manage user profiles with customizable settings for shared Windows computers. It allows users to personalize their computing experience while ensuring settings are stored and maintained efficiently.

## Features

- **Create User Profiles**: Easily create profiles for different users on a shared computer.
- **Customizable Settings**: Users can customize settings such as theme, font size, and language.
- **Update Profiles**: Modify existing profiles with new settings.
- **Delete Profiles**: Remove user profiles when they are no longer needed.
- **List Profiles**: View all available user profiles.

## Installation

1. Ensure you have Python installed on your system.
2. Clone this repository or download the `maxcraft.py` file.

## Usage

Run the script using Python:

```bash
python maxcraft.py
```

The script provides a command-line interface to manage user profiles. You can create, update, delete, and list profiles directly from the terminal.

## Example

Here's a quick example to get you started:

```python
maxcraft = MaxCraft()
maxcraft.create_profile("john_doe")
maxcraft.update_profile("john_doe", theme="dark", font_size=14)
maxcraft.list_profiles()
maxcraft.delete_profile("john_doe")
maxcraft.list_profiles()
```

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.