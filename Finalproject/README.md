# MiniOS Nova

A simple command-line operating system simulator built in Python to demonstrate core Operating Systems concepts.

## Project Description
MiniOS Nova is a command-line interface (CLI) simulator running through Windows Command Prompt (CMD). It demonstrates basic operating system functionalities including user authentication, file management, process simulation, memory management, and robust error handling.

## Features
- **Command-Line Interface:** Custom command prompt (`MiniOS>`) with an interactive shell.
- **User Management:** Secure login system (`admin` and `student` accounts) and `whoami` command.
- **File Management:** Commands to list directories (`dir`), create folders (`mkdir`), create files (`create`), read files (`read`), and delete files (`delete`).
- **Process Management:** Simulate running processes (`run`), view process status (`process`), and terminate processes (`kill`).
- **Memory Management:** Track total, used, and free memory (`memory`), allocate memory (`allocate`), and release memory (`free`).
- **System Information:** View system details (`systeminfo`).
- **Error Handling:** Gracefully handles unknown commands and missing files/processes without crashing.

## Requirements
- Python 3.x
- Windows Command Prompt (CMD)

## How to Run
1. Clone or download this repository.
2. Open Windows Command Prompt (CMD) or your terminal.
3. Navigate to the project folder:
   ```bash
   cd path/to/MiniOS