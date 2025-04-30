import re
from typing import List, Dict

class LogProcessor:
    def __init__(self, input_file: str):
        self.input_file = input_file
        self.logs = []

    def read_logs(self) -> None:
        with open(self.input_file, 'r') as file:
            self.logs = file.readlines()
        print("[+] Logs loaded successfully.")

    def filter_logs(self, keywords: List[str]) -> None:
        self.logs = [log for log in self.logs if any(k in log for k in keywords)]
        print(f"[+] Filtered logs with keywords {keywords}.")

    def sanitize_logs(self) -> None:
        sanitized = []
        for log in self.logs:
            log = re.sub(r'\b\d{1,3}(?:\.\d{1,3}){3}\b', '[REDACTED_IP]', log)
            log = re.sub(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', '[REDACTED_EMAIL]', log)
            sanitized.append(log)
        self.logs = sanitized
        print("[+] Sanitized IPs and emails.")

    def lowercase_logs(self) -> None:
        self.logs = [log.lower() for log in self.logs]
        print("[+] Converted logs to lowercase.")

    def count_log_levels(self) -> Dict[str, int]:
        summary = {"error": 0, "warning": 0}
        for log in self.logs:
            if "error" in log:
                summary["error"] += 1
            elif "warning" in log:
                summary["warning"] += 1
        print("[+] Counted log levels.")
        return summary

    def save_logs(self, output_file: str) -> None:
        with open(output_file, 'w') as file:
            file.writelines(self.logs)
        print(f"[+] Logs saved to {output_file}.")


if __name__ == "__main__":
    processor = LogProcessor("app.log")
    processor.read_logs()
    processor.filter_logs(["ERROR", "WARNING"])
    processor.sanitize_logs()
    processor.lowercase_logs()
    summary = processor.count_log_levels()
    processor.save_logs("processed_logs.txt")

    print("\n Log Summary:")
    for level, count in summary.items():
        print(f"{level.upper()}: {count}")
