import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set seed for reproducibility
np.random.seed(0)

# Generate dates
start_date = datetime(2025, 5, 1)
end_date = datetime(2026, 5, 10)
date_range = pd.date_range(start_date, end_date, freq='D')

# Generate random data
data = {
    'sale_id': range(1, len(date_range) + 1),
    'sales_channel': np.random.choice(['Online', 'Retail', 'Wholesale'], size=len(date_range)),
    'revenue': np.random.uniform(100, 500, size=len(date_range)).round(2),
    'sale_date': date_range
}

# Create DataFrame
sales_data = pd.DataFrame(data)

# Save to CSV
sales_data.to_csv('sales_data.csv', index=False)

print("Sample data generated:")
print(sales_data.head())

