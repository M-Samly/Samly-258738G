# Market Basket & Customer Segmentation in Grocery Transactions

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
│   ├── online_retail.csv             # Raw sample dataset (download csv file)
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
```
---

## Dataset Instructions

To run the analysis, you need to download the dataset and place it in the correct folder. Follow the steps below:

1. **Download the Dataset**  
   Download the `online_retail.csv` file from the following Google Drive link:  
   [Click here to download the dataset](https://drive.google.com/drive/folders/1Qt1dzvWsDGiwL7HDXTnKlakkag7AnILp?usp=sharing)

2. **Create the `data/` Folder**  
   If it doesn't already exist, create a folder named `data` at the root of the project directory.

3. **Move the CSV File**  
   After downloading, move the `online_retail.csv` file into the `data/` folder.


## How to Execute This Project

To run the code and view the analysis outputs, please follow the steps below:

---

### Step 1: Install Python

Make sure you have **Python 3.8+** installed. You can download it from the official site.

---

### Step 2: Set Up in VS Code

1. Open the project in **Visual Studio Code** (VS Code).
2. Make sure the Python extension is installed in VS Code.
3. Open a terminal in VS Code.

---

### Step 3: Install Required Python Packages

Install all required packages using the following command in the terminal:

```bash
pip install mlxtend scikit-learn matplotlib seaborn pandas jupyter notebook
pip install -r requirements.txt
```
---

## Step 4: Launch Jupyter Notebook

To launch Jupyter Notebook, run the following command in your terminal:

```bash
python -m notebook
```
---

## Execution Options

### Option 1: Use Shell Script 

```bash
./run_all.sh
```

### Option 2: Run Python Scripts Manually

Make sure your terminal is located at the **project root folder** (e.g., `miniproject_258738G`).

#### Run Association Rule Mining Script

```bash
python src/association_rules.py
```

This will generate the file `association_rules_output.csv` inside the `data/` folder.

---

#### Run Customer Clustering Script

```bash
python src/customer_clustering.py
```
This will generate the file `customer_clusters.csv` inside the `data/` folder.

---

### Launching Jupyter Notebook

After setting up the dataset and environment, you can run the full analysis interactively using **Jupyter Notebook**.

To launch Jupyter Notebook, run the following command:

```bash
python -m notebook
```

---

### Best Practice Recommendation

For full insights including:

- Interactive visualizations  
- Summary tables  
- Charts and clustering plots  

It is **highly recommended** to open and run:

```bash
analysis.ipynb
```

---

### Full Analysis Report

You can view the complete results with charts, association rules, and clustering insights here:

🔗 [View Full Analysis Output (HTML/PDF)](https://drive.google.com/drive/folders/1ZuF17gcwqzQ-impOph0J49z5Wut1tAXa?usp=sharing)

