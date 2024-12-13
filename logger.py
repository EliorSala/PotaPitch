import time
import os


class Logger:
    LEVELS = {
        "D": 10,
        "I": 20,
        "W": 30,
        "E": 40,
        "C": 50
    }

    def __init__(self, level="I", log_dir="logs", retain_days=7):
        self.level = self.LEVELS.get(level.upper(), 20)
        self.log_dir = log_dir
        self.retain_days = retain_days
        os.makedirs(log_dir, exist_ok=True)

    def cleanup_logs(self):
        current_time = time.time()
        for filename in os.listdir(self.log_dir):
            filepath = os.path.join(self.log_dir, filename)
            if os.path.isfile(filepath):
                file_time = os.path.getmtime(filepath)
                if (current_time - file_time) >= (self.retain_days * 86400):  # 86400 seconds in a day
                    os.remove(filepath)

    def get_log_file(self):
        timestamp = time.localtime()
        date = "{:02}{:02}{:02}".format(timestamp[0] % 100, timestamp[1], timestamp[2])
        return os.path.join(self.log_dir, f"log_{date}.txt")

    def log(self, level, message):
        if self.LEVELS[level] >= self.level:
            timestamp = time.localtime()
            raw_time = "{:02}{:02}{:02}{:02}{:02}{:02}".format(
                timestamp[0] % 100, timestamp[1], timestamp[2],
                timestamp[3], timestamp[4], timestamp[5]
            )
            log_message = f"{raw_time}{level}{message}"
            print(log_message)
            log_file = self.get_log_file()
            try:
                with open(log_file, "a") as file:
                    file.write(log_message + "\n")
            except Exception as e:
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
