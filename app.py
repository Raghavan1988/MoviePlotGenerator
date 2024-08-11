import streamlit as st
import requests
import json
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI()

# Set your OpenAI API key
# openai.api_key = 'your_openai_api_key'

# Function to generate a movie plot based on genres, optional plot twist, and a reference movie
def generate_movie_plot(genre1, genre2, plot_twist, movie):
    prompt = f"Create a detailed plot of a movie that would make as much money as the movie '{movie}'. The movie should be a mix of the genres '{genre1}' and '{genre2}'. If provided, include a plot twist: '{plot_twist}'. Include a last section that explains why the plot matches both genres and how the plot twist is incorporated, how is it similar to movie mentioned input"
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a creative movie plot generator."},
            {"role": "user", "content": prompt}
        ]
    )
    
    plot = response.choices[0].message.content.strip()
    return plot

# Streamlit app
def main():
    st.title("NoirCat Writes Movie Plots")

    genre1 = st.text_input("Primary Genre:")
    genre2 = st.text_input("Mix with which Genre:")
    plot_twist = st.text_input("Gimme a Plot Twist:", placeholder="No Twist")
    movie = st.text_input("Reference Box Office Hit:")

    if st.button("GO"):
        if not genre1 or not genre2 or not movie:
            st.error("Please provide all the required inputs: Genre 1, Genre 2, and a reference movie.")
        else:
            plot = generate_movie_plot(genre1, genre2, plot_twist, movie)
            plot_html = plot ##markdown.markdown(plot)
            st.markdown(plot_html, unsafe_allow_html=True)

# Add this CSS code to the Streamlit app
st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        background-color: green;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)


if __name__ == '__main__':
    main()

