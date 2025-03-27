Restaurant Name & Menu Generator
Overview
This project generates a restaurant name and menu items based on a selected cuisine. It leverages LangChain and OpenAI's GPT model to create meaningful and creative outputs. The interface is built with Streamlit.

Features
Select a cuisine from a sidebar dropdown.

Generate a restaurant name based on the cuisine.

Get a list of menu items for the generated restaurant.

Simple and interactive web UI using Streamlit.

Installation
Prerequisites
Python 3.x

OpenAI API Key

Streamlit

Steps
Clone the repository:
```
git clone https://github.com/Partha-png/resturant-name-generator.git
```
2.Install dependencies:
```
pip install -r requirements.txt
```
Set up your OpenAI API Key:

Create a file openai_key.py and define:
```
openai_key = "your_openai_api_key"
```
Run the Streamlit app:
```
streamlit run main.py
```
Project Structure
```
📂 project-folder/
│-- main.py                # Streamlit app interface
│-- langchain_code.py       # Handles LangChain-based name & menu generation
│-- openai_key.py           # Stores OpenAI API Key (not to be shared)
│-- requirements.txt        # Dependencies
```
Usage
Open the app in your browser.

Select a cuisine from the sidebar.

View the generated restaurant name and menu items.

Technologies Used
LangChain (for prompt management and chaining)

OpenAI GPT API (for generating text-based outputs)

Streamlit (for UI/UX)

Future Enhancements
Support for more cuisines.

Add pricing suggestions for menu items.

Allow user customization of the menu.
