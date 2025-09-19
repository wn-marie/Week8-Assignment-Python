# 🧪 CORD-19 Research Explorer (Sample)

A Python-based analysis of a **sample (10,000 rows)** from the CORD-19 metadata dataset, with an interactive Streamlit dashboard.

> **Note**: Per assignment instructions (“Start small: Begin with a subset of the data”), this project uses a sample of 10,000 papers. The full `metadata.csv` is >300MB and excluded from this repo.

## 📁 Structure
- `data/` — Excluded large files via `.gitignore`
- `src/` — Cleaning, analysis, and Streamlit app scripts
- `plots/` — Generated visualizations from sample data

## 🚀 How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt

2. Place metadata.csv (downloaded from Kaggle) into /data

3. Clean sample data:
   ```bash
   python src/clean_and_save.py

4. Generate plots:
   ```bash
   python src/analyze_and_plot.py

5. Launch app:
   ```bash
   streamlit run src/app.py

   Use this if `streamlit` command is not found:
   ```bash
   python -m streamlit run src/app.py

🎯 Built For
Python Frameworks Assignment — demonstrating data cleaning, analysis, visualization, and web app development using a sample dataset as instructed.

✅ Submitted to GitHub