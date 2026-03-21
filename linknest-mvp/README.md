# LinkNest MVP

Lit.link系のユースケースを参考にした、**独自デザインのリンクまとめMVP**。

## 特徴
- 公開ページ: `index.html`
- 編集ページ: `admin.html`（ローカル保存）
- データ形式: `data.sample.json`（Import/Export可）
- 依存なし（静的HTML/CSS/JSのみ）

## 使い方
1. `index.html` を開く
2. `admin.html` でプロフィール/リンク編集
3. Saveするとブラウザに保存される
4. ExportでJSONバックアップ

## 注意
- MVPのため認証は未実装
- 本番化時はサーバー側保存・認証・分析機能を追加
