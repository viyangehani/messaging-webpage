import pandas as pd # allows dataframe usage
import tkinker as tk # creates images
from datetime import datetime # tells time
name = st.session_state["user's name"] # helps send in messages and organize
df=pd.read_csv("messages.csv")
root = tk.Tk() 
def handle_submit():
  global df
  global name
  message = user_entry.get()
  time = datetime.now()
  new_message = {"user":name, "message":message, "time":time}
  message_send = pd.DataFrame([new_message])
  df=pd.concat([df, message_send], ignore_index = False )
  df.to_csv("messages.csv", index=False)
  user_entry.delete(0, tk.END)
bottom_frame = tk.Frame(root)
bottom_frame.pack(side="bottom", fill="x", padx=20, pady=20)
icon = tk.PhotoImage(file="send_icon.png")
submit_btn = tk.Button(bottom_frame, image=icon, command=handle_submit)
submit_btn.pack(side="right")
user_entry = tk.Entry(bottom_frame, font=("Arial", 11))
user_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
