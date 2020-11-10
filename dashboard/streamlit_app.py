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

    # No Idea ######################################
    if exp == "No Idea" and edu == "High School":
        st.write("So you don't have much idea about data science")
        st.write("You are in High school, super enthusisastic about data science!")

        st.write("Now that you want to learn, here are the most popular online platforms to get into world of Data Visualisation!")
        st.image("../visualizations/images/MostUsedPlatform.png")

        st.write("Now that you know where to learn, you should start with python")
        st.image("../visualizations/images/language.png")

        st.write("ML/DS is a very technical feild, so to truly master it you will need some formal education.")
        st.image("../visualizations/images/degree.png")

        st.write("After mastering ML/DS where will you be employed? These are the leading industries that are hiring Data Scientists")
        st.image("../visualizations/images/emp_industry.png")

        st.write("There are lots of misconceptions related to ML/DS that we need a powerfull system to do any kind of ML/DS, We found that most of the Data Scientists use regular laptop for their day to day use!")
        st.image("../visualizations/images/hardware.png")

        st.write("Here is how you can practice and start your ML/DS journey")
        st.image("../visualizations/images/how_learnt.png")

    elif exp == "No Idea" and edu == "Undergrad":
        st.write("So you don't have much idea about data science")
        st.write("You are in Undergrad, very eager to know about data science")

        st.write("Now that you know where to learn, you should start with python")
        st.image("../visualizations/images/language.png")

        st.write("ML/DS is a very technical feild, so to truly master it you will need some formal education.")
        st.image("../visualizations/images/degree.png")

        st.write("After mastering ML/DS where will you be employed? These are the leading industries that are hiring Data Scientists")
        st.image("../visualizations/images/emp_industry.png")

        st.write("There are lots of misconceptions related to ML/DS that we need a powerfull system to do any kind of ML/DS, We found that most of the Data Scientists use regular laptop for their day to day use!")
        st.image("../visualizations/images/hardware.png")

        st.write("Here is how you can practice and start your ML/DS journey")
        st.image("../visualizations/images/how_learnt.png")

    elif exp == "No Idea" and edu == "PostGrad":
        st.write("So you don't have much idea about data science")
        st.image("../visualizations/images/language.png")

        st.write("ML/DS is a very technical feild, so to truly master it you will need some formal education.")
        st.image("../visualizations/images/degree.png")

        st.write("After mastering ML/DS where will you be employed? These are the leading industries that are hiring Data Scientists")
        st.image("../visualizations/images/emp_industry.png")

        st.write("There are lots of misconceptions related to ML/DS that we need a powerfull system to do any kind of ML/DS, We found that most of the Data Scientists use regular laptop for their day to day use!")
        st.image("../visualizations/images/hardware.png")

        st.write("Here is how you can practice and start your ML/DS journey")
        st.image("../visualizations/images/how_learnt.png")

    elif exp == "No Idea" and edu == "PhD":
        st.write("So you don't have much idea about data science")
        st.write("Wow a PhD student starting DS/ML! its never too late to learn a new skill!")
        st.image("../visualizations/images/language.png")

        st.image("There are lots of new papers published for DS/ML each day, here is a plot to see how much the average number of papers have increased in past decade.")
        st.image("../visualizations/images/averagePapersPublisedPerDay.png")

        st.write("ML/DS is a very technical feild, so to truly master it you will need some formal education.")
        st.image("../visualizations/images/degree.png")

        st.write("After mastering ML/DS where will you be employed? These are the leading industries that are hiring Data Scientists")
        st.image("../visualizations/images/emp_industry.png")
        
        st.write("ML and AI are one of the most opted subjects by PhD students, here is a plot to show the rapid rise in popularity of ML/AI")
        st.image("../visualizations/images/growth_ml.png")

        st.write("There are lots of misconceptions related to ML/DS that we need a powerfull system to do any kind of ML/DS, We found that most of the Data Scientists use regular laptop for their day to day use!")
        st.image("../visualizations/images/hardware.png")

        st.write("Here is how you can practice and start your ML/DS journey")
        st.image("../visualizations/images/how_learnt.png")

        st.write("Here are the people who are best in this feild, its highly recommended to follow them and their work to stay updated!")
        st.image("../visualizations/images/TopPopularAuthors.png")


    # Beginner #######################
    elif exp == "Beginner" and edu == "High School":
        st.write("Let us help you to get started in Data Science")
        st.write("You are in High school, super enthusisastic about data science")

        st.write("Now that you can consider yourself as beginner in DS/ML, you might be wondering what are the employment statistics for Data Science? We used Kaggle survey data of 2017 and 2018 to compile the employment status.")
        st.image("../visualizations/images/employment.png")

        st.write("Now that you have basic concepts of DS/ML, next step will be to master it, and for that you will have to spend at least 2-10 hours a week.")
        st.image("../visualizations/images/time_spent.png")

    elif exp == "Beginner" and edu == "Undergrad":
        st.write("Hey have a look at Data Science")
        st.write("You are in Undergrad, very eager to know about data science")

        st.write("Lets see how much Undergrad students constitute the total DS/ML community and which method they used to learn it.")
        st.image("../visualizations/images/ContributionByDegree.png")

        st.write("Now that you can consider yourself as beginner in DS/ML, you might be wondering what are the employment statistics for Data Science? We used Kaggle survey data of 2017 and 2018 to compile the employment status.")
        st.image("../visualizations/images/employment.png")

        st.write("Now that you have basic concepts of DS/ML, next step will be to master it, and for that you will have to spend at least 2-10 hours a week.")
        st.image("../visualizations/images/time_spent.png")

    elif exp == "Beginner" and edu == "PostGrad":
        st.write("Hey have a look at Data Science")

        st.write("These are the most used Algorithms in ML/DS community")
        st.image("../visualizations/images/algos.png")

        st.write("Lets see how much Undergrad students constitute the total DS/ML community and which method they used to learn it.")
        st.image("../visualizations/images/ContributionByDegree.png")

        st.write("Now that you can consider yourself as beginner in DS/ML, you might be wondering what are the employment statistics for Data Science? We used Kaggle survey data of 2017 and 2018 to compile the employment status.")
        st.image("../visualizations/images/employment.png")

        st.write("Now that you have basic concepts of DS/ML, next step will be to master it, and for that you will have to spend at least 2-10 hours a week.")
        st.image("../visualizations/images/time_spent.png")

    elif exp == "Beginner" and edu == "PhD":
        st.write("As a Phd scholar learning the basics of ML/DS would have been a breeze, now to truly master it you might need the information")

        st.write("These are the most used Algorithms in ML/DS community")
        st.image("../visualizations/images/algos.png")

        st.write("Now that you have basic concepts of DS/ML, next step will be to master it, and for that you will have to spend at least 2-10 hours a week.")
        st.image("../visualizations/images/time_spent.png")

        st.image("There are lots of new papers published for DS/ML each day, here is a plot to see how much the average number of papers have increased in past decade.")
        st.image("../visualizations/images/averagePapersPublisedPerDay.png")

        st.write("Lets see how much Undergrad students constitute the total DS/ML community and which method they used to learn it.")
        st.image("../visualizations/images/ContributionByDegree.png")

        st.write("ML and AI are one of the most opted subjects by PhD students, here is a plot to show the rapid rise in popularity of ML/AI")
        st.image("../visualizations/images/growth_ml.png")

        st.write("Here are the people who are best in this feild, its highly recommended to follow them and their work to stay updated!")
        st.image("../visualizations/images/TopPopularAuthors.png")


    # Expert ########################
    elif exp == "Expert" and edu == "High School":
        interest = st.sidebar.radio("What's your Key Interest", ('Computer Vision', 'NLP', 'Data Science'))
        st.write("You are in High school, super enthusisastic about data science")

        st.write("These are the most used Algorithms in ML/DS community")
        st.image("../visualizations/images/algos.png")

        st.write("As an expert at this feild you might wonder what methods are used in actual companies, here are the top few of them.")
        st.image("../visualizations/images/methods.png")

        st.write("ML/DS feild is rapidly evolving each year hence we get a new function/method almost each month. To be competent in this feild we need to keep learning the new methods that are available, here are the top few")
        st.image("../visualizations/images/ml_method.png")

        st.write("In real world senarios how often do we actually make new ML models? Turns out only quater of the time we need a purpose built ML/AI model.")
        st.image("../visualizations/images/prod.png")

    elif exp == "Expert" and edu == "Undergrad":
        interest = st.sidebar.radio("What's your Key Interest", ('Computer Vision', 'NLP', 'Data Science'))
        st.write("Hey, you look expreinced, let us explore some new concepts")

        st.write("Lets see how much Undergrad students constitute the total DS/ML community and which method they used to learn it.")
        st.image("../visualizations/images/ContributionByDegree.png")

        st.write("As an expert at this feild you might wonder what methods are used in actual companies, here are the top few of them.")
        st.image("../visualizations/images/methods.png")

        st.write("ML/DS feild is rapidly evolving each year hence we get a new function/method almost each month. To be competent in this feild we need to keep learning the new methods that are available, here are the top few")
        st.image("../visualizations/images/ml_method.png")

        st.write("In real world senarios how often do we actually make new ML models? Turns out only quater of the time we need a purpose built ML/AI model.")
        st.image("../visualizations/images/prod.png")

    elif exp == "Expert" and edu == "PostGrad":
        interest = st.sidebar.radio("What's your Key Interest", ('Computer Vision', 'NLP', 'Data Science'))
        st.write("Hey, you look expreinced, let us explore some new concepts")

        st.write("These are the most used Algorithms in ML/DS community")
        st.image("../visualizations/images/algos.png")

        st.write("Lets see how much Undergrad students constitute the total DS/ML community and which method they used to learn it.")
        st.image("../visualizations/images/ContributionByDegree.png")

        st.write("As an expert at this feild you might wonder what methods are used in actual companies, here are the top few of them.")
        st.image("../visualizations/images/methods.png")

        st.write("ML/DS feild is rapidly evolving each year hence we get a new function/method almost each month. To be competent in this feild we need to keep learning the new methods that are available, here are the top few")
        st.image("../visualizations/images/ml_method.png")

        st.write("In real world senarios how often do we actually make new ML models? Turns out only quater of the time we need a purpose built ML/AI model.")
        st.image("../visualizations/images/prod.png")

    elif exp == "Expert" and edu == "PhD":
        interest = st.sidebar.radio("What's your Key Interest", ('Computer Vision', 'NLP', 'Data Science'))
        st.write("Wow you are experienced AND a PhD student, there will be very little that we can tell you, but no knowledge goes wasted!")

        st.image("There are lots of new papers published for DS/ML each day, here is a plot to see how much the average number of papers have increased in past decade.")
        st.image("../visualizations/images/averagePapersPublisedPerDay.png")

        st.write("Lets see how much Undergrad students constitute the total DS/ML community and which method they used to learn it.")
        st.image("../visualizations/images/ContributionByDegree.png")

        st.write("ML and AI are one of the most opted subjects by PhD students, here is a plot to show the rapid rise in popularity of ML/AI")
        st.image("../visualizations/images/growth_ml.png")

        st.write("As an expert at this feild you might wonder what methods are used in actual companies, here are the top few of them.")
        st.image("../visualizations/images/methods.png")

        st.write("ML/DS feild is rapidly evolving each year hence we get a new function/method almost each month. To be competent in this feild we need to keep learning the new methods that are available, here are the top few")
        st.image("../visualizations/images/ml_method.png")

        st.write("In real world senarios how often do we actually make new ML models? Turns out only quater of the time we need a purpose built ML/AI model.")
        st.image("../visualizations/images/prod.png")

        st.write("Here are the people who are best in this feild, its highly recommended to follow them and their work to stay updated!")
        st.image("../visualizations/images/TopPopularAuthors.png")
