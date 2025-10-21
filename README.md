# Olist E-Commerce Data Analysis

Brazilian e-commerce data analysis project using the Olist dataset to uncover insights about delivery times, customer satisfaction, and revenue patterns.

## 📊 Presentation

Full analysis and findings available in: [OlistDataPresentation.pdf](./OlistDataPresentation.pdf)

## Dataset

Source: [Olist Brazilian E-Commerce Public Dataset](https://wagon-public-datasets.s3.amazonaws.com/olist/olist.zip)

The dataset contains information about:
- Orders and their status
- Customers and their locations
- Order items and products
- Payments
- Reviews and ratings
- Sellers

## Project Structure

```
olistdata/
├── data/
│   ├── csv/                    # CSV datasets
│   └── olist.zip              # Original dataset archive
├── olistanalyisis.py          # Main analysis script
├── Untitled.ipynb             # Jupyter notebook analysis
└── venv/                      # Python virtual environment
```

## Analysis Overview

The analysis includes:

1. **Data Loading & Merging**: Combines multiple datasets (orders, customers, products, payments, reviews, sellers)
2. **Data Cleaning**: Handles timestamps, calculates delivery times, removes null values
3. **Descriptive Statistics**: Average delivery time, review scores
4. **Visualizations**:
   - Delivery time distribution
   - Review score vs delivery time correlation
   - Top 10 states by revenue
5. **Key Insights**: Customer satisfaction metrics and delivery performance

## Setup

### Requirements

- Python 3.12
- pandas
- numpy
- matplotlib
- seaborn

### Installation

```bash
# Clone the repository
git clone https://github.com/ignaciogomenuka/olistdata.git
cd olistdata

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install pandas numpy matplotlib seaborn jupyter
```

## Usage

### Running the Python Script

```bash
python olistanalyisis.py
```

### Using Jupyter Notebook

```bash
jupyter notebook Untitled.ipynb
```

## Key Findings

- **Delivery Performance**: Analysis of average delivery times across different regions
- **Customer Satisfaction**: Correlation between delivery time and review scores
- **Revenue Distribution**: Geographic revenue patterns across Brazilian states
- **Review Patterns**: Percentage of positive reviews (4-5 stars)

## Data Schema

The dataset consists of multiple interconnected tables that provide a comprehensive view of the e-commerce operations:

### Database Schema Overview

![Database Schema - Part 1](./Captura%20de%20pantalla%202025-10-21%20040815.png)

![Database Schema - Part 2](./Captura%20de%20pantalla%202025-10-21%20040834.png)

### Datasets Used

- `olist_orders_dataset.csv` - Order information
- `olist_customers_dataset.csv` - Customer data
- `olist_order_items_dataset.csv` - Items per order
- `olist_products_dataset.csv` - Product catalog
- `olist_order_payments_dataset.csv` - Payment details
- `olist_order_reviews_dataset.csv` - Customer reviews
- `olist_sellers_dataset.csv` - Seller information
- `olist_geolocation_dataset.csv` - Geolocation data
- `product_category_name_translation.csv` - Category translations

## Author

Ignacio Muñoz Gomeñuka

## License

This project uses public data from Olist. Please refer to the original dataset terms of use.
