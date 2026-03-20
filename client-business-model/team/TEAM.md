# AI Team Blueprint

## 目的
個人受託ビジネスを「集客→提案→納品→保守」まで自走化する。

## Team Roles

### 1) Strategist（戦略）
- 週次目標設定
- 優先案件の選定
- KPIの見直し

### 2) Lead Hunter（案件獲得）
- 案件サイトの新着調査
- 応募候補の抽出
- 提案先リスト作成

### 3) Proposal Writer（提案作成）
- 提案文テンプレ生成
- 案件ごとのカスタマイズ
- 見積り文面の整備

### 4) Engineer（実装）
- PoC/自動化スクリプト作成
- Laravel/JSの実装タスク
- AWS構成の最小設計

### 5) Analyst（分析）
- 提案通過率・受注率の計測
- 原因分析
- 改善アクション提案

### 6) Secretary（進行管理）
- 今日のTODO 3つ提示
- 締切管理
- 未完了タスクの可視化

## Daily Cadence
- 朝: Lead Hunter + Proposal Writer
- 昼: Engineer
- 夜: Analyst + Secretary

## KPI
- 週の応募数
- 返信率
- 面談化率
- 受注率
- 月間売上

## 役割別フローチャート

```mermaid
flowchart TD

subgraph S1[① 戦略担当（Strategist）]
A1[週次目標を設定] --> A2[KPI確認]
A2 --> A3[優先課題を決定]
A3 --> A4[今週の実行テーマを確定]
A4 --> A5[各担当に指示]
end

subgraph S2[② 案件獲得担当（Lead Hunter）]
B1[案件サイト/コミュニティを調査] --> B2[候補案件を抽出]
B2 --> B3[条件一致を判定]
B3 -->|Yes| B4[提案作成担当へ連携]
B3 -->|No| B5[除外リストへ]
end

subgraph S3[③ 提案作成担当（Proposal Writer）]
C1[案件情報を受け取る] --> C2[提案テンプレ選択]
C2 --> C3[案件別にカスタマイズ]
C3 --> C4[見積/納期を整える]
C4 --> C5[提出]
C5 --> C6[返信内容を記録]
end

subgraph S4[④ 実装担当（Engineer）]
D1[受注/タスク確定] --> D2[要件を分解]
D2 --> D3[実装（Python/Laravel/JS/AWS）]
D3 --> D4[テスト]
D4 --> D5[納品]
D5 --> D6[運用ドキュメント更新]
end

subgraph S5[⑤ 分析担当（Analyst）]
E1[KPI収集] --> E2[応募率・受注率分析]
E2 --> E3[ボトルネック特定]
E3 --> E4[改善案を1つ決定]
E4 --> E5[戦略担当へ報告]
end

subgraph S6[⑥ 秘書担当（Secretary）]
F1[全タスク一覧を更新] --> F2[期限/優先度を整理]
F2 --> F3[今日のTODO 3つ提示]
F3 --> F4[進捗リマインド]
F4 --> F5[未完了を翌日に繰越]
end

A5 --> B1
B4 --> C1
C6 --> E1
E5 --> A1
A5 --> D1
D6 --> E1
F1 --> A1
F4 --> D3
```
