import streamlit as st
import pandas as pd
import numpy as np
from plotly import tools
from IPython.core import display as ICD
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
import plotly.express as px
import plotly.io as pio

        # Use write for most of the text
st.title('DataViz for DataViz')
st.write("Starting Data science journey can be difficult, let us help you.")

@st.cache(suppress_st_warning=True)
def displayPlot(d):
    fig = go.Figure(data=d, layout=layout)
    fig


survey_df = pd.read_csv("multipleChoiceResponses.csv") 
responses_df = survey_df[1:]
responses_df_orig = responses_df.copy()

responses_df = responses_df[~pd.isnull(responses_df['Q35_Part_1'])]
count_dict = {
    'Self-taught' : (responses_df['Q35_Part_1'].astype(float)>0).sum(),
    'Online courses (Coursera, Udemy, edX, etc.)' : (responses_df['Q35_Part_2'].astype(float)>0).sum(),
    'Work' : (responses_df['Q35_Part_3'].astype(float)>0).sum(),
    'University' : (responses_df['Q35_Part_4'].astype(float)>0).sum(),
    'Kaggle competitions' : (responses_df['Q35_Part_5'].astype(float)>0).sum(),
    'Other' : (responses_df['Q35_Part_6'].astype(float)>0).sum()
}

cnt_srs = pd.Series(count_dict)

trace = go.Bar(
    x=cnt_srs.index,
    y=cnt_srs.values,
    marker=dict(
        color='#ffa600',
    #    colorscale = 'Picnic',
    #    reversescale = True
    ),
)

layout = go.Layout(
    title='Number of respondents for each learning category'
)

data = [trace]
displayPlot(data)

st.write("This should take less time")



        # To make table
# st.write(pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# }))


# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])

# st.line_chart(chart_data)


        #To get map data don't know how to use
# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

# st.map(map_data)