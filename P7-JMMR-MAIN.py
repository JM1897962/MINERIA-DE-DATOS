import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("Defunciones-Covid-A2.csv")

def create_age_groups(df):
    age_groups = []
    for age in df['edad']:
        if age >= 0 and age <= 18:
            age_group = '0-18'
        elif age >= 19 and age <= 30:
            age_group = '19-30'
        elif age >= 31 and age <= 50:
            age_group = '31-50'
        else:
            age_group = '51-100'
        age_groups.append(age_group)
    df['age_group'] = age_groups

create_age_groups(df)

df['nacionalidad'] = df['nacionalidad'].astype(str)

colors = {'0-18': 'red', '19-30': 'green', '31-50': 'blue', '51-100': 'purple'}

def scatter_age_groups(df, x_column, y_column, label_column, k_neighbors):
    fig, ax = plt.subplots()
    labels = df[label_column].unique()

    for label in labels:
        filter_df = df[df[label_column] == label]
        ax.scatter(filter_df[x_column], filter_df[y_column], label=label, color=colors[label])

    ax.legend()
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title('Scatter Grupos de Edades')
    plt.savefig('SCATTER1.png')
    plt.show()

scatter_age_groups(df, 'edad', 'nacionalidad', 'age_group', k_neighbors=5)

def scatter_nationality_avg_age(df, x_column, y_column):
    fig, ax = plt.subplots()

    avg_age_by_nationality = df.groupby(x_column)[y_column].mean()
    unique_nationalities = avg_age_by_nationality.index

    colors = plt.cm.jet(np.linspace(0, 1, len(unique_nationalities)))

    for i, nationality in enumerate(unique_nationalities):
        avg_age = avg_age_by_nationality[nationality]
        ax.scatter(nationality, avg_age, label=nationality, color=colors[i])

    ax.legend()
    plt.xlabel(x_column)
    plt.ylabel(f'Promedio de {y_column}')
    plt.title(f'Scatter Plot de Nacionalidad contra el Promedio de {y_column}')
    plt.xticks(rotation=45)
    plt.savefig('SCATTER2.png')
    plt.show()

scatter_nationality_avg_age(df, 'nacionalidad', 'edad')

#Juan Manuel Martínez Ramírez
#1897962
