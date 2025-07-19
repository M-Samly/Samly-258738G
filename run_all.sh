echo "Starting Data Mining Pipeline..."

if [ ! -f "data/cleaned_retail.csv" ]; then
  echo "Error: 'data/cleaned_retail.csv' not found."
  echo "Please run notebooks/analysis.ipynb to create the cleaned data first."
  exit 1
fi

echo "Running association rule mining..."
python3 src/association_rules.py

echo "Running customer clustering..."
python3 src/customer_clustering.py

echo "All tasks completed successfully."
echo "Outputs saved in: data/"