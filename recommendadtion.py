import pandas as pd

# Load dataset
df = pd.read_excel("movies_dataset.csv.xlsx")

# Show columns
print(df.columns)

# Show first rows
print(df.head())

# User input
genre = input("Enter your favorite genre: ")

# Filter movies
recommended = df[df['Genre'].str.lower() == genre.lower()]

# Show recommendations
print("\nRecommended Movies:")
print(recommended.head(5))