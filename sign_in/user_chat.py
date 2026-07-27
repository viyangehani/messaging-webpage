import pandas as pd
from ipywidgets import Button, Output, Text, VBox
from IPython.display import display
text_received = st.session_state["shared_string"]
df_received = st.session_state["shared_df"]
