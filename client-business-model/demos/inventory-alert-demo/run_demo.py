import csv
from pathlib import Path

base = Path(__file__).parent
input_path = base / "input" / "inventory.csv"
output_dir = base / "output"
output_dir.mkdir(exist_ok=True)

alerts = []
rows = list(csv.DictReader(input_path.open(encoding="utf-8")))

for r in rows:
    stock_qty = int(r["stock_qty"])
    reorder_point = int(r["reorder_point"])

    if stock_qty <= reorder_point:
        level = "critical" if stock_qty <= max(1, reorder_point // 2) else "warn"
        alerts.append(
            {
                "sku": r["sku"],
                "product_name": r["product_name"],
                "stock_qty": stock_qty,
                "reorder_point": reorder_point,
                "alert_level": level,
                "supplier_email": r["supplier_email"],
            }
        )

alerts_path = output_dir / "low_stock_alerts.csv"
with alerts_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(
        f,
        fieldnames=[
            "sku",
            "product_name",
            "stock_qty",
            "reorder_point",
            "alert_level",
            "supplier_email",
        ],
    )
    w.writeheader()
    w.writerows(alerts)

summary_path = output_dir / "summary.txt"
critical_count = sum(1 for a in alerts if a["alert_level"] == "critical")
warn_count = sum(1 for a in alerts if a["alert_level"] == "warn")
summary_path.write_text(
    f"total_items={len(rows)}\nalerts={len(alerts)}\ncritical={critical_count}\nwarn={warn_count}\n",
    encoding="utf-8",
)

print(f"done: {alerts_path}")
print(summary_path.read_text(encoding='utf-8'))
