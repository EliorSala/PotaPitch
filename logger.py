import time
import uos

class Logger:
    LEVELS = {
        "D": 10,
        "I": 20,
        "W": 30,
        "E": 40,
        "C": 50
    }

    def __init__(self, level="I", log_dir="logs", retain_days=4):
        self.level = self.LEVELS.get(level.upper(), 20)
        self.log_dir = log_dir
        self.retain_days = retain_days

        # Ensure the log directory exists
        try:
            uos.mkdir(self.log_dir)
        except OSError:
            pass  # Directory already exists

    def cleanup_logs(self):
        current_time = time.time()
        try:
            for filename in uos.listdir(self.log_dir):
                filepath = f"{self.log_dir}/{filename}"
                try:
                    file_time = uos.stat(filepath)[8]  # Last modified time
                    if (current_time - file_time) >= (self.retain_days * 86400):  # 86400 seconds in a day
                        uos.remove(filepath)
                except OSError as e:
                    self.error(f"Failed to remove file: {e}")  # Skip if unable to access file info
        except OSError:
            pass  # Skip if directory doesn't exist or can't be accessed

    def get_log_file(self):
        timestamp = time.localtime()
        date = "{:02}{:02}{:02}".format(timestamp[0] % 100, timestamp[1], timestamp[2])
        return f"{self.log_dir}/log_{date}.txt"

    def log(self, level, message):
        if self.LEVELS[level] >= self.level:
            timestamp = time.localtime()
            raw_time = "{:02}{:02}{:02}{:02}{:02}{:02}".format(
                timestamp[0] % 100, timestamp[1], timestamp[2],
                timestamp[3], timestamp[4], timestamp[5]
            )
            log_message = f"{raw_time}{level}{message}"
            print(log_message)  # Output to console

            log_file = self.get_log_file()
            try:
                with open(log_file, "a") as file:
                    file.write(log_message + "\n")
            except OSError as e:
                print(f"E Failed to write log: {e}")

    def debug(self, message):
        self.log("D", message)

    def info(self, message):
        self.log("I", message)

    def warning(self, message):
        self.log("W", message)

    def error(self, message):
        self.log("E", message)

    def critical(self, message):
        self.log("C", message)


# Example usage
if __name__ == "__main__":
    logger = Logger(level="D", log_dir="logs", retain_days=0)
    logger.debug("Debug msg")
    logger.info("Init")
    logger.warning("Low mem")
    logger.error("File missing")
    logger.critical("Crash")
    logger.cleanup_logs()
