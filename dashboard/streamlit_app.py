# Using streamlit, run using ==> streamlit run streamlit_app.py

import streamlit as st
import pandas as pd
import numpy as np
from plotly import tools
from IPython.core import display as ICD
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode, iplot
import plotly.express as px
import plotly.io as pio


if __name__ == "__main__":
    # Use write for most of the text
    st.title('DataViz for DataViz')
    st.write("Starting Data science journey can be difficult, let us help you.")

    exp = st.radio("How experienced are you ? ", ("No Idea", "Beginner", "Expert"), index=0)

    if exp == "No Idea":
        st.write("Hey have a look at Data Science")

    elif exp == "Beginner":
        st.write("Let us help you to get started in Data Science")

    elif exp == "Expert":
        st.write("Hey, you look expreinced, let us explore some new concepts")
        # st.image("../visualizations/newplot (5).png")
        # st.image("../visualizations/newplot (6).png")
        # st.image("../visualizations/newplot (7).png")

    # if st.button('Say hello'):
    #     st.write('Why hello there')
        # st.image("../visualizations/newplot (1).png")
        # st.image("../visualizations/newplot (2).png")
        # st.image("../visualizations/newplot (3).png")
        # st.image("../visualizations/newplot (4).png")


    # else:
    #     st.write('Goodbye')    
    
