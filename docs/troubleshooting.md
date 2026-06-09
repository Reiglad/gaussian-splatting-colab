# Troubleshooting

## simple-knn ビルドエラー（CUDA 12 環境）

**症状**: `error: identifier "__float128" is undefined`

**対処**:

    pip install cccl
    pip install submodules/simple-knn

---

## `incremental_mapping` が空を返す

**症状**: `再構成に失敗しました` エラー

**原因と対処**:
- 画像の重複が不足 → 隣接フレームで 30〜60% 重複するよう撮影
- 画像数が少ない → 30 枚以上推奨
- 動画から抽出した場合 → 1 秒 1 フレーム程度に間引く
- `max_num_features` を 16384 に増やす（`02_colmap_sfm.ipynb` Cell 4 を編集）

---

## 学習中に OOM（Out of Memory）

**症状**: `RuntimeError: CUDA out of memory`

**対処** (`03_train_3dgs.ipynb` の学習コマンドセルでコメントを外す):

    "--resolution", "2",              # 解像度を 1/2 に
    "--densify_until_iter", "10000",  # Gaussian 数を制限

---

## Colab セッションが 90 分でタイムアウト

**対処**:
- `ITERATIONS = 7000` で短縮版を試す（約 15 分）
- Colab Pro へアップグレード（12 時間セッション）
- チェックポイントから再開: `--start_checkpoint <path>`

---

## Google Drive の読み書きが遅い

`03_train_3dgs.ipynb` は `/content/` で学習後に Drive へコピーする設計のため、通常は問題ありません。

---

## `cameras.bin` が読めない

pycolmap のバージョンによっては txt 形式でも動作します。

    reconstruction.write_text(str(SPARSE_DIR))
    # cameras.txt, images.txt, points3D.txt が生成される
