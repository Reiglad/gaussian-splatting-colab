"""環境チェックスクリプト。Colab のセル上で実行可能。"""
import sys
import importlib


def check(name):
    try:
        m = importlib.import_module(name)
        ver = getattr(m, "__version__", "n/a")
        print(f"  [OK] {name} ({ver})")
        return True
    except ImportError as e:
        print(f"  [NG] {name}: {e}")
        return False


print("=== Python ===")
print(f"  {sys.version}")

print("\n=== GPU ===")
try:
    import torch
    if torch.cuda.is_available():
        print(f"  [OK] CUDA {torch.version.cuda} / {torch.cuda.get_device_name(0)}")
        print(f"       VRAM: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")
    else:
        print("  [NG] CUDA not available")
except Exception as e:
    print(f"  [NG] torch: {e}")

print("\n=== Libraries ===")
all_ok = all([
    check("pycolmap"),
    check("diff_gaussian_rasterization"),
    check("simple_knn"),
    check("plyfile"),
])

print("\n" + ("全モジュールOK" if all_ok else "エラーあり — troubleshooting.md を参照"))
