def parse_log_file(input_file, output_file):
    levels = {
        "D": "DEBUG",
        "I": "INFO",
        "W": "WARNING",
        "E": "ERROR",
        "C": "CRITICAL"
    }

    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            line = line.strip()
            timestamp = line[:12]
            level = line[12]
            message = line[13:]

            year = "20" + timestamp[:2]
            month = timestamp[2:4]
            day = timestamp[4:6]
            hour = timestamp[6:8]
            minute = timestamp[8:10]
            second = timestamp[10:12]

            formatted_time = f"{year}-{month}-{day} {hour}:{minute}:{second}"
            formatted_level = levels.get(level, "UNKNOWN")
            formatted_line = f"[{formatted_time}] {formatted_level}: {message}"
            outfile.write(formatted_line + "\n")
            print(formatted_line)  # Optional: Print to console


# Example usage
parse_log_file("./log_210101.txt", "log_210101.parsed.txt")
parse_log_file("./log_210111.txt", "log_210111.parsed.txt")
parse_log_file("./log_210112.txt", "log_210112.parsed.txt")
parse_log_file("./log_210113.txt", "log_210113.parsed.txt")
parse_log_file("./log_210114.txt", "log_210114.parsed.txt")
parse_log_file("./log_210124.txt", "log_210124.parsed.txt")
parse_log_file("./log_210125.txt", "log_210125.parsed.txt")
parse_log_file("./log_210126.txt", "log_210126.parsed.txt")
parse_log_file("./log_210127.txt", "log_210127.parsed.txt")
# parse_log_file("./log_210108.txt", "log_210108.parsed.txt")
