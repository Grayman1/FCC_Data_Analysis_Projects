# Proposed Solution

import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult_data.csv')
    df.head()
    
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()
    #print(race_count)

    # What is the average age of men?
    average_age_men = round(df.loc[df['sex'] == 'Male', 'age'].mean(),1)
    #print(average_age_men)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df.loc[(df['education'] == 'Bachelors')].shape[0] / len(df))*100,1)
    #print(percentage_bachelors)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    # with and without `Bachelors`, `Masters`, or `Doctorate`

    higher_education = df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    #print(len(advanced_education))
    #print(advanced_education)
   
    lower_education = df[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    #print(len(lower_education))
    #print(lower_education)
    
      
    # percentage with salary >50K
    higher_education_rich = round(len(higher_education[higher_education['salary'] == '>50K'])/ len(higher_education)*100,1)
    lower_education_rich = round(len(lower_education[lower_education["salary"] == ">50K"]) / len(lower_education) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    #print(min_work_hours)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    
    num_min_workers = len(df[df["hours-per-week"] == min_work_hours])

    rich_min_workers = len(df[(df["hours-per-week"] == min_work_hours) & (df["salary"] == ">50K")])
    
    rich_percentage = round((rich_min_workers/ num_min_workers)*100,1)

    # What country has the highest percentage of people that earn >50K?
    # Reporting no. employees makikng >50K by native-country
    step_1 = (df.loc[df["salary"] == ">50K", "native-country"].value_counts())
    #print('step_1', step_1)

    # Reporting total employees by native-country
    step_2 = df["native-country"].value_counts()
    #print('step_2', step_2)

    # Report country with highest % of employees earning >50K
    #step_3C = (step_1 / step_2).fillna(0).sort_values(ascending=False).index[0]
    #print('step_3C', step_3C)
    highest_earning_country = (step_1 / step_2).fillna(0).sort_values(ascending=False).index[0]
    #print('hightest_earning_country', hightest_earning_country)

    # Number of country's employees earning >50
    step_4 = len(df[(df["native-country"] == highest_earning_country) & (df["salary"] == ">50K")])
    #print('step_4', step_4)
    # Numboer of country's employees earning >50
    step_5 = len(df[df["native-country"] == highest_earning_country])
    #print('step_5', step_5)

    highest_earning_country_percentage = round(step_4 / step_5*100, 1)

    #print('highest_earning_country_percentage', highest_earning_country_percentage)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation =  df.loc[df["native-country"] == "India", 'occupation'].value_counts().sort_values(ascending=False).index[0]
    #print(most_popular_IN)



    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
