# Inventory Alert Automation Demo

在庫CSVを読み込み、しきい値以下の商品を抽出してアラート用CSVを生成するデモです。

## 実行
python3 run_demo.py

## Slack通知（疑似/本番）
1. まず集計を実行
   - `python3 run_demo.py`
2. 通知を作成
   - 疑似通知（ファイル出力）: `python3 notify_slack.py`
   - 本番通知（Webhook）: `SLACK_WEBHOOK_URL=... python3 notify_slack.py`

## 入力
- input/inventory.csv

## 出力
- output/low_stock_alerts.csv
- output/summary.txt
- output/slack_payload.json（Webhook未設定時）
