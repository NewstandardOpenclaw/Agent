# 独自ドメイン取得・設定ガイド（無料寄り運用）

対象: `NewstandardOpenclaw/Kenchiku`（GitHub Pages）

---

## 0. 結論

最小コストで始めるなら、以下の構成が楽です。

- ドメイン管理: **Cloudflare**
- ホスティング: **GitHub Pages**
- SSL: **Cloudflare + GitHub Pagesで自動**

> 実費は通常「ドメイン代のみ」。

---

## 1. ドメイン取得

### 方法A（おすすめ）
Cloudflare Registrar で取得（.com / .jp など）

### 方法B
お名前.com / ムームー / Google Domains移管済みのレジストラで取得し、
DNSだけCloudflareへ向ける

---

## 2. Cloudflareへドメイン追加

1. Cloudflareダッシュボードで「Add a site」
2. ネームサーバー変更指示に従う
3. レジストラ側でネームサーバーをCloudflare指定へ変更

反映に数分〜24h程度かかる場合あり。

---

## 3. GitHub Pages 側設定

対象リポジトリ: `https://github.com/NewstandardOpenclaw/Kenchiku`

1. Settings → Pages
2. Source: `Deploy from a branch`
3. Branch: `main` / `(root)`
4. Custom domain に例: `lp.example.com` を入力して保存
5. `Enforce HTTPS` をON

---

## 4. Cloudflare DNS設定

例: `lp.example.com` を使う場合

- Type: `CNAME`
- Name: `lp`
- Target: `newstandardopenclaw.github.io`
- Proxy status: まずは `DNS only`（灰色雲）推奨

ルートドメイン（`example.com`）を使う場合は、
CNAME Flattening か Aレコード構成を使う。

---

## 5. 動作確認

- `https://lp.example.com` で表示確認
- SSL証明書が有効か確認（鍵マーク）
- `https` 強制リダイレクト確認

---

## 6. つまずきポイント

- 404: Pages反映待ち or CNAME設定ミス
- SSLエラー: 証明書発行待ち（数分〜）
- 古いページ表示: ブラウザキャッシュ

---

## 7. 運用メモ

- GitHub Pages URL（現行）: `https://newstandardopenclaw.github.io/Kenchiku/`
- 独自ドメイン適用後は、QRコードやチラシURLを新URLに差し替える
- OGP画像・faviconは `assets/` 配下で管理

---

## 8. AWSでやる場合（参考）

構成: Route53 + ACM + CloudFront + S3（静的）

- 柔軟性は高い
- ただし設定が増え、CloudFront/Route53で課金が発生しやすい

まずは Cloudflare + Pages で十分。
