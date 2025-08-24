
import datetime
import os

def create_file_with_timestamp(directory="."):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"file_{timestamp}.txt"
    filepath = os.path.join(directory, filename)
    with open(filepath, "w") as f:
        f.write(f"Created at {timestamp}\n")
    print(f"File created: {filepath}")

if __name__ == "__main__":
    create_file_with_timestamp()
