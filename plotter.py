import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import requests 
import streamlit as st

df = pd.read_csv('question5.csv')
print(df.head)

plt.yscale('log')
plot = sns.scatterplot(data=df.query('`Job created` <= 50'), x='Job created', y='Total Savings')