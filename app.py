import streamlit as st
import pandas as pd
import plotly.express as px

vehicles_df = pd.read_csv('../vehicles_us.csv')

#Snake case
vehicles_df.columns = (
    vehicles_df.columns
    .str.strip()             
    .str.lower()             
    .str.replace(' ', '_')   
)

# 1. Tratamiento de Categóricas y Binarias
vehicles_df['paint_color'] = vehicles_df['paint_color'].fillna('unknown')
vehicles_df['is_4wd'] = vehicles_df['is_4wd'].fillna(0)

#2. Tratamiento de Numéricas 
vehicles_df = vehicles_df.dropna(subset=['model_year', 'cylinders', 'odometer'])

vehicles_df = vehicles_df.reset_index(drop=True)

# 3. Verificación de nulos
print(vehicles_df.isna().sum()) 


#Cambio a entero

columnas_a_entero = ['model_year', 'cylinders', 'odometer', 'is_4wd']

for col in columnas_a_entero:
    vehicles_df[col] = vehicles_df[col].astype(int)

#Graficas


# encabezado principal de la aplicación web
st.header('Cuadro de Mando: Análisis del Mercado de Vehículos Usados')

# Texto introductorio básico
st.write('Use los botones de abajo para generar las visualizaciones interactivas del dataset.')

st.subheader('Análisis de Distribución de Precios')

if st.button('Construir Histograma'):
    st.write('Generando histograma interactivo de precios con Plotly Express...')
    
    fig_hist = px.histogram(
        vehicles_df, 
        x='price', 
        title='Distribución de Precios de los Vehículos en Venta',
        labels={'price': 'Precio (USD)'},
        color_discrete_sequence=['#636EFA'],
        nbins=50
    )
    
    st.plotly_chart(fig_hist, use_container_width=True)

st.subheader('Análisis de Depreciación por Uso')

if st.button('Construir Gráfico de Dispersión'):
    st.write('Generando gráfico de dispersión interactivo (Precio vs. Odómetro) con Plotly Express...')
    
    fig_scatter = px.scatter(
        vehicles_df, 
        x='odometer', 
        y='price', 
        title='Relación entre el Kilometraje (Odómetro) y el Precio',
        labels={'odometer': 'Kilometraje (millas)', 'price': 'Precio (USD)'},
        opacity=0.4,
        color_discrete_sequence=['#EF553B']
    )
    
    st.plotly_chart(fig_scatter, use_container_width=True)