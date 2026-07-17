import os

# Create images folder
os.makedirs("images", exist_ok=True)

# Image file names
image_files = [
    "dashboard.png",
    "sales_by_category.png",
    "sales_by_region.png",
    "monthly_sales_trend.png",
    "top_10_products.png",
    "payment_method_analysis.png",
    "region_performance.png",
    "dashboard_filters.png"
]

# Create empty image files
for image in image_files:
    file_path = os.path.join("images", image)
    with open(file_path, "wb") as f:
        pass

print("✅ Images folder created successfully!")
print("Files created:")

for image in image_files:
    print("📷", image)