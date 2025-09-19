# src/test_path.py
import pandas as pd

try:
    df = pd.read_csv('../data/metadata_clean.csv')
    print("✅ SUCCESS! File loaded.")
    print(f"Shape: {df.shape}")
    print(df.head(2))
except FileNotFoundError as e:
    print("❌ ERROR:", e)