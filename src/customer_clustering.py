import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import os

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print(f"Loaded data: {file_path}")
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        exit(1)

def calculate_rfm(df):
    print("Calculating RFM features...")

    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

    reference_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)

    rfm = df.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (reference_date - x.max()).days,  
        'InvoiceNo': 'nunique',                                    
        'TotalPrice': 'sum'                                        
    }).reset_index()

    rfm.columns = ['CustomerID', 'Recency', 'Frequency', 'Monetary']
    print(f"RFM features created for {rfm.shape[0]} customers")
    return rfm

def perform_clustering(rfm, n_clusters=4):
    print(f"Running KMeans with {n_clusters} clusters...")

    features = ['Recency', 'Frequency', 'Monetary']

    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(rfm[features])

    kmeans = KMeans(n_clusters=n_clusters, max_iter=500, random_state=42)
    rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)

    print("Clustering complete.")
    return rfm

def main():
    input_file = os.path.join("data", "cleaned_retail.csv")
    output_file = os.path.join("data", "customer_clusters.csv")

    df = load_data(input_file)
    rfm = calculate_rfm(df)
    rfm_clustered = perform_clustering(rfm)

    rfm_clustered.to_csv(output_file, index=False)
    print(f"Clustered customer data saved to {output_file}")
    print(rfm_clustered.groupby('Cluster').agg({
        'Recency': 'mean',
        'Frequency': 'mean',
        'Monetary': ['mean', 'count']
    }))

if __name__ == "__main__":
    main()