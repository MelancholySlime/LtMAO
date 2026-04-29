import cProfile, pstats
import os.path
import winreg

def get_desktop_path():
    # Path to the registry key containing user shell folder locations
    registry_key_path = r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders"
    
    try:
        # Open the key in the HKEY_CURRENT_USER hive
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, registry_key_path) as key:
            # Query the 'Desktop' value; [0] retrieves the data string
            desktop_path, reg_type = winreg.QueryValueEx(key, "Desktop")
            
            # If the path contains environment variables like %USERPROFILE%, expand them
            return winreg.ExpandEnvironmentStrings(desktop_path)
    except OSError as e:
        print(f"Error accessing registry: {e}")
        return None


def db(func):
    with cProfile.Profile() as profile:
        func()
    stats = pstats.Stats(profile)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats(20)

def test3():
    print(get_desktop_path())
    
db(test3)