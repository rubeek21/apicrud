#Tutorial: https://www.youtube.com/watch?v=QpYKVXDqyco&t=114s

import gspread
from oauth2client.service_account import ServiceAccountCredentials #pip oauh2client and pip google-cloud-store (for service aacountcreentials)
import streamlit as st
import pandas as pd

st.title("Simple Data Entry using Streamlit")

# Authenticate and connect to Google Sheets

scope = ["https://spreadsheets.google.com/feeds", 
        "https://www.googleapis.com/auth/drive"]
    
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    ".streamlit/webapp/credentials.json",
      scope,)

#se crea el cliente y se otorga acceso a traves de las credenciales que existen en el archivo json
client = gspread.authorize(credentials)

#se crea el objeto sheet, el cual se utilizara para leer/escribir en la hoja de excel compartida
hoja=1 # cambiar entre hoja de excel
sheet = client.open("Streamlit").get_worksheet(hoja) # cambiando el numero para buscar una hoja especifica

#sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1KnMZDl54vL-DzyaujJUE9g-5ZhBz9bM1/edit?usp=sharing&ouid=105653698796504229896&rtpof=true&sd=true") url donde se ubica el archivo compartido sin pasar por google drive
#sheet=client.open("Streamlit").worksheet("Sheet2")    para acceder a otra hoja de trabajo
#sheet=client.open("Streamlit").get_worksheet(1)    para acceder al numero de hoja: sheet1=0, sheet2=1

### Escribir informacion en una celda especifica
mensaje="por fin funciona esto"
#llamado al servicio de la API, procurar no meter el llamado en un ciclo para no hacer mas lento el proceso.
sheet.update_cell(3,3,mensaje)  #funciona!!!

###Leer informacion de una celda especifica
valor=sheet.col_values(3)[0:]  #(columna 3)[desde renglon 0 en adelante], el indice del primer renglon es 0
print(valor)

###leer toda la tabla
def read_data():
    todo=sheet.get_all_records()
    frame=pd.DataFrame(todo)
    print(frame)
    return frame

# Add Data to Google Sheets
def add_data(row):
    sheet.append_row(row)  # Append the row to the Google Sheet


# Sidebar form for data entry
with st.sidebar:
    st.header("Enter New Data")
    # Assuming the sheet has columns: 'Name', 'Age', 'Email'
    with st.form(key="data_form",clear_on_submit=True):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0, max_value=120)
        email = st.text_input("Email")
        # Submit button inside the form
        submitted = st.form_submit_button("Submit")
        # Handle form submission
        if submitted:
            if name and email:  # Basic validation to check if required fields are filled
                add_data([name, age, email])  # Append the row to the sheet
                st.success("Data added successfully!")
            else:
                st.error("Please fill out the form correctly.")

# Display data in the main view
st.header("Data Table")
df = read_data()
st.dataframe(df, width=800, height=400) 

#@rubeek21
###activando el modo .venv --> source /workspaces/pythoncode/.venv/bin/activate
#(.venv) @rubeek21
###correr App
###streamlit run /workspaces/pythoncode/.streamlit/webapp/app1.py