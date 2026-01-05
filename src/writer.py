import os
import csv
from config import CSV_FILE


def get_next_queue_number():
    if not os.path.exists(CSV_FILE):
        return 1

    with open(CSV_FILE, newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)

        if len(rows) <= 1:
            return 1

        try:
            return int(rows[-1][1]) + 1
        except:
            return len(rows)


def write_header_if_needed(writer, is_new_file):
    if is_new_file:
        writer.writerow(["", "Queue", "Name", "Card", "Birthdate", "Phone", "Date"])
