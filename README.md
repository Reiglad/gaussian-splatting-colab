# COLMAP SfM + 3D Gaussian Splatting on Google Colab

Google Colab（無料 T4 GPU）上で COLMAP による Structure from Motion → 3D Gaussian Splatting を実行するパイプラインです。

[![01_setup](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/reiglad/gaussian-splatting-colab/blob/main/notebooks/01_setup.ipynb)
[![02_colmap_sfm](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/reiglad/gaussian-splatting-colab/blob/main/notebooks/02_colmap_sfm.ipynb)
[![03_train_3dgs](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/reiglad/gaussian-splatting-colab/blob/main/notebooks/03_train_3dgs.ipynb)

## 特徴

- **完全無料**: Google Colab 無料枠 + Google Drive で動作
- **3 ステップ構成**: setup → SfM → 学習
- **SuperSplat 対応**: 出力 `.ply` をブラウザで即閲覧可能

## 必要なもの

- Google アカウント（Colab + Drive）
- 撮影画像（20〜200 枚の JPG/PNG）
- ブラウザ（SuperSplat 閲覧用）

## クイックスタート

### Step 0: Google Drive の準備

`MyDrive/gaussian_splatting/input/<scene_name>/images/` に画像ファイル（JPG / PNG）を配置してください。

### Step 1: 環境構築

`notebooks/01_setup.ipynb` を Google Colab で開き、ランタイムを **T4 GPU** に設定して全セル実行。

### Step 2: SfM（COLMAP）

`notebooks/02_colmap_sfm.ipynb` の先頭セルで `SCENE_NAME` を設定して全セル実行。

### Step 3: 3DGS 学習

`notebooks/03_train_3dgs.ipynb` の先頭セルで `SCENE_NAME` を設定して全セル実行。
T4 GPU で **約 45〜90 分**（30000 iter）。

### Step 4: 閲覧

1. [SuperSplat](https://playcanvas.com/supersplat/editor) を開く
2. `[Open]` → `point_cloud.ply` を選択

## Drive フォルダ構成

```
MyDrive/gaussian_splatting/
├── input/
│   └── <scene_name>/
│       └── images/         ← JPG/PNG を置く
└── output/
    └── <scene_name>/
        ├── colmap.db
        ├── sparse/0/       ← COLMAP sparse 出力
        ├── images/         ← コピーされた画像
        └── point_cloud/
            └── iteration_30000/
                └── point_cloud.ply   ← SuperSplat で開く
```

## トラブルシューティング

[docs/troubleshooting.md](docs/troubleshooting.md) を参照してください。

## 使用ライブラリ

- [pycolmap](https://github.com/colmap/pycolmap) — COLMAP Python バインディング
- [gaussian-splatting](https://github.com/graphdeco-inria/gaussian-splatting) — 3DGS オリジナル実装 (Kerbl et al., 2023)
- [SuperSplat](https://playcanvas.com/supersplat/editor) — PLY ビューワー
