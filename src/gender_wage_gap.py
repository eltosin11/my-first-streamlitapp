# Streamlit live coding script
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy



# First some MPG Data Exploration
@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    return df

gwg_df_raw = load_data(path = "C:/Users/eltos/OneDrive/Jobbie/Data_Science_Bootcamp/tosin-aderanti/03_Visualization/day1/data/data/gwg.csv")
gwg_df = deepcopy(gwg_df_raw)
 
# Add title and header
st.title("Gender Wage Gap in Low and Middle-Income Countries")
st.header("By Occupation")


# Widgets: checkbox (you can replace st.xx with st.sidebar.xx)
if st.checkbox("Show Dataframe"):
    st.subheader("ILO dataset:")
    st.dataframe(data=gwg_df)

# Setting up columns
left_column, middle_column, right_column = st.columns([3, 1, 1])

# Widgets: selectbox
years = ["All"]+sorted(pd.unique(gwg_df['time']))
year = left_column.selectbox("Choose a Year", years)

# Widgets: radio buttons
show_means = middle_column.radio(
    label='Show Class Means', options=['Yes', 'No'])

plot_types = ["Matplotlib", "Plotly"]
plot_type = right_column.radio("Choose Plot Type", plot_types)

# Flow control and plotting
if year == "All":
    reduced_df = gwg_df
else:
    reduced_df = gwg_df[gwg_df["year"] == year]

means = reduced_df.groupby('classif1.label').mean(numeric_only=True)

# In Matplotlib
m_fig, ax = plt.subplots(figsize=(10, 8))
ax.scatter(reduced_df['ref_area.label'], reduced_df['obs_value'], alpha=0.7)

if show_means == "Yes":
    ax.scatter(means['displ'], means['hwy'], alpha=0.7, color="red")

ax.set_title("Engine Size vs. Highway Fuel Mileage")
ax.set_xlabel('Displacement (Liters)')
ax.set_ylabel('MPG')

