import os
import subprocess
import platform
import datetime

LOG_FILE = "pc_support_log.txt"

def log(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.datetime.now()}: {message}\n")

def cleanup_temp_files():
    temp_dirs = [r"C:\Windows\Temp", os.environ.get("TEMP", "")]
    for temp_dir in temp_dirs:
        if os.path.exists(temp_dir):
            try:
                for root, dirs, files in os.walk(temp_dir):
                    for file in files:
                        try:
                            os.remove(os.path.join(root, file))
                        except Exception as e:
                            log(f"Failed to remove {file}: {e}")
                log(f"Cleaned temp files in {temp_dir}")
            except Exception as e:
                log(f"Error cleaning {temp_dir}: {e}")

def collect_software_info():
    try:
        if platform.system() == "Windows":
            result = subprocess.run(
                ["wmic", "product", "get", "name,version"],
                capture_output=True, text=True, shell=True
            )
            log("Installed Applications:\n" + result.stdout[:1000])  # Log first 1000 chars for brevity
        else:
            log("Software info collection not implemented for this OS.")
    except Exception as e:
        log(f"Error collecting software info: {e}")

def main():
    log("=== PC Support Toolkit Run ===")
    cleanup_temp_files()
    collect_software_info()
    log("=== Toolkit Finished ===")

if __name__ == "__main__":
    main()