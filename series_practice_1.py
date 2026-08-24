import pandas as pd

def get_total_sales(sales_data):
    pass


def get_date_with_highest_sales(sales_data):
    pass



def get_average_sales(sales_data):
    pass


def get_days_with_sales_above(sales_data, threshold):
    pass


def get_sales_on_selected_days(sales_data, indices):
    pass



dates = ["2023-10-10", "2023-10-11", "2023-10-12", "2023-10-13", "2023-10-14", "2023-10-15", "2023-10-16"]
sales = [1500, 2300, 2100, 2400, 1800, 2200, 2050]

# Creating a Pandas Series with dates as the index
sales_series = pd.Series(data=sales, index=dates)

# Create a Pandas Series with dates as the index
sales_series = pd.Series(data=sales, index=dates)
print("Sales Series:\n", sales_series, "\n")

# === Manual print-based tests ===
print("Testing get_total_sales()...")
print("Expected: 14350")
print("Got:", get_total_sales(sales_series), "\n")

print("Testing get_date_with_highest_sales()...")
print("Expected: 2023-10-13")
print("Got:", get_date_with_highest_sales(sales_series), "\n")

print("Testing get_average_sales()...")
print("Expected:", 2050.0)
print("Got:", get_average_sales(sales_series), "\n")

print("Testing get_days_with_sales_above() (threshold = 2100)...")
print("Expected: ['2023-10-11', '2023-10-13', '2023-10-15']")
print("Got:", get_days_with_sales_above(sales_series, 2100), "\n")

print("Testing get_sales_on_selected_days() (indices [0, 3, 5])...")
print("Expected: [1500, 2400, 2200]")
print("Got:", get_sales_on_selected_days(sales_series, [0, 3, 5]), "\n")
