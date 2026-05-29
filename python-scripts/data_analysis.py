"""
Data Analysis — Honda used car listings using pandas and matplotlib
Demonstrates: DataFrame creation, filtering, aggregation, and pie charts
"""

import pandas as pd
import matplotlib.pyplot as plt

HONDA_LISTINGS = {
    "Model": [
        "Honda Amaze 1.2 VX i-VTEC", "Honda Brio V MT",    "Honda WR-V VX MT Petrol",
        "Honda CR-V 2.4 AT",          "Honda Brio S MT",    "Honda Accord 2.4 iVtec AT",
        "Honda City SV Diesel",        "Honda City V",       "Honda City SV CVT",
        "Honda City V"
    ],
    "Price":     [5050.00, 3510.00, 8199.99, 8600.00, 4400.00, 1950.00, 7500.00, 7300.00, 5900.00, 4800.00],
    "Year":      [2017,    2014,    2018,    2013,    2016,    2008,    2018,    2016,    2015,    2015],
    "Kilometer": [87150,   39276,   27963,   67000,   50374,   57885,   75000,   51834,   116592,  49000]
}


def load_data() -> pd.DataFrame:
    return pd.DataFrame(HONDA_LISTINGS)


def summarize(df: pd.DataFrame) -> None:
    print(df.to_string(index=False))
    print(f"\nPrice range:    ${df['Price'].min():,.2f} – ${df['Price'].max():,.2f}")
    print(f"Avg price:      ${df['Price'].mean():,.2f}")
    print(f"Year range:     {df['Year'].min()} – {df['Year'].max()}")
    print(f"Avg km driven:  {df['Kilometer'].mean():,.0f} km")


def plot_sales_by_year(df: pd.DataFrame, min_price: float = 1000) -> None:
    filtered = df[df["Price"] > min_price]
    sales_count = filtered["Year"].value_counts().sort_index()

    plt.figure(figsize=(8, 8))
    plt.pie(sales_count, labels=sales_count.index, autopct="%1.1f%%", startangle=90)
    plt.title(f"Honda Listings by Year  (price > ${min_price:,.0f})")
    plt.axis("equal")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    df = load_data()
    summarize(df)
    plot_sales_by_year(df)
