import pandas as pd
import tkinker as tk
from datetime import datetime
name = st.session_state["user's name"]
df=pd.read_csv("messages.csv")

def handle_submit():
  global df
  global name
  message = user_entry.get()
  time = datetime.now()
  new_message = {"user":name, "message":message, "time":time}
  message_send = pd.DataFrame([new_message])
  df=pd.concat([df, message_send], ignore_index = False )
  
  user_entry.delete(0, tk.END)

root = tk.Tk() 
