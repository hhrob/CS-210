import matplotlib.pyplot as plt
import csv
import numpy
import statistics
# Write your functions here
def load_data(file_name,types):
    new_dict = {}

    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        cols = next(reader)

        for key in types:
            new_dict[(key, types[key])] = []

        for line in csv.reader(f):
            i = 0
            for key,val in types.items():
                new_dict[(key, val)].append(val(line[i]))
                i += 1

    return new_dict

def summarize(data):
    for key, value in data.items():
        if all(isinstance(v, (int, float)) for v in value):
            print(f'Statistics for {key[0]}:')
            print("    min:", '{:>6}'.format(float(round(min(data[key]),1))))
            print('    max:', '{:>6}'.format(float(round(max(data[key]),1))))
            print('   mean:', '{:>6}'.format(float(round(statistics.mean(data[key]),1))))
            print('  stdev:', '{:>6}'.format(float(round(statistics.stdev(data[key]),1))))
            print('   mode:', '{:>6}'.format(float(round(statistics.mode(data[key]),1))))
        else:
            print(f'Statistics for {key[0]}:')
            print('Number of unique values:', len(numpy.unique(data[key])))
            print('      Most common value:', statistics.mode(data[key]))
    return None

def pearson_corr(x,y):
    if len(x) != len(y):
        raise ValueError("The list parameters must have the same number of elements.")
    for i in x:
        if type(i) == str:
            raise ValueError('pearson_corr only works with int or float lists.')
    for i in y:
        if type(i) == str:
            raise ValueError('pearson_corr only works with int or float lists.')
    else:
        return round((numpy.corrcoef(x, y)[0, 1]),2)

def survivor_vis(data,col_1,col_2, label1, label2):
    x_survive, y_survive, x_died, y_died = [],[],[],[]
    for i in range(len(col_1)):
        if data[('Survived',int)][i] == 1:
            x_survive.append(col_1[i])
            y_survive.append(col_2[i])
        else:
            x_died.append(col_1[i])
            y_died.append(col_2[i])
    plt.title('Survivor Visualization')
    plt.scatter(x_survive, y_survive, color='green', marker='o', label='Survived')
    plt.scatter(x_died, y_died, color='red', marker='x', label='Died')
    plt.xlabel(label1), plt.ylabel(label2)
    plt.legend()
    plt.show()

# ------ You shouldn't have to modify main --------
def main():
    """Main program driver for Project 3."""

    # 3.1 Load the dataset
    titanic_types = {'PassengerId': int, 'Survived': int, 'Pclass': int,
                     'Sex': str, 'Age': float, 'SibSp': int, 'Parch': int,
                     'Fare': float, 'Embarked': str, 'FamilySize': int,
                     'age_group': str}
    data = load_data('proj7/titanic_clean.csv', titanic_types)

    # 3.2 Print informative summaries
    print("\nPart 3.2")
    summarize(data)

    print("\nPart 3.3")
    # 3.3 Compute correlations between age and survival
    corr_age_lived = pearson_corr(data[('Age', float)], data[('Survived', int)])
    print(f'Correlation between age and survival is {corr_age_lived:3.2f}')

    # 3.3 Correlation between fare and survival
    corr_fare_lived = pearson_corr(data[('Fare', float)], data[('Survived', int)])
    print(f'Correlation between fare and survival is {corr_fare_lived:3.2f}')

    # 3.3 Correlation between family size and survival
    corr_fare_lived = pearson_corr(data[('FamilySize', int)], data[('Survived', int)])
    print(f'Correlation between family size and survival is' f' {corr_fare_lived:3.2f}')

    # 3.4 Visualize results
    fig = survivor_vis(data, data[('Age', float)], data[('Fare', float)], 'Age', 'Fare')
    fig = survivor_vis(data, data[('Age', float)], data[('Pclass', int)], 'Age', 'Pclass')
    fig = survivor_vis(data, data[('Age', float)], data[('Parch', int)], 'Age', 'Parch')

if __name__ == "__main__":
    main()

 


