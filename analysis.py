import pandas as pd
import plotly.express as px
df2=pd.read_csv('Retail sales analysis.csv')

df = pd.DataFrame(df2)

# Convert 'Sales' to float
df['Sales'] = df['Sales'].astype(float)

# Convert 'Order Date' to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

df['Year'] = df['Order Date'].dt.year
df_yearly_sales = df.groupby('Year')['Sales'].sum().reset_index()
df['Month'] = df['Order Date'].dt.month_name()

# Get unique years for dropdown
years = df['Year'].unique()
years=list(years)
years.sort()
# Create a dropdown with years
dropdown = years  

# Create a bar chart using Plotly Express
fig = px.bar(df_yearly_sales, x='Year', y='Sales', title='Yearly Sales Analysis')
fig.update_layout(xaxis_title='Year', yaxis_title='Total Sales')

fig.update_layout(updatemenus=[
            dict(type='buttons',
                 showactive=False,
                    buttons=[dict(label='All Years',
                       method='update'),
                         *[
                        dict(label=str(years),
                              method='update'
                              )                  ]
                     ])],
         showlegend=False
        )

# Display the plot
fig.show()


