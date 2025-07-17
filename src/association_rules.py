import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import os

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def prepare_data(df):
    df = df[df['Country'] == 'United Kingdom']

    basket = df.groupby(['InvoiceNo', 'Description'])['Quantity'].sum().unstack().fillna(0)

    basket = basket.applymap(lambda x: 1 if x > 0 else 0)
    return basket

def generate_association_rules(basket, min_support=0.02, min_confidence=0.2, min_lift=3):

    frequent_itemsets = apriori(basket, min_support=min_support, use_colnames=True)

    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=min_lift)

    rules = rules[rules['confidence'] >= min_confidence]

    return rules

def main():
    print("Reading and processing data...")

    raw_data_path = os.path.join("data", "cleaned_retail.csv")
    df = load_data(raw_data_path)

    basket = prepare_data(df)

    rules = generate_association_rules(basket)

    output_path = os.path.join("data", "association_rules_output.csv")
    rules.to_csv(output_path, index=False)

    print(f"Association rules saved to {output_path}")
    print(rules.head(10)) 

if __name__ == "__main__":
    main()