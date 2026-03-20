# デモ仕様書: CSV業務自動化ミニツール

## 目的
受託提案で使える「業務自動化の実績デモ」を作る。

## 入力
- `input/sales.csv`
  - order_id, customer_id, amount, order_date
- `input/customers.csv`
  - customer_id, name, email

## 処理
1. salesの欠損/不正値を検出（amountが数値でない等）
2. customer_idで結合
3. order_id重複を除去
4. 顧客別売上合計を集計

## 出力
- `output/clean_sales.csv`（整形済み明細）
- `output/customer_summary.csv`（顧客別集計）
- `output/error_log.csv`（不正データログ）

## 成果
- 手作業集計の自動化
- エラーデータを可視化して再現性ある運用へ
