import pandas as pd
from ipywidgets import Button, Output, Text, VBox
from IPython.display import display
def switch_page(name_of_user,chat_list):
  # Save your string and dataframe into labeled memory boxes
  st.session_state["user's name"] = name_of_user
  st.session_state["user's chats"] = chat_list

  # Trigger the transition
  st.session_state.script = "user_chat.py"
  st.rerun()
username_input = Text(description='input your username:')
password_input = Text(description='input your password:')
name_input = Text(description='input your name:')
def submit():
  
