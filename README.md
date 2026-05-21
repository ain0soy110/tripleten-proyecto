# tripleten-proyecto

# Cuadro de Mando de Anuncios de Venta de Coches

Este proyecto es una aplicación web interactiva desarrollada en Python utilizando Streamlit. La aplicación funciona como un cuadro de mando dinámico que analiza un conjunto de datos sobre anuncios de venta de vehículos en los Estados Unidos (`vehicles_us.csv`).

## ¿Para qué sirve la aplicación?
El objetivo principal de la aplicación es facilitar el Análisis Exploratorio de Datos (EDA) de manera visual y accesible para cualquier usuario, permitiendo identificar rápidamente tendencias de precios, distribuciones de kilometraje y correlaciones clave en el mercado automotriz sin necesidad de escribir código.

## Funcionalidades principales
La aplicación proporciona herramientas visuales interactivas construidas con Plotly Express:

*   Visualización de Distribuciones: Incluye un componente interactivo para generar un histograma que muestra cómo se distribuyen los kilómetros recorridos (odometer) de los vehículos en venta.
*   Análisis de Relaciones: Incluye un componente interactivo para generar un gráfico de dispersión (scatter plot) que analiza la relación directa entre el kilometraje de los autos y sus precios de venta.
*   Interactividad en Tiempo Real: Los gráficos se renderizan de manera dinámica en la página mediante controles de usuario, permitiendo activar o desactivar las visualizaciones al instante.

## Tecnologías utilizadas
*   Python 3
*   Streamlit (Interfaz web)
*   Pandas (Manipulación y limpieza de datos)
*   Plotly (Gráficos interactivos)

## Despliegue
La aplicación web se encuentra desplegada y completamente en vivo en los servidores de Render; https://tripleten-proyecto.onrender.com/