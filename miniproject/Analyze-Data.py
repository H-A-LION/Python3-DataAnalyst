import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('Chocolate Sales.csv')

# Clean the "Amount" column
df['Amount'] = df['Amount'].replace('[\$,]', '', regex=True).astype(float)

# Group by Country and calculate total sales
total_sales_per_country = df.groupby('Country')['Amount'].sum().reset_index()

# Plot the bar chart
plt.figure(figsize=(10, 6))
plt.bar(total_sales_per_country['Country'], total_sales_per_country['Amount'], color='skyblue')
plt.title('Total Sales Amount per Country')
plt.xlabel('Country')
plt.ylabel('Total Sales Amount ($)')
plt.xticks(rotation=45)
plt.show()

# Group by Product and calculate total boxes shipped
boxes_per_product = df.groupby('Product')['Boxes Shipped'].sum().reset_index()

# Plot the pie chart
plt.figure(figsize=(8, 8))
plt.pie(boxes_per_product['Boxes Shipped'], labels=boxes_per_product['Product'], autopct='%1.1f%%', startangle=140)
plt.title('Number of Boxes Shipped per Product Type')
plt.show()

# Convert the "Date" column to datetime
df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%y')

# Group by Date and calculate total sales
sales_over_time = df.groupby('Date')['Amount'].sum().reset_index()

# Plot the line graph
plt.figure(figsize=(10, 6))
plt.plot(sales_over_time['Date'], sales_over_time['Amount'], marker='o', color='green')
plt.title('Sales Amount Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales Amount ($)')
plt.xticks(rotation=45)
plt.show()



# Plot the scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df['Amount'], df['Boxes Shipped'], color='orange', alpha=0.5)
plt.title('Correlation Between Sales Amount and Boxes Shipped')
plt.xlabel('Sales Amount ($)')
plt.ylabel('Boxes Shipped')
plt.show()

# Calculate the correlation coefficient
correlation = df['Amount'].corr(df['Boxes Shipped'])
print(f"Correlation Coefficient: {correlation:.2f}")
