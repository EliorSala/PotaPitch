import re
import matplotlib.pyplot as plt
from datetime import datetime

# File path
file_path = 'log_210101.parsed.txt'
file_path2 = 'log_210102.parsed.txt'

# Regular expression to parse logs
log_pattern = re.compile(r'\[(.*?)\] INFO: (.*?)$')

def parse_logs(file_path):
    """Parses the log file and returns a dictionary with timestamps and their corresponding values."""
    logs = []  # List of tuples (timestamp, value)
    with open(file_path, 'r') as file:
        for line in file:
            match = log_pattern.match(line.strip())
            if match:
                timestamp_str, value_str = match.groups()
                try:
                    timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
                    value = float(value_str)
                    logs.append((timestamp, value))
                except ValueError:
                    pass
    return logs[::2]

def plot_logs(logs):
    """Plots the logs as a single graph with time on the x-axis and values on the y-axis."""
    if not logs:
        print("No logs to plot.")
        return

    timestamps, values = zip(*logs)

    plt.figure(figsize=(12, 6))
    plt.plot(timestamps, values, marker='o', linestyle='-', label='Log Values')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('Log Values Over Time')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()


# Main execution
if __name__ == "__main__":
    logs = parse_logs(file_path)
    logs2 = parse_logs(file_path2)
    plot_logs(logs + logs2)
