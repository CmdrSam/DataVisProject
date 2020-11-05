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
    st.title('RoadMap for Data Science')
    # st.balloons()

    st.subheader("Starting Data science journey can be difficult, let us help you.")

    st.subheader("Answer a few questions on left sidebar and we would display you a complete guide")

    # exp = st.radio("How experienced are you with Data Science ? ", ("No Idea", "Beginner", "Expert"), index=0)

    exp = st.sidebar.selectbox('How experienced are you with Data Science ?',
                               options=["No Idea", "Beginner", "Expert"], index=0)

    edu = st.sidebar.select_slider("Select your education",
                            options=["High School", "Undergrad", "Post-Grad", "PhD"])

    if exp == "No Idea":
        st.write("Hey have a look at Data Science")

    elif exp == "Beginner":
        st.write("Let us help you to get started in Data Science")

    elif exp == "Expert":
        interest = st.sidebar.radio("What's your Key Interest", ('Computer Vision', 'NLP', 'Data Science'))
        st.write("Hey, you look expreinced, let us explore some new concepts")



