import os
from datetime import datetime

OS_NAME = "MiniOS Nova"
VERSION = "1.0"
TOTAL_MEMORY = 1024  # MB

# User database
USERS = {
    "admin": "admin123",
    "student": "password123"
}
current_user = None

# Virtual File System
virtual_dirs = ["Documents", "Downloads"]
virtual_files = {
    "notes.txt": "Operating Systems Final Project"
}

# Process Simulation
processes = {}
next_pid = 1

# Memory Simulation
used_memory = 256  # Initial baseline used memory in MB

def show_banner():
    print("=" * 40)
    print(f"       {OS_NAME} v{VERSION}")
    print("=" * 40)

def login():
    global current_user
    print("\n========================================")
    print("           MiniOS Login")
    print("========================================")
    
    while True:
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        
        if username in USERS and USERS[username] == password:
            current_user = username
            print(f"\nLogin successful. Welcome, {username}!\n")
            break
        else:
            print("Invalid username or password. Please try again.\n")

def main():
    show_banner()
    login()

    global next_pid, used_memory

    while True:
        command_input = input(f"MiniOS> ").strip()
        if not command_input:
            continue

        parts = command_input.split(maxsplit=1)
        command = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""

        if command == "help":
            print("\nAvailable Commands:")
            print("  help                 Show available commands")
            print("  clear                Clear the screen")
            print("  date                 Show current date")
            print("  time                 Show current time")
            print("  whoami               Show current user")
            print("  systeminfo           Show system information")
            print("  dir                  List files and directories")
            print("  mkdir <dir>          Create a directory")
            print("  create <file>        Create a file")
            print("  read <file>          Read file content")
            print("  delete <file>        Delete a file")
            print("  process              List running processes")
            print("  run <name>           Start a simulated process")
            print("  kill <pid>           Terminate a process by PID")
            print("  memory               Display memory status")
            print("  allocate <MB>        Allocate simulated memory")
            print("  free <MB>            Release simulated memory")
            print("  exit                 Shut down MiniOS\n")

        elif command == "clear":
            os.system("cls" if os.name == "nt" else "clear")

        elif command == "date":
            print(datetime.now().strftime("%Y-%m-%d"))

        elif command == "time":
            print(datetime.now().strftime("%H:%M:%S"))

        elif command == "whoami":
            print(f"Current User: {current_user}")

        elif command == "systeminfo":
            print("========================================")
            print("          SYSTEM INFORMATION")
            print("========================================")
            print(f"OS Name:      {OS_NAME}")
            print(f"Version:      {VERSION}")
            print("Architecture: 64-bit")
            print("CPU:          Virtual CPU")
            print(f"Memory:       {TOTAL_MEMORY} MB")
            print(f"User:         {current_user}")
            print("========================================")

        elif command == "dir":
            print("\nDirectory of MiniOS:")
            for d in virtual_dirs:
                print(f"  <DIR>  {d}")
            for f in virtual_files:
                print(f"         {f}")
            print()

        elif command == "mkdir":
            if not args:
                print("Error: Missing directory name. Syntax: mkdir <dirname>")
            elif args in virtual_dirs:
                print(f"Error: Directory '{args}' already exists.")
            else:
                virtual_dirs.append(args)
                print("Directory created.")

        elif command == "create":
            if not args:
                print("Error: Missing file name. Syntax: create <filename>")
            elif args in virtual_files:
                print(f"Error: File '{args}' already exists.")
            else:
                virtual_files[args] = ""
                print("File created.")

        elif command == "read":
            if not args:
                print("Error: Missing file name. Syntax: read <filename>")
            elif args in virtual_files:
                print(virtual_files[args])
            else:
                print("Error: File does not exist.")

        elif command == "delete":
            if not args:
                print("Error: Missing file name. Syntax: delete <filename>")
            elif args in virtual_files:
                del virtual_files[args]
                print("File deleted.")
            else:
                print("Error: File does not exist.")

        elif command == "process":
            print("\nPID\tNAME\t\tSTATUS")
            print("-" * 35)
            if not processes:
                print("No active processes.")
            for pid, pinfo in processes.items():
                print(f"{pid}\t{pinfo['name']}\t\t{pinfo['status']}")
            print()

        elif command == "run":
            if not args:
                print("Error: Missing process name. Syntax: run <process_name>")
            else:
                pid = next_pid
                processes[pid] = {"name": args, "status": "RUNNING"}
                next_pid += 1
                print(f"Process started.\nPID: {pid}\nName: {args}\nStatus: RUNNING")

        elif command == "kill":
            if not args.isdigit():
                print("Error: Invalid PID. Syntax: kill <PID>")
            else:
                pid = int(args)
                if pid in processes:
                    del processes[pid]
                    print(f"Process {pid} terminated.")
                else:
                    print("Error: Process does not exist.")

        elif command == "memory":
            free_mem = TOTAL_MEMORY - used_memory
            print("\nMemory Status")
            print("------------------------")
            print(f"Total Memory: {TOTAL_MEMORY} MB")
            print(f"Used Memory:  {used_memory} MB")
            print(f"Free Memory:  {free_mem} MB\n")

        elif command == "allocate":
            if not args.isdigit():
                print("Error: Specify valid amount in MB. Syntax: allocate <MB>")
            else:
                amount = int(args)
                if used_memory + amount > TOTAL_MEMORY:
                    print("Error: Not enough free memory to allocate.")
                else:
                    used_memory += amount
                    print(f"{amount} MB allocated.")

        elif command == "free":
            if not args.isdigit():
                print("Error: Specify valid amount in MB. Syntax: free <MB>")
            else:
                amount = int(args)
                if used_memory - amount < 0:
                    print("Error: Cannot free more memory than currently used.")
                else:
                    used_memory -= amount
                    print(f"{amount} MB released.")

        elif command == "exit":
            print("Shutting down MiniOS...")
            print("Goodbye!")
            break

        else:
            print("Unknown command. Type 'help' to see the available commands.")

if __name__ == "__main__":
    main()