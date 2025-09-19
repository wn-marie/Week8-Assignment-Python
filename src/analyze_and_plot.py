# src/analyze_and_plot.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import os

def main():
    print("=== STEP 3: GENERATING VISUALIZATIONS ===")
    
    # Load cleaned sample
    df = pd.read_csv('../data/metadata_clean.csv')
    print(f"📈 Loaded {len(df):,} papers for analysis.")
    
    # Create plots folder
    os.makedirs('../plots', exist_ok=True)
    
    # 1. PLOT: Publications by Year
    plt.figure(figsize=(10, 5))
    year_counts = df['year'].value_counts().sort_index()
    plt.bar(year_counts.index, year_counts.values, color='#4B8BBE', edgecolor='black', width=0.6)
    plt.title('Publications by Year (Sample)', fontsize=16, weight='bold')
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Number of Papers', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('../plots/01_publications_by_year.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("✅ Saved: 01_publications_by_year.png")
    
    # 2. PLOT: Top 10 Journals
    plt.figure(figsize=(10, 6))
    top_journals = df['journal'].value_counts().head(10)
    sns.barplot(x=top_journals.values, y=top_journals.index, palette='Spectral')
    plt.title('Top 10 Journals (Sample)', fontsize=16, weight='bold')
    plt.xlabel('Number of Papers', fontsize=12)
    plt.tight_layout()
    plt.savefig('../plots/02_top_journals.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("✅ Saved: 02_top_journals.png")
    
    # 3. PLOT: Word Cloud of Titles
    text = ' '.join(df['title'].dropna().astype(str).tolist())
    if len(text.strip()) > 50:
        wordcloud = WordCloud(
            width=800, height=400,
            background_color='white',
            max_words=100,
            colormap='plasma',
            random_state=42
        ).generate(text)
        
        plt.figure(figsize=(15, 7))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('Frequent Words in Titles (Sample)', fontsize=18, weight='bold', pad=20)
        plt.tight_layout()
        plt.savefig('../plots/03_title_wordcloud.png', dpi=300, bbox_inches='tight')
        plt.show()
        print("✅ Saved: 03_title_wordcloud.png")
    else:
        print("⚠️ Not enough title text for word cloud.")
    
    # 4. PLOT: Source Distribution
    plt.figure(figsize=(8, 8))
    source_counts = df['source_x'].value_counts()
    plt.pie(source_counts.values, labels=source_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title('Paper Sources (Sample)', fontsize=16, weight='bold')
    plt.tight_layout()
    plt.savefig('../plots/04_source_distribution.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("✅ Saved: 04_source_distribution.png")
    
    print("\n🎉 STEP 3 COMPLETE — All plots saved to /plots")

if __name__ == "__main__":
    main()