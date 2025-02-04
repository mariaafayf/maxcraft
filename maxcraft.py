import json
import os

class UserProfile:
    def __init__(self, username, settings=None):
        self.username = username
        self.settings = settings or {
            "theme": "light",
            "font_size": 12,
            "language": "English"
        }

    def update_settings(self, **kwargs):
        self.settings.update(kwargs)

    def to_dict(self):
        return {
            "username": self.username,
            "settings": self.settings
        }

class MaxCraft:
    def __init__(self, data_file='user_profiles.json'):
        self.data_file = data_file
        self.profiles = self.load_profiles()

    def load_profiles(self):
        if not os.path.exists(self.data_file):
            return {}

        with open(self.data_file, 'r') as file:
            return json.load(file)

    def save_profiles(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.profiles, file, indent=4)

    def create_profile(self, username):
        if username in self.profiles:
            print(f"Profile for {username} already exists.")
            return

        profile = UserProfile(username)
        self.profiles[username] = profile.to_dict()
        self.save_profiles()
        print(f"Profile for {username} created successfully.")

    def update_profile(self, username, **settings):
        if username not in self.profiles:
            print(f"No profile found for {username}.")
            return

        profile = UserProfile(username, self.profiles[username]['settings'])
        profile.update_settings(**settings)
        self.profiles[username] = profile.to_dict()
        self.save_profiles()
        print(f"Profile for {username} updated successfully.")

    def delete_profile(self, username):
        if username in self.profiles:
            del self.profiles[username]
            self.save_profiles()
            print(f"Profile for {username} deleted successfully.")
        else:
            print(f"No profile found for {username}.")

    def list_profiles(self):
        if not self.profiles:
            print("No profiles available.")
            return

        print("Available profiles:")
        for username in self.profiles:
            print(f"- {username}")

if __name__ == "__main__":
    maxcraft = MaxCraft()
    maxcraft.create_profile("john_doe")
    maxcraft.update_profile("john_doe", theme="dark", font_size=14)
    maxcraft.list_profiles()
    maxcraft.delete_profile("john_doe")
    maxcraft.list_profiles()