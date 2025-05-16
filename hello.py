import pandas as pd
import plotly.express as px
import preswald

# Load dataset
df = pd.read_csv('data/titanic.csv')

# Show data table
preswald.text("# Titanic Dataset 🛳️")
preswald.table(df)

# Survival rate by gender
fig1 = px.bar(
    df.groupby('Sex')['Survived'].mean().reset_index(),
    x='Sex',
    y='Survived',
    title='Survival Rate by Gender',
    labels={'Survived': 'Survival Rate'}
)
preswald.plotly(fig1)

# Survival rate by class
fig2 = px.bar(
    df.groupby('Pclass')['Survived'].mean().reset_index(),
    x='Pclass',
    y='Survived',
    title='Survival Rate by Class',
    labels={'Survived': 'Survival Rate', 'Pclass': 'Class'}
)
preswald.plotly(fig2)
