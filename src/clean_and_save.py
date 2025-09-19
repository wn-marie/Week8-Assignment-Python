# src/clean_and_save.py
import pandas as pd

def main():
    print("=== STEP 2: CLEANING DATA (USING SAMPLE) ===")
    
    # Load only 10,000 rows — as suggested and per assignment instructions
    df = pd.read_csv('../data/metadata.csv', nrows=10000)
    print(f"📦 Loaded sample of {len(df):,} rows.")
    
    # Drop columns with >70% missing (keep cols with at least 30% non-null)
    threshold = len(df) * 0.3
    df_clean = df.dropna(thresh=threshold, axis=1).copy()
    print(f"🧹 After dropping sparse columns: {df_clean.shape}")
    
    # Convert publish_time to datetime, extract year
    df_clean['publish_time'] = pd.to_datetime(df_clean['publish_time'], errors='coerce')
    df_clean['year'] = df_clean['publish_time'].dt.year
    df_clean = df_clean.dropna(subset=['year']).copy()
    df_clean['year'] = df_clean['year'].astype(int)
    print(f"📅 After cleaning dates: {df_clean.shape}")
    
    # Add word counts
    df_clean['abstract_word_count'] = df_clean['abstract'].fillna('').str.split().str.len()
    df_clean['title_word_count'] = df_clean['title'].fillna('').str.split().str.len()
    print("🧮 Added word count columns.")
    
    # Save cleaned sample (this is what your app & plots will use)
    output_path = '../data/metadata_clean.csv'
    df_clean.to_csv(output_path, index=False)
    print(f"✅ FINAL CLEANED SAMPLE SAVED TO: {output_path}")
    print(f"📊 Final sample shape: {df_clean.shape}")

if __name__ == "__main__":
    main()