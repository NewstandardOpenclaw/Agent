import json
import os
import csv
from pathlib import Path
from urllib.request import Request, urlopen

BASE = Path(__file__).parent
ALERTS_CSV = BASE / "output" / "low_stock_alerts.csv"
MOCK_OUT = BASE / "output" / "slack_payload.json"


def build_message(rows):
    if not rows:
        return {"text": "✅ 在庫アラートはありません。"}

    lines = ["🚨 *在庫アラート*", f"対象件数: {len(rows)}"]
    for r in rows[:10]:
        lines.append(
            f"- {r['product_name']} ({r['sku']}): 在庫 {r['stock_qty']} / 発注点 {r['reorder_point']} [{r['alert_level']}]"
        )

    return {"text": "\n".join(lines)}


def main():
    if not ALERTS_CSV.exists():
        raise SystemExit(f"alerts csv not found: {ALERTS_CSV}")

    rows = list(csv.DictReader(ALERTS_CSV.open(encoding="utf-8")))
    payload = build_message(rows)

    webhook = os.getenv("SLACK_WEBHOOK_URL", "").strip()
    if webhook:
        req = Request(
            webhook,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urlopen(req, timeout=10) as res:
            print(f"posted to slack: status={getattr(res, 'status', 'unknown')}")
    else:
        MOCK_OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"mock payload saved: {MOCK_OUT}")


if __name__ == "__main__":
    main()
