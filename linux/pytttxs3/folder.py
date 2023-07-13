import os
import platform
import subprocess

def openFolderExplorer(folder_path):
    os_name = platform.system()

    if os_name == "Windows":
        subprocess.run(["explorer", os.path.abspath(folder_path)])
    elif os_name == "Linux":
        desktop_env = os.environ.get("XDG_CURRENT_DESKTOP")
        username = os.getenv("SUDO_USER")
        if username is None:  # script was not run with sudo
            username = os.getenv("USER")
        if desktop_env == "KDE":
            subprocess.run(["su", "-c", f"dolphin {os.path.abspath(folder_path)}", username])
        else:
            subprocess.run(["su", "-c", f"xdg-open {os.path.abspath(folder_path)}", username])
    elif os_name == "Darwin": # macOS
        subprocess.run(["open", os.path.abspath(folder_path)])
    else:
        print(f"Unsupported operating system: {os_name}")

# Test the function:
openFolderExplorer("./outputFolder")
