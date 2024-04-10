import streamlit as st
import plotly.express as px
import pandas as pd

# Sample dataframe
df = pd.DataFrame({
    'Category': ['Electronics', 'Electronics', 'Fashion', 'Fashion', 'Fashion', 'Home', 'Home', 'Home'],
    'Brand': ['Sony', 'Samsung', 'Nike', 'Adidas', 'Zara', 'IKEA', 'Home Depot', 'Target']
})

# Group brands by category
brands_by_category = df.groupby('Category')['Brand'].unique().reset_index()

# Streamlit app
st.title('Bubble Charts for Sellers')

# Dropdown to select seller
selected_category = st.selectbox('Select a Category', brands_by_category['Category'])

# Filter data for selected category
selected_brands = brands_by_category[brands_by_category['Category'] == selected_category]['Brand'].iloc[0]

# Plot bubble chart for selected seller
fig = px.scatter(x=[selected_category]*len(selected_brands),
                 y=[len(selected_brands)],
                 size=[len(selected_brands)],
                 color=[selected_category],
                 hover_name=selected_brands,
                 title=f'Brands in Category: {selected_category}',
                 labels={'y': 'Number of Brands', 'x': 'Category'},
                 size_max=30,
                 template='plotly_white')

# Hide axis labels
fig.update_layout(xaxis_showgrid=False, yaxis_showgrid=False)

# Show plot
st.plotly_chart(fig)
