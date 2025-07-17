# Market Basket Analysis & Customer Segmentation in Online Retail

**Course**: Advanced Data Mining  
**Project Type**: Individual Mini-project 

---

## Project Overview

This project applies **market basket analysis** and **customer segmentation** techniques to a real-world ecommerce dataset from the UK-based **Online Retail Dataset**. The goal is to understand which products are commonly purchased together (market basket rules), and to identify distinct customer groups based on purchasing behavior (clustering).

---

## Objectives

- Extract meaningful **association rules** between products using the **Apriori algorithm**
- Segment customers using **K-Means clustering** on **RFM (Recency, Frequency, Monetary)** metrics
- Present insights that can help improve marketing, promotions, and customer management
- Deliver reproducible, clean, and well-documented data-mining code

---

## Data Source

- Dataset: [UCI Machine Learning Repository – Online Retail](https://archive.ics.uci.edu/ml/datasets/online+retail)
- Format: CSV (for Kaggle/lab compatibility)
- Size: ~50,000+ transactions from a UK-based online store (2010–2011)
- Only transactions with non-null `CustomerID`, positive `Quantity`, and `UnitPrice` were used. Cancellations were removed.

---

## Project Structure

```plaintext
miniproject_258738G/
├── data/
│   ├── online_retail.csv             # Raw sample dataset
│   ├── cleaned_retail.csv            # Cleaned and preprocessed data
│   ├── association_rules_output.csv  # Output of Apriori algorithm
│   └── customer_clusters.csv         # Clustering output using KMeans
│
├── notebooks/
│   └── analysis.ipynb                # Exploratory data analysis
│
├── src/
│   ├── association_rules.py          # Market basket analysis
│   └── customer_clustering.py        # KMeans clustering for RFM
│
├── run_all.sh                        # Runs entire code
├── requirements.txt                  # Python dependencies
├── README.md                         # reading it