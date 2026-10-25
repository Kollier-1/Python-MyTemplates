"""
Module Name: System Command Executor
Description: Executes operating system commands using the subprocess module and displays the command output or error message.
Author: Kollier
"""

import subprocess

def execute_command(command: str) -> None:
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            encoding="cp850",
            errors="replace",
            timeout=30
        )

        if result.returncode == 0:
            print("Command executed successfully:\n")
            print(result.stdout)
        else:
            print(f"Command failed with exit code {result.returncode}:")
            print(result.stderr)

    except subprocess.TimeoutExpired:
        print("Error: The command exceeded the 30-second time limit.")

    except OSError as error:
        print(f"Error executing command: {error}")

if __name__ == "__main__":
    command = input("Enter the system command to execute: ").strip()

    if command:
        execute_command(command)
    else:
        print("Error: The command cannot be empty.")