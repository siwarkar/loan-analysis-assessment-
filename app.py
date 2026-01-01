import streamlit as st    
import plotly.express as px 
import pandas as pd   
from sklearn.datasets import load_iris
iris=load_iris(as_frame=True)
df=iris.frame
st.title("iris interactive dashboard")
species=st.selectbox("select species",df['target'].unique())
filtered_df=df[df["target"]==species]
fig=px.scatter(filtered_df,x="sepal length (cm)",y="petal length (cm)",color="target")
st.plotly_chart(fig,use_container_width=True)
st.dataframe(filtered_df)
fig1=px.scatter(filtered_df,x="sepal width (cm)",y="petal width (cm)",color="target")
st.plotly_chart(fig1,use_container_width=True)
st.dataframe(filtered_df)