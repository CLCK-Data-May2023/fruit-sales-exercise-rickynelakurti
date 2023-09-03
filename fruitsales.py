# add your code here

import pandas as pd

def create_fruit_sales_csv():
    sales_data = {
        'Apples': [35, 41],
        'Bananas': [21, 34]
    }
    
    years = ['2017 Sales', '2018 Sales']

    df = pd.DataFrame(sales_data, index=years)

    df.to_csv('fruit.csv')
    print("Data saved to fruit.csv!")

if __name__ == "__main__":
    create_fruit_sales_csv()