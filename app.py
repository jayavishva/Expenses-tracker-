from flask import Flask, render_template, request, jsonify
import csv
import os

app = Flask(__name__)
CSV_FILE = os.path.join(os.path.dirname(__file__), "expenses.csv")


def read_expenses():
    expenses = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for index, row in enumerate(reader):
                if len(row) >= 2:
                    try:
                        expenses.append({
                            "id": index,
                            "item": row[0],
                            "amount": float(row[1])
                        })
                    except ValueError:
                        continue
    return expenses


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/expenses", methods=["GET"])
def get_expenses():
    expenses = read_expenses()
    total = sum(expense["amount"] for expense in expenses)
    return jsonify({"expenses": expenses, "total": total})


@app.route("/api/expenses", methods=["POST"])
def add_expense():
    data = request.get_json(silent=True) or {}
    item = str(data.get("item", "")).strip()
    amount = data.get("amount")

    if not item:
        return jsonify({"error": "Item is required"}), 400

    try:
        amount = float(amount)
    except (TypeError, ValueError):
        return jsonify({"error": "Amount must be a valid number"}), 400

    if amount <= 0:
        return jsonify({"error": "Amount must be greater than 0"}), 400

    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow([item, amount])

    return jsonify({"message": "Expense added successfully"}), 201


@app.route("/api/expenses/<int:expense_id>", methods=["DELETE"])
def delete_expense(expense_id):
    expenses = read_expenses()

    if not any(expense["id"] == expense_id for expense in expenses):
        return jsonify({"error": "Expense not found"}), 404

    remaining = [expense for expense in expenses if expense["id"] != expense_id]

    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for expense in remaining:
            writer.writerow([expense["item"], expense["amount"]])

    return jsonify({"message": "Expense deleted successfully"})


if __name__ == "__main__":
    app.run(debug=True)
