# 仕様書: 在庫アラート自動化デモ

## 目的
在庫切れリスクを早期検知し、担当者が即対応できる状態を作る。

## 入力
- sku
- product_name
- stock_qty
- reorder_point
- supplier_email

## 処理
1. 在庫CSVを読み込む
2. `stock_qty <= reorder_point` を満たす商品を抽出
3. 緊急度（critical/warn）を付与
4. アラート一覧CSVを出力

## 出力
- low_stock_alerts.csv
- summary.txt
