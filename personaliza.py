import streamlit as st
import pandas as pd
from PIL import Image

#tutorial https://www.youtube.com/watch?v=WC4_YpdgE18&list=PL7HAy5R0ehQXnHqAEJUNb1ci_24cUQ4L5

#LLamda a las tablas de datos en formato csv
clientes=pd.read_csv("clientes.csv").sort_values(by="nombre")
productos=pd.read_csv("productos.csv") #.sort_values(by="producto")
ventas=pd.read_csv("ventas.csv")
abonos=pd.read_csv("abonos.csv")


img=Image.open(".streamlit/Basicos/ame.png") #copy path
st.set_page_config(page_title="Personalizado",page_icon=img, layout="wide", initial_sidebar_state="collapsed")

def main():
    st.title("Personalizado  ")
    st.sidebar.header("Menu Principal")

    menu=["inicio","clientes","productos","ventas","abonos","edo cuenta","formulario"]
    eleccion=st.sidebar.selectbox("Elige una opcion",menu) #eleccion guarda el valor elegido

    if eleccion=="inicio":
        st.subheader("Hola, Bienvenido a la aplicacion Web") 
        st.write("""
                 Esta aplicacion esta desarrollada para llevar el control de:
                - clientes y
                - productos
                 """)

    elif eleccion=="clientes":
      st.subheader("Lista de Clientes")
      st.dataframe(clientes[["nombre","phone"]],width=400,height=400)

    elif eleccion=="productos":
      st.subheader("Lista de Productos") 
      st.dataframe(productos)

    elif eleccion=="ventas":
       st.subheader("Ventas de clientes")  
       st.dataframe(ventas)  

    elif eleccion=="abonos":
       st.subheader("Abonos de clientes")  
       st.dataframe(abonos,width=600,height=400)

    elif eleccion=="edo cuenta":
        st.subheader("Estado de cuenta de clientes") 

        with st.form(key="subtotal", clear_on_submit=True): #se limpia el formulario cuando se presiona el boton
           col1, col2, col3 = st.columns(3)

           with col1:
              precio=st.number_input("Precio Producto", min_value=0.0)
           with col2:
              cantidad=st.number_input("numero de piezas", min_value=0, max_value=3)
           with col3:
              calc=st.form_submit_button("Calcular")

        if calc:
           subtot=precio*cantidad
           st.write("El precio a pagar es", subtot)
              
                 


    elif eleccion=="formulario":
        st.subheader("Formulario de clientes")   

        #llamado a formulario
        with st.form(key="formulario_basico", clear_on_submit=True):  
           st.write("Formulario de Registro")
           nombre=st.text_input("Nombre:")
           telefono=st.text_input("Telefono")
           boton_enviar=st.form_submit_button(label="Registrarse")
        if boton_enviar:
           st.success(f"Hola {nombre}, tu cuenta ha sido creada")   


    #graficos min 33.40

    #carga de archivos






if __name__=='__main__':
    main()
    

#para ejecutar el codigo:
#streamlit run /workspaces/pythoncode/Streamlit/personaliza.py     