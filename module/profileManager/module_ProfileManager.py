import os
from cryptography.fernet import Fernet
from .module_ProfileDataManager import ProfileDataManager
from .module_ProfileDirectoryManager import ProfileDirectoryManager
from .module_Errorhandling import ErrorHandling


class ProfileManager:
    def __init__(self):
        self._profile_directory_manager = ProfileDirectoryManager()
        self._profile_data_manager = ProfileDataManager()
        self._error_handler = ErrorHandling()

    def create_profile(self, profile_name, email, password, key):
        try:
            if not self._error_handler.validate_profile_name(profile_name):
                raise ValueError("Invalid profile name. Profile name should only contain alphanumeric characters and underscores.")

            if not self._error_handler.validate_email(email):
                raise ValueError("Invalid email format.")

            # Create profile using both managers
            self._profile_directory_manager.create_profile(profile_name)
            self._profile_data_manager.create_profile(profile_name, email, password, key)
            return self._error_handler.response_msg(f"Profile '{profile_name}' created successfully.")
        except Exception as e:
            return self._error_handler.response_msg(f"Error creating profile '{profile_name}': {str(e)}")

    def update_profile(self, old_profile_name, new_profile_name=None, email=None, password=None):
        try:
            if new_profile_name and not self._error_handler.validate_profile_name(new_profile_name):
                print("error")
                raise ValueError("Invalid profile name. Profile name should only contain alphanumeric characters and underscores.")

            if email and not self._error_handler.validate_email(email):
                raise ValueError("Invalid email format.")
                print("error")

            # Update profile using both managers
            self._profile_data_manager.update_profile(old_profile_name, new_profile_name, email, password)
            self._profile_directory_manager.rename_profile(old_profile_name, new_profile_name)
            print("success")
            return self._error_handler.response_msg(f"Profile '{old_profile_name}' updated successfully.")
        except Exception as e:
            return self._error_handler.response_msg(f"Error updating profile '{old_profile_name}': {str(e)}")

    def delete_profile(self, profile_name):
        try:
            # Delete profile using both managers
            self._profile_data_manager.delete_profile(profile_name)
            self._profile_directory_manager.delete_profile(profile_name)
            return self._error_handler.response_msg(f"Profile '{profile_name}' deleted successfully.")
        except Exception as e:
            return self._error_handler.response_msg(f"Error deleting profile '{profile_name}': {str(e)}")

    def get_all_profiles(self):
        try:
            # Get all profiles using binary manager
            result = self._profile_data_manager.get_all_profiles()
            return self._error_handler.response_msg("All profiles retrieved successfully.", data=result)
        except Exception as e:
            return self._error_handler.response_msg(f"Error getting all profiles: {str(e)}")
    def initial_task(self, tasks):
        try:
            result = self._profile_data_manager.initial_task(tasks)
            return self._error_handler.response_msg("All user tasks retrieved successfully.", data=result)

        except Exception as e:
            return self._error_handler.response_msg(f"Error getting initail user tasks: {str(e)}")

# Example usage: