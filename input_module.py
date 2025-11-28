import csv
from pathlib import Path
from datetime import datetime

# 儲存資料的檔案
DATA_FILE = Path("expenses.csv")

# 欄位名稱：要跟 Member B 約好一起使用這個欄位順序
FIELDS = ["date", "amount", "category", "notes"]


def init_file():
    """如果檔案不存在，建立一個含有欄位名稱的 CSV 檔。"""
    if not DATA_FILE.exists():
        with DATA_FILE.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS)
            writer.writeheader()


def input_date():
    """讓使用者輸入日期（格式：YYYY-MM-DD），並做基本檢查。"""
    while True:
        s = input("日期 (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(s, "%Y-%m-%d")
            return s
        except ValueError:
            print("日期格式錯誤，請輸入 YYYY-MM-DD，例如 2025-11-28")


def input_amount():
    """讓使用者輸入金額（正數），並做基本檢查。"""
    while True:
        s = input("金額: ").strip()
        try:
            value = float(s)
            if value <= 0:
                print("金額必須大於 0")
                continue
            return value
        except ValueError:
            print("請輸入數字，例如 120 或 120.5")


def input_category():
    """讓使用者輸入分類（必填）。"""
    while True:
        s = input("分類 (例如 food, transport, entertainment): ").strip()
        if s:
            return s
        print("分類不能為空，請重新輸入。")


def input_notes():
    """讓使用者輸入備註（可留空）。"""
    s = input("備註 (可留空): ").strip()
    return s


def add_expense():
    """引導使用者輸入一筆支出，並寫入 CSV 檔。"""
    print("\n=== 新增支出 ===")
    date = input_date()
    amount = input_amount()
    category = input_category()
    notes = input_notes()

    expense = {
        "date": date,
        "amount": f"{amount:.2f}",  # 統一用兩位小數
        "category": category,
        "notes": notes,
    }

    with DATA_FILE.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writerow(expense)

    print("已儲存：", expense)


def main():
    print("簡易記帳工具 (Member A - Input Module)")
    init_file()

    while True:
        print("\n請選擇：")
        print("1) 新增一筆支出")
        print("2) 離開")
        choice = input("輸入選項編號: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            print("程式結束")
            break
        else:
            print("請輸入 1 或 2")


if __name__ == "__main__":
    main()
