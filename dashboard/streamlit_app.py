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
    st.balloons()

    st.subheader("Starting Data science journey can be difficult, let us help you.")

    st.subheader("Answer a few questions on left sidebar and we would display you a complete guide")

    # exp = st.radio("How experienced are you with Data Science ? ", ("No Idea", "Beginner", "Expert"), index=0)

    exp = st.sidebar.selectbox('How experienced are you with Data Science ?',
                               options=["No Idea", "Beginner", "Expert"], index=0)

    edu = st.sidebar.select_slider("Select your education",
                                    options=["High School", "Undergrad", "PostGrad", "PhD"])

    if exp == "No Idea" and edu == "High School":
        st.write("So you don't have much idea about data science")
        st.write("You are in High school, super enthusisastic about data science")

        st.image("../visualizations/images/MostUsedPlatform.png")
        st.image("../visualizations/images/language.png")
        st.image("../visualizations/images/degree.png")
        st.image("../visualizations/images/emp_industry.png")
        st.image("../visualizations/images/hardware.png")
        st.image("../visualizations/images/how_learnt.png")

    elif exp == "No Idea" and edu == "Undergrad":
        st.write("So you don't have much idea about data science")
        st.write("You are in Undergrad, very eager to know about data science")
        st.image("../visualizations/images/language.png")
        st.image("../visualizations/images/degree.png")
        st.image("../visualizations/images/emp_industry.png")
        st.image("../visualizations/images/hardware.png")
        st.image("../visualizations/images/how_learnt.png")

    elif exp == "No Idea" and edu == "PostGrad":
        st.write("So you don't have much idea about data science")
        st.image("../visualizations/images/language.png")
        st.image("../visualizations/images/degree.png")
        st.image("../visualizations/images/emp_industry.png")
        st.image("../visualizations/images/hardware.png")
        st.image("../visualizations/images/how_learnt.png")

    elif exp == "No Idea" and edu == "PhD":
        st.write("So you don't have much idea about data science")
        st.image("../visualizations/images/language.png")
        st.image("../visualizations/images/averagePapersPublisedPerDay.png")
        st.image("../visualizations/images/degree.png")
        st.image("../visualizations/images/emp_industry.png")
        st.image("../visualizations/images/growth_ml.png")
        st.image("../visualizations/images/hardware.png")
        st.image("../visualizations/images/how_learnt.png")
        st.image("../visualizations/images/TopPopularAuthors.png")

    elif exp == "Beginner" and edu == "High School":
        st.write("Let us help you to get started in Data Science")
        st.write("You are in High school, super enthusisastic about data science")
        st.image("../visualizations/images/employment.png")
        st.image("../visualizations/images/time_spent.png")

    elif exp == "Beginner" and edu == "Undergrad":
        st.write("Hey have a look at Data Science")
        st.write("You are in Undergrad, very eager to know about data science")
        st.image("../visualizations/images/ContributionByDegree.png")
        st.image("../visualizations/images/employment.png")
        st.image("../visualizations/images/time_spent.png")

    elif exp == "Beginner" and edu == "PostGrad":
        st.write("Hey have a look at Data Science")
        st.image("../visualizations/images/algos.png")
        st.image("../visualizations/images/ContributionByDegree.png")
        st.image("../visualizations/images/employment.png")
        st.image("../visualizations/images/time_spent.png")

    elif exp == "Beginner" and edu == "PhD":
        st.write("Hey have a look at Data Science")
        st.image("../visualizations/images/algos.png")
        st.image("../visualizations/images/time_spent.png")
        st.image("../visualizations/images/averagePapersPublisedPerDay.png")
        st.image("../visualizations/images/ContributionByDegree.png")
        st.image("../visualizations/images/growth_ml.png")
        st.image("../visualizations/images/TopPopularAuthors.png")

    elif exp == "Expert" and edu == "High School":
        interest = st.sidebar.radio("What's your Key Interest", ('Computer Vision', 'NLP', 'Data Science'))
        st.write("You are in High school, super enthusisastic about data science")
        st.image("../visualizations/images/algos.png")
        st.image("../visualizations/images/methods.png")
        st.image("../visualizations/images/ml_method.png")
        st.image("../visualizations/images/prod.png")

    elif exp == "Expert" and edu == "Undergrad":
        interest = st.sidebar.radio("What's your Key Interest", ('Computer Vision', 'NLP', 'Data Science'))
        st.write("Hey, you look expreinced, let us explore some new concepts")
        st.image("../visualizations/images/ContributionByDegree.png")
        st.image("../visualizations/images/methods.png")
        st.image("../visualizations/images/ml_method.png")
        st.image("../visualizations/images/prod.png")

    elif exp == "Expert" and edu == "PostGrad":
        interest = st.sidebar.radio("What's your Key Interest", ('Computer Vision', 'NLP', 'Data Science'))
        st.write("Hey, you look expreinced, let us explore some new concepts")
        st.image("../visualizations/images/algos.png")
        st.image("../visualizations/images/ContributionByDegree.png")
        st.image("../visualizations/images/methods.png")
        st.image("../visualizations/images/ml_method.png")
        st.image("../visualizations/images/prod.png")

    elif exp == "Expert" and edu == "PhD":
        interest = st.sidebar.radio("What's your Key Interest", ('Computer Vision', 'NLP', 'Data Science'))
        st.write("Hey, you look expreinced, let us explore some new concepts")
        st.image("../visualizations/images/averagePapersPublisedPerDay.png")
        st.image("../visualizations/images/ContributionByDegree.png")
        st.image("../visualizations/images/growth_ml.png")
        st.image("../visualizations/images/methods.png")
        st.image("../visualizations/images/ml_method.png")
        st.image("../visualizations/images/prod.png")
        st.image("../visualizations/images/TopPopularAuthors.png")
