# LinkNest MVP コード解説（レビュー用）

このドキュメントは `linknest-mvp` の実装意図を短く把握するためのメモです。

## 構成
- `index.html`: 公開プロフィールページ
- `admin.html`: 編集ページ（localStorage保存）
- `data.sample.json`: 初期データ
- `README.md`: 使い方

## 1) index.html のポイント

### 目的
訪問者向けにリンク一覧を表示する。

### 主要ロジック
1. 起動時に `localStorage('linknest:data')` を読む
2. なければ `data.sample.json` を読み込む
3. `render(data)` でプロフィール・リンク一覧をDOMに描画

### 関数
- `loadSample()`
  - `fetch('./data.sample.json')` でサンプルJSON取得
- `render(data)`
  - `profile` を画面に反映
  - `links` を `enabled !== false` でフィルタしてカード生成
- `init()`
  - localStorage優先でデータ解決し、描画

### 補足
- 外部リンクは `target=_blank` + `rel=noopener noreferrer` を指定（最低限の安全配慮）

## 2) admin.html のポイント

### 目的
プロフィールとリンクをノーコードで編集する。

### 主要ロジック
- 入力フォームで `profile` を編集
- `links` は JSON テキストエリアで編集
- Save時に `localStorage` へ保存
- Export/Import でJSONのバックアップと復元

### 関数/イベント
- `loadData()`
  - localStorage優先でフォームへ反映
- `save.onclick`
  - フォーム値 + links(JSON.parse) を保存
- `export.onclick`
  - BlobでJSONをダウンロード
- `importFile.onchange`
  - JSON妥当性を検証して保存

## 3) data.sample.json

### 役割
- 初期表示用のデータ
- localStorage未設定時のフォールバック

## 現状の制約（MVP）
- 認証なし（誰でも管理画面を開ける）
- サーバー保存なし（ブラウザ依存）
- クリック分析なし

## 本番化の次ステップ
1. 認証追加（メール/パスワード or OAuth）
2. DB保存（users / profiles / links）
3. クリック計測（link_clicks）
4. slug公開URL（`/u/{slug}`）
5. UIテーマ拡張
