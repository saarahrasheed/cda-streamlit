# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 15:44:53 2023

@author: saarah.rasheed
"""

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


st.header('Billionaire Dataset')

# reading the file 
df = pd.read_csv('Billionaire.csv')

# data cleaning 
df['NetWorth'] = df['NetWorth'].apply(lambda x: float(x.replace('$', '').replace(' B', '')))

all_countries = sorted(df['Country'].unique())

st.title('Billionaires Dataset')
col1, col2 = st.columns(2)

# COLUMN 1
# display on streamlit
selected_country = col1.selectbox('Select Your Country', all_countries)
#subset on selected country
subset_country = df[df['Country'] == selected_country]

#get unique sources from the selected country
sources = sorted(subset_country['Source'].unique())
# display multi select option on source
selected_source = col1.multiselect('Select Source of Income', sources)
# subset on selected source
subset_source = subset_country[subset_country['Source'].isin(selected_source)]

# COLUMN 2
main_string = '{} - Billionaires'.format(selected_country)
# main_string = selected_country + '  - Billionaires'
col2.header(main_string)
col2.dataframe(subset_country)
col2.header('Source wise Info')
col2.dataframe(subset_source)



















