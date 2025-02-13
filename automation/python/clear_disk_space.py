import shutil
import os


def check_disk_space(path="/", threshold=90):
    """this function checks the disk space of the system"""
    usage = shutil.disk_usage(path)
    percent_used = (usage.used / usage.total) * 100
    return percent_used > threshold


def clear_disk_space(path="/var/log", max_files=5):
    """this function clear the overhead disk space"""
    if check_disk_space():
        logs = sorted(
            os.listdir(path), key=lambda f: os.path.getmtime(os.path.join(path, f))
        )
        for log in logs[:-max_files]:
            os.remove(os.path.join(path, log))
        print(f"Cleared old logs from {path}")
    else:
        print("Disk space is within limits.")


if __name__ == "__main__":
    clear_disk_space()
