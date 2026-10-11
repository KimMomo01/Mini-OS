# Individual Contribution Report

- **Student Name:** Patrick Kim Villaruz
- **Group Name:** MiniOS
- **Assigned Role:** Solo Developer (Project Leader / CLI / File / Process / Memory / User / System Developer)

## 1. Project Contributions
As the sole developer for MiniOS, I designed, implemented, and tested the entire command-line operating system simulator from scratch in Python (`main.py`). My specific contributions include:
- **Core Shell & CLI:** Built the interactive command-line interface loop (`MiniOS>`) with robust error handling to catch unknown commands and missing arguments without crashing.
- **User Authentication:** Implemented secure login verification for `admin` and `student` accounts, along with the `whoami` and `systeminfo` commands.
- **Virtual File System:** Developed commands for listing directories (`dir`), creating directories (`mkdir`), creating files (`create`), reading files (`read`), and deleting files (`delete`).
- **Process Management:** Created simulated process execution (`run`) and termination (`kill`) tracked via a dynamic process ID (PID) table.
- **Memory Management:** Implemented resource tracking against a fixed 1024 MB pool, supporting `memory`, `allocate`, and `free` commands.
- **Documentation & Testing:** Drafted the project README, User Manual, Technical Documentation, captured terminal execution screenshots, and recorded the final demo video.

## 2. What I Learned
Through this project, I gained practical, hands-on understanding of core Operating Systems concepts:
- How shell control loops parse user input, manage execution states, and handle syntax exceptions gracefully.
- The mechanics behind process lifecycles (creation, tracking, and termination) using in-memory data structures.
- How memory allocation and deallocation are tracked and simulated in a constrained software environment.