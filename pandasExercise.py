import pandas as pd
import matplotlib.pyplot as plt


def read_data(file_name):
    return pd.read_csv(file_name)


def common_class(data):
    recurrence = 0
    noRecurrence = 0
    for i,j in data.iterrows():
        if data.iloc[i]['Class'] != "?":
            if data.iloc[i]['Class'] == "no-recurrence-events":
                noRecurrence += 1
            else:
                recurrence += 1
    return {"no-recurrence": noRecurrence} if recurrence < noRecurrence else {"recurrence": reecurrence}


def common_age_and_menopause_w_recurrence(data):
    age = {}
    menopause = {}
    for i,j in data.iterrows():
        if data.iloc[i]['Class'] != "?":
            if data.iloc[i]['Class'] == "recurrence-events":
                age[data.iloc[i]['age']] =  age.get(data.iloc[i]['age'], 0) + 1
                if data.iloc[i]['menopause'] != "premeno":
                    menopause[data.iloc[i]['menopause']] = menopause.get(data.iloc[i]['menopause'], 0) + 1
       
    return (age, menopause, max(age, key=age.get), max(menopause, key=menopause.get))


def plot_recurrences(frequencies):
    df4 = pd.DataFrame(frequencies, columns= [freq for freq in frequencies], index=[0])
    df4.plot.bar(alpha=0.5)


if __name__ == '__main__':
    print(common_class(read_data("breast-cancer.data")))
    age, menopause, max_age, max_meno= common_age_and_menopause_w_recurrence(read_data("breast-cancer.data"))
    print(age, max_age)
    print(menopause, max_meno)
    plot_recurrences(age)
