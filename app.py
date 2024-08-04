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
    prompt = f"Create a detailed plot of a movie that would make as much money as the movie '{movie}'. The movie should be a mix of the genres '{genre1}' and '{genre2}'. If provided, include a plot twist: '{plot_twist}'."
    
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
    st.title("Movie Plot Generator")

    genre1 = st.text_input("Enter Genre 1:")
    genre2 = st.text_input("Enter Genre 2:")
    plot_twist = st.text_input("Optional: Enter a Plot Twist:")
    movie = st.text_input("Enter a reference movie that made a lot of money:")

    if st.button("Generate Movie Plot"):
        if not genre1 or not genre2 or not movie:
            st.error("Please provide all the required inputs: Genre 1, Genre 2, and a reference movie.")
        else:
            plot = generate_movie_plot(genre1, genre2, plot_twist, movie)
            plot_html = plot ##markdown.markdown(plot)
            st.markdown(plot_html, unsafe_allow_html=True)

if __name__ == '__main__':
    main()

