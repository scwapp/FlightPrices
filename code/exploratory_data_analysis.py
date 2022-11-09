import pandas as pd
from pathlib import Path
import plotly.graph_objects as go
import plotly.express as px

dataset_folder = Path('C:/Users/s.coll/Documents/Udacity Data Science Course/01-Project Airlines/data')
dataset_path = dataset_folder/'Clean_Dataset.csv'

df = pd.read_csv(dataset_path, index_col=0)
indep_cols = [col for col in df.columns if col != 'price']

for col in indep_cols:
    print(col)
    fig = px.violin(df, y="price", x=col, box=True, 
          hover_data=indep_cols)
    fig.show()

print()