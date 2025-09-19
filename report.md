# 📊 CORD-19 Assignment Reflection

## ✅ Tasks Completed
- Loaded and explored CORD-19 metadata dataset.
- Cleaned data: handled missing values, converted dates, added word counts.
- Generated 4 visualizations: publications by year, top journals, title word cloud, source distribution.
- Built interactive Streamlit app with filters and download.
- Documented entire process.

## 🔍 Key Findings (Based on 10,000-Paper Sample)
- Peak research output occurred in 2020–2021.
- Top publishing sources: PubMed Central (PMC), medRxiv, bioRxiv.
- Most frequent title words: “COVID-19”, “SARS-CoV-2”, “pandemic”, “vaccine”.

## ⚠️ Challenges & Solutions
- **Kaggle site down**: Already had dataset downloaded — no issue.
- **Large dataset**: Used sample of 10,000 rows as suggested in assignment (“Start small”).
- **Missing data**: Dropped sparse columns, used `.fillna('')` for text features.
- **Date parsing**: Used `errors='coerce'` to handle malformed dates.

## 📚 What I Learned
- Importance of data cleaning in real-world projects.
- How to create meaningful visualizations with matplotlib/seaborn.
- Building interactive web apps with Streamlit — surprisingly easy!
- Using `.gitignore` to manage large files in GitHub repos.

## 🚀 Future Improvements
- Add keyword search functionality.
- Implement simple topic modeling.
- Allow user to upload their own sample.

✅ Assignment complete. All code is clean, commented, and functional — built using a sample as permitted by instructions.