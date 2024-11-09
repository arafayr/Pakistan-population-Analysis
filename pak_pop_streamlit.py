import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv('https://raw.githubusercontent.com/arafayr/Pakistan-s-population-Analysis/refs/heads/main/pakistan_pop_data.csv')

list_of_province = list(df['province'].unique())
list_of_province.insert(0,'Overall Pakistan')

st.sidebar.title('Pakistan pop Data visualization')

selected_province = st.sidebar.selectbox('Select a province',list_of_province)
primary = st.sidebar.selectbox('Select Primary Parameter',sorted(df.columns[2:]))
secondary = st.sidebar.selectbox('Select Secondary Parameter', [x for x in sorted(df.columns[2:]) if x != primary])

plot = st.sidebar.button('Plot Graph')

if plot:

    st.text('Size of dots represent primary parameter')
    st.text('Color of dots represents secondary parameter')
    if selected_province == 'Overall Pakistan':
        fig = px.scatter_mapbox(df, lat="lat", lon="lng", size=primary, color=secondary, zoom=4,size_max=35,
                                mapbox_style="carto-positron",width=1200,height=700,hover_name='city')

        st.plotly_chart(fig,use_container_width=True)
    else:
        province_df = df[df['province'] == selected_province]

        fig = px.scatter_mapbox(province_df, lat="lat", lon="lng", size=primary, color=secondary, zoom=6, size_max=35,
                                mapbox_style="carto-positron", width=1200, height=700,hover_name='city')

        st.plotly_chart(fig, use_container_width=True)