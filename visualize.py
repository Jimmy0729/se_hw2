import csv
from collections import defaultdict
from pathlib import Path
import matplotlib.pyplot as plt

DATA_FILE = Path("expenses.csv")

def load_expenses():
    """讀取 A 所產生的 expenses.csv，依分類累加金額。"""
    if not DATA_FILE.exists():
        print("❌ 找不到 expenses.csv，請先讓 A 模組新增幾筆資料。")
        return None

    totals = defaultdict(float)

    with DATA_FILE.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                amount = float(row["amount"])
                category = row["category"]
                totals[category] += amount
            except:
                print("⚠ 跳過一筆無效資料：", row)

    return totals


def plot_pie():
    """依類別畫出圓餅圖。"""
    data = load_expenses()

    if not data:
        print("⚠ 沒有資料可繪製圖表")
        return

    categories = list(data.keys())
    values = list(data.values())

    print("📊 類別金額：")
    for c, v in data.items():
        print(f"  {c}: {v}")

    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=categories, autopct="%1.1f%%")
    plt.title("費用類別分布圖")
    plt.show()


def main():
    print("=== 視覺化模組 (Member B) ===")
    plot_pie()


if __name__ == "__main__":
    main()
