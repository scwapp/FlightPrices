import pandas as pd
from pathlib import Path
import plotly.graph_objects as go
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

parent_folder = Path('C:/Users/s.coll/Documents/Udacity Data Science Course/01-Project Airlines')
dataset_folder = Path('C:/Users/s.coll/Documents/Udacity Data Science Course/01-Project Airlines/data')
dataset_path = dataset_folder/'Clean_Dataset.csv'

df = pd.read_csv(dataset_path, index_col=0)
indep_cols = [col for col in df.columns if col != 'price']

###process data

#convert indian rupee to euro (1 Indian Rupee = 0.012 Euro)
df['price'] = df['price'] * 0.012
#define categorical variables
df['stops'] = df['stops'].astype('category')
df['departure_time'] = df['departure_time'].astype('category')
#order categories
df['stops'] = df['stops'].cat.set_categories(['zero', 'one', 'two_or_more'],ordered=True)
df['departure_time'] = df['departure_time'].cat.set_categories(['Early_Morning', 'Morning', 'Afternoon', 'Evening', 'Night', 'Late_Night'],ordered=True)


###PLOTS
# plot = 'departure_time' #'heatmap' 'violin'
# if plot== 'heatmap':
#Plot heatmap of stops and departure time
df_heat= df.pivot_table(index = "stops", columns="departure_time", values="price", aggfunc='mean')
fig = px.density_heatmap(df, x="stops", y="departure_time", z='price',marginal_x="box", marginal_y="violin",histfunc='avg')
fig_html_path = parent_folder/'plots'/f'heatmap_marginals_viol_box.html'
# fig.write_html(fig_html_path)
fightml = fig.to_html(full_html=False, include_plotlyjs='cdn')  
with open(fig_html_path, 'w') as f:
    f.write(fightml)
fig.show()

for col in indep_cols:
    print(col)
    fig = px.violin(df, y="price", x=col, box=True, 
          hover_data=indep_cols)
    fig.show()

print()