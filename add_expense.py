import csv
import os

CSV_FILE = "expenses.csv"

def add_expense():
    date = input("輸入日期 (YYYY-MM-DD): ")
    category = input("輸入類別: ")
    amount = input("輸入金額: ")

    # CSV 是否存在，不存在就建立表頭
    file_exists = os.path.exists(CSV_FILE)

    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["date", "category", "amount"])

        writer.writerow([date, category, amount])

    print("✔ 已新增一筆資料到 expenses.csv")

if __name__ == "__main__":
    add_expense()
