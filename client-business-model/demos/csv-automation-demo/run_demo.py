import csv
from pathlib import Path

BASE = Path(__file__).parent
inp = BASE / "input"
out = BASE / "output"
out.mkdir(exist_ok=True)

sales = list(csv.DictReader((inp / "sales.csv").open(encoding="utf-8")))
customers = {r["customer_id"]: r for r in csv.DictReader((inp / "customers.csv").open(encoding="utf-8"))}

seen_order = set()
clean_rows, errors = [], []

for r in sales:
    order_id = r.get("order_id", "")
    cid = r.get("customer_id", "")
    amt_raw = r.get("amount", "")

    if order_id in seen_order:
        continue
    seen_order.add(order_id)

    try:
        amt = float(amt_raw)
    except ValueError:
        errors.append({"order_id": order_id, "reason": "invalid amount", "value": amt_raw})
        continue

    if cid not in customers:
        errors.append({"order_id": order_id, "reason": "customer not found", "value": cid})
        continue

    c = customers[cid]
    clean_rows.append({
        "order_id": order_id,
        "customer_id": cid,
        "name": c["name"],
        "email": c["email"],
        "amount": amt,
        "order_date": r.get("order_date", ""),
    })

summary = {}
for r in clean_rows:
    k = r["customer_id"]
    summary.setdefault(k, {"customer_id": k, "name": r["name"], "total_amount": 0.0, "order_count": 0})
    summary[k]["total_amount"] += float(r["amount"])
    summary[k]["order_count"] += 1

with (out / "clean_sales.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["order_id", "customer_id", "name", "email", "amount", "order_date"])
    w.writeheader(); w.writerows(clean_rows)

with (out / "customer_summary.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["customer_id", "name", "total_amount", "order_count"])
    w.writeheader(); w.writerows(summary.values())

with (out / "error_log.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["order_id", "reason", "value"])
    w.writeheader(); w.writerows(errors)

print("done")
