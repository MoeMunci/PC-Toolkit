# PC Support Toolkit

A simple Python script to automate basic helpdesk tasks on Windows PCs.  
It performs disk cleanup, collects installed software information, and generates a log file for support purposes.

## Features

- Cleans up temporary files in `C:\Windows\Temp` and the user's `%TEMP%` directory.
- Collects a list of installed applications using Windows Management Instrumentation (`wmic`).
- Logs all actions and results to `pc_support_log.txt`.

## Requirements

- Python 3.x
- Windows OS
- Administrator privileges (recommended for full cleanup)

## Usage

1. **Clone or download this repository.**
2. **Open Command Prompt as Administrator.**
3. **Run the script:**
   ```sh
   python Tool.py
   ```
4. **Check the `pc_support_log.txt` file** for logs and results.

## Notes

- The script is designed for Windows.  
- `wmic` may be deprecated on some Windows versions. For modern systems, consider updating the script to use PowerShell for software inventory.
- For best results, run as administrator.

## License

MIT License