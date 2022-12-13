import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import colornormalizer

df = pd.read_csv('coches-de-segunda-mano-sample.csv')

# Delete column price_financed (not useful and lots of na)
df.drop(['price_financed'], axis = 1, inplace = True)

# Delete other non useful columns
df.drop(columns=['url', 'company', 'publish_date', 'insert_date'], inplace=True)

# Drop rows with missing values
cars = df.dropna()


#cars['color'] = cars['color'].apply(colornormalizer.normalize_color)
colores = cars.groupby("color").count()

