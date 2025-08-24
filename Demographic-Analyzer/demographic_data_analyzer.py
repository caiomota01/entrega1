import pandas as pd

def calculate_demographic_data(print_data=True):
    # Ler os dados
    df = pd.read_csv("adult.data.csv")

    # 1. Quantas pessoas de cada raça
    race_count = df['race'].value_counts()

    # 2. Idade média dos homens
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentual de pessoas com diploma de bacharel
    percentage_bachelors = round((df['education'].value_counts(normalize=True)['Bachelors'] * 100), 1)

    # 4. Educação avançada (Bachelors, Masters, Doctorate)
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # 5. % pessoas com educação avançada que ganham >50K
    higher_education_rich = round((higher_education[higher_education['salary'] == '>50K'].shape[0] 
                                   / higher_education.shape[0]) * 100, 1)

    # 6. % pessoas sem educação avançada que ganham >50K
    lower_education_rich = round((lower_education[lower_education['salary'] == '>50K'].shape[0] 
                                  / lower_education.shape[0]) * 100, 1)

    # 7. Número mínimo de horas trabalhadas por semana
    min_work_hours = df['hours-per-week'].min()

    # 8. % das pessoas que trabalham min de horas e ganham >50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] 
                             / num_min_workers.shape[0]) * 100, 1)

    # 9. País com maior % de pessoas >50K
    country_salary = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_total = df['native-country'].value_counts()
    highest_earning_country = (country_salary / country_total * 100).idxmax()
    highest_earning_country_percentage = round((country_salary / country_total * 100).max(), 1)

    # 10. Ocupação mais popular para pessoas >50K na Índia
    india_top_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    # Dicionário de resultados
    if print_data:
        print("Número de pessoas por raça:\n", race_count)
        print("Idade média dos homens:", average_age_men)
        print(f"Porcentagem de Bacharelado: {percentage_bachelors}%")
        print(f"% com educação avançada e >50K: {higher_education_rich}%")
        print(f"% sem educação avançada e >50K: {lower_education_rich}%")
        print("Mínimo de horas trabalhadas/semana:", min_work_hours)
        print(f"% dos que trabalham min horas e >50K: {rich_percentage}%")
        print("País com maior % >50K:", highest_earning_country, highest_earning_country_percentage)
        print("Trabalho mais popular na Índia (>50K):", india_top_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': india_top_occupation    # ✅ nome correto
    }

