import pandas as pd
import streamlit as st
import plotly.express as px

dfPoliza = pd.read_excel("https://github.com/arianasauri2110/STREAMLIT-ARIANA-/blob/main/ConsultaPagos.xlsx?raw=true")
#dfPoliza = pd.read_excel("C:\\Users\\Ariana Sauri\\OneDrive\\Documentos\\PROYECTO HERRAMIENTAS\\Consultapagos.xlsx")
dfPoliza.head()
dfPoliza.columns

# DISTRIBUCIÓN DE SEGUROS Y ASEGURADORAS
df= dfPoliza[["ASEGURADORA","SEGURO","FECHA_INICIO"]]
df
dfPoliza["ASEGURADORA"].unique()
dfPoliza["SEGURO"].unique()
dfPoliza["ASEGURADORA"].value_counts()
dfPoliza["SEGURO"].value_counts()

#GRAFICO POR TIPO DE SEGURO
dfSeguros= dfPoliza ["SEGURO"].value_counts().to_frame()
dfSeguros.columns
dfSeguros

#REMOVEMOS EL INDEX
dfSeguros.reset_index(inplace=True)

#CAMBIAMOS NOMBRE DE LAS COLUMNAS
dfSeguros.rename(columns={"index":"Tipo de seguro", "SEGURO":"Total"},inplace=True)
dfSeguros.columns
fig= px.bar(dfSeguros, x="Tipo de seguro", y= "Total", title= "Distribución de tipos de seguros")
st.plotly_chart(fig, use_container_width=True)

#GRAFICA POR ASEGURADORA
dfAseguradora= dfPoliza ["ASEGURADORA"].value_counts().to_frame()
dfAseguradora.columns
dfAseguradora
dfAseguradora.reset_index(inplace=True)
dfAseguradora.rename(columns={"index":"Aseguradora", "ASEGURADORA":"Total"},inplace=True)
dfAseguradora.columns
fig= px.bar(dfAseguradora, x="Aseguradora", y= "Total", title= "Distribución de aseguradoras")
st.plotly_chart(fig, use_container_width=True)

#GRAFICA DE PIE POR TIPOS DE SEGUROS
fig= px.pie (df, values=df["SEGURO"].value_counts().values, names=df["SEGURO"].value_counts().index)
st.plotly_chart(fig, use_container_width=True)

#GRAFICA DE PIE POR ASEGURADORAS
fig= px.pie (df,values=df["ASEGURADORA"].value_counts().values, names=df["ASEGURADORA"].value_counts().index)
st.plotly_chart(fig, use_container_width=True)

#AGRUPACION DE ASEGURADORAS POR TIPO DE SEGURO.
df.groupby(["ASEGURADORA","SEGURO"]).count()
df_stack=df.groupby(["ASEGURADORA","SEGURO"]).size().reset_index()
df_stack.columns
df_stack.rename(columns={0:"Total"},inplace=True)
fig= px.bar(df_stack, x= "ASEGURADORA",y="Total",color="SEGURO", barmode ="stack")
st.plotly_chart(fig, use_container_width=True)
