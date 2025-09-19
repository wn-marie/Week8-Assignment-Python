# src/app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

st.set_page_config(page_title="CORD-19 Explorer", layout="wide")

# ✅ REPLACED THIS FUNCTION — now uses absolute path + error handling
@st.cache_data
def load_data():
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, '..', 'data', 'metadata_clean.csv')
    
    if not os.path.exists(data_path):
        st.error(f"❌ Data file not found at: {data_path}")
        st.stop()
    
    return pd.read_csv(data_path)

def main():
    st.title("CORD-19 Research Explorer 🧪")
    st.markdown("### Interactive exploration of COVID-19 research (Sample of 10,000 papers)")
    
    df = load_data()
    st.info(f"📚 Loaded {len(df):,} research papers (sample).")
    
    # Sidebar filters
    st.sidebar.header("🔍 Filters")
    min_year = int(df['year'].min())
    max_year = int(df['year'].max())
    selected_years = st.sidebar.slider(
        "Select Year Range",
        min_value=min_year,
        max_value=max_year,
        value=(2020, 2022)
    )
    
    # Filter data
    df_filtered = df[(df['year'] >= selected_years[0]) & (df['year'] <= selected_years[1])]
    st.write(f"### 📄 Showing {len(df_filtered):,} papers from {selected_years[0]}–{selected_years[1]}")
    
    # Layout: 2 columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Publications Over Time")
        yearly = df_filtered['year'].value_counts().sort_index()
        fig, ax = plt.subplots(figsize=(6,4))
        ax.bar(yearly.index, yearly.values, color='#FF6F61', edgecolor='black')
        ax.set_xlabel("Year", fontsize=11)
        ax.set_ylabel("Number of Papers", fontsize=11)
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        st.pyplot(fig)
    
    with col2:
        st.subheader("📰 Top 5 Journals")
        top_j = df_filtered['journal'].value_counts().head(5)
        if not top_j.empty:
            fig, ax = plt.subplots(figsize=(6,4))
            sns.barplot(x=top_j.values, y=top_j.index, ax=ax, palette='coolwarm')
            ax.set_xlabel("Paper Count", fontsize=11)
            st.pyplot(fig)
        else:
            st.write("_No journal data in this range._")
    
    # Full-width: Word Cloud
    st.subheader("☁️ Title Word Cloud")
    text = ' '.join(df_filtered['title'].dropna().astype(str))
    if len(text.strip()) > 50:
        wc = WordCloud(width=800, height=300, background_color='white', max_words=80, random_state=42).generate(text)
        fig, ax = plt.subplots(figsize=(15, 5))
        ax.imshow(wc, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig)
    else:
        st.write("Not enough titles to generate word cloud.")
    
    # Sample data table
    st.subheader("📋 Sample Papers")
    display_cols = ['title', 'journal', 'year', 'doi']
    available_cols = [col for col in display_cols if col in df_filtered.columns]
    st.dataframe(df_filtered[available_cols].head(10), use_container_width=True)
    
    # Download button (for the filtered sample)
    csv = df_filtered.to_csv(index=False).encode('utf-8')
    st.download_button(
        "📥 Download Filtered Sample (CSV)",
        csv,
        f"cord19_sample_{selected_years[0]}_{selected_years[1]}.csv",
        "text/csv",
        key='download-csv'
    )

if __name__ == "__main__":
    main()