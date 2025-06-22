import os
import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')  # Use an interactive backend
import matplotlib.pyplot as plot

def run():    
    file_path = "housing_market/Mall_Customers.csv"
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return

    df = pd.read_csv(file_path)

    print(df.describe())

    # Gender distribution
    sns.countplot(x='Gender', data=df)
    plot.title("Gender Distribution")
    plot.show()