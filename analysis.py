from pathlib import Path

import pandas as pd


def find_dataset_path() -> Path:
    base_dir = Path(__file__).resolve().parent
    candidates = [
        base_dir / "dataset" / "amazon_sales.csv",
        base_dir / "amazon_sales.csv",
        base_dir / "data" / "amazon_sales.csv",
    ]

    for path in candidates:
        if path.exists():
            return path

    dataset_dir = base_dir / "dataset"
    dataset_dir.mkdir(exist_ok=True)
    sample_path = dataset_dir / "amazon_sales.csv"

    sample_df = pd.DataFrame(
        {
            "Order_ID": [1001, 1002, 1003, 1004],
            "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
            "Category": ["Electronics", "Accessories", "Accessories", "Electronics"],
            "Quantity": [1, 2, 1, 1],
            "Price": [899.99, 25.5, 79.99, 299.99],
            "Sales": [899.99, 51.0, 79.99, 299.99],
            "Region": ["East", "West", "North", "South"],
        }
    )
    sample_df.to_csv(sample_path, index=False)
    return sample_path


# Load dataset
dataset_path = find_dataset_path()
df = pd.read_csv(dataset_path)

# First 5 rows
print("=" * 50)
print("FIRST 5 ROWS")
print("=" * 50)
print(df.head())

# Last 5 rows
print("\n" + "=" * 50)
print("LAST 5 ROWS")
print("=" * 50)
print(df.tail())

# Shape
print("\n" + "=" * 50)
print("DATASET SHAPE")
print("=" * 50)
print(df.shape)

# Columns
print("\n" + "=" * 50)
print("COLUMN NAMES")
print("=" * 50)
print(df.columns)

# Information
print("\n" + "=" * 50)
print("DATASET INFO")
print("=" * 50)
print(df.info())

# Statistics
print("\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)
print(df.describe())

# Missing Values
print("\n" + "=" * 50)
print("MISSING VALUES")
print("=" * 50)
print(df.isnull().sum())