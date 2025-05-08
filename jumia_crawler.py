import pandas as pd

df = pd.read_csv(jumia.csv)

df.column = ['HT_name','current_price','old_price','percent_discount','reviews_no','Ratings']

df['current_price'] = ['current_price'].str.replace()

df.describe()
df.head()
df.info()


