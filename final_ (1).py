# A terminal based knowledge game based on a chosen country's average population from 2000-2020, the year with the minimum population from 2000-2020, the most endangered species over this time, and which continent the country belongs to.

import numpy as np      # Import the module numpy for arrays and calculations
import matplotlib.pyplot as plt     # Import matplotlib for plotting
    

class Country:     
    ''' A class used to create an object Counrty

            Attributes:
                name (str): String that represents the chosen country's name
                mean_population (int): Integer that represents the average population of the chosen country from 2000-2020
                species (str): String that represents the most endangered species of the chosen country
                continent (str): String that represents the continent of the chosen country
    '''
    def __init__(self, name, mean_population, species, continent):
        self.name = name
        self.mean_population = mean_population
        self.species = species
        self.continent = continent
    
    def print_all_stats(self):
        '''A function that prints the name, mean population, most endangered species and continent of the country instsance.

        Parameters: None
        Returns: None

        '''
        format_string = '{title:<26}{answer:^30}'
        print('\nYour Selected Country')
        print('-'*56)
        print(format_string.format(title='Country Name:',answer=self.name))
        print(format_string.format(title='Mean Population:',answer=self.mean_population))
        print(format_string.format(title='Most Endangered Species:',answer=self.species))
        print(format_string.format(title='Continent:',answer=self.continent))
        print()


def answer_1(population, column):
    ''' A function that takes in the country data array, and the row the selected country is on, and calculates the mean population using the numpy.mean function.
    
    Parameters: 
        population: an array 
    Returns: The average population over 20 years

    '''
    ans1=int(np.mean(population[column, 1:]))
    return ans1

def answer_2(population, column, years):
    min_pop_c,min_pop_r = np.where(population == (np.min(population[column, 1:])))
    year_index_dict=dict(zip(min_pop_c,min_pop_r))
    i=(column[0])
    index_years=(year_index_dict[i])-1        
    ans2=(range(int((years[index_years])-2),int((years[index_years]+3))))
    ans2=years[index_years]
    return ans2

def answer_3(species, column):
    max_species_c,max_species_r = np.where(species == (np.max(species[column, 1:])))
    spec_index_dict=dict(zip(max_species_c,max_species_r))
    i=(column[0])
    index_animals=(spec_index_dict[i])-1
    animals=['Plants','Fish','Birds','Mammals']
    ans3=(str(animals[index_animals]))
    return ans3


def answer_4(data, column, row):
    ans4_array=(data[column, row+1])
    ans4=str(ans4_array[0])
    return ans4

def max_pop_year(population, column, years):
    max_pop_c,max_pop_r = np.where(population == (np.max(population[column, 1:])))
    year_index_dict=dict(zip(max_pop_c,max_pop_r))
    i=(column[0])
    index_years=(year_index_dict[i])-1       
    max_year=years[index_years]
    return max_year

def main():
    country_names = np.genfromtxt('Country_Data.csv', delimiter= ',', skip_header = True, dtype=str)
    population = np.genfromtxt('Population_Data.csv', delimiter= ',', skip_header = True)
    threatened_species = np.genfromtxt('Threatened_Species.csv', delimiter= ',', skip_header = True)
    years_array = np.array([2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])
    format_title = '{title:^75}'
    print(format_title.format(title = 'xXxCOUNTRY KNOWLEDGE GAMExXx\n'))
    pick_country = input(f'{country_names[:,0]} \nPlease pick a country from this list: ')
    while pick_country not in country_names:
        print('Not a valid country, please check your spelling and enter again')
        pick_country = input('Please pick a country from this list: ')
    index1, index2 = np.where(country_names == pick_country)

        
    ans1_range = range(int(answer_1(population,index1)-(answer_1(population,index1)*0.20)),int(answer_1(population,index1)+((answer_1(population,index1)*0.20))+1))
    #print(ans1_range)
    ans2_range = range(int(answer_2(population, index1, years_array)-2),int(answer_2(population, index1, years_array)+3))

    question = {f'What is the mean population of {pick_country} from 2000-2020? (Guess within 20% for a point) ':ans1_range, 
    f'When was the lowest population of {pick_country} from 2000-2020? (Guess within 2 years for a point) ' : ans2_range, 
    f'Does {pick_country} have more endangered plants, fish, birds, or mammals? (Guess the species for a point) ': answer_3(threatened_species, index1).lower(), 
    f'What region is {pick_country} in? (Americas, Asia, Oceania, Africa, Europe) ': answer_4(country_names, index1, index2).lower()}
    answers = [answer_1(population, index1), answer_2(population, index1, years_array), answer_3(threatened_species, index1), answer_4(country_names, index1, index2)]
    pt=0
    n=0
    counter = 0

    for i in question:
        ans = input(i)
        while counter < 2 and ans.isnumeric() != True:
            ans = input(i)
        while counter >= 2 and ans.isalpha() != True:
            ans = input(i)
        if ans.isnumeric() and counter < 2:
            num_ans = int(ans)
            if num_ans in question[i]:
                print(question[i])
                pt+=1
                print(f'You\'re a GENIUS\nPoints: {pt}')
            else:
                print(f'Wrong\nPoints: {pt}')
        elif ans.lower() == question[i]:
            pt+=1
            print(f'You\'re a GENIUS\nPoints: {pt}')

        else:
            print(f'Wrong\nPoints: {pt}')
        print(f'Answer is: {answers[n]}')
        n+=1
        counter += 1
    print(f'You have scored {(((pt)/4)*100):.0f}%!')

    if pt == 4:
        print('WOW, you are a master of', pick_country)
    elif pt >= 2:
        print('Good Job!')
    else:
        print('Better luck next time!')

    chosen_country = Country(pick_country, answer_1(population, index1), answer_3(threatened_species, index1), answer_4(country_names, index1, index2))
    chosen_country.print_all_stats()

    x_axis=years_array

    y_pop=(population[index1, 1:])
    y=y_pop.flatten()
    mean_pop=answer_1(population, index1)
    mean=[]
    for i in range(len(x_axis)):
        mean.append(mean_pop)

    plt.plot(x_axis, y)
    plt.plot(x_axis,mean, '--', color='orange', label=f'Population Mean = {mean_pop}')
    plt.title(f'Population of {pick_country}')
    plt.ylabel('Population')
    plt.xlabel('Year')
    plt.xticks(np.arange(2000,2021,2))
    plt.scatter([answer_2(population, index1, years_array)], [np.min(population[index1, 1:])], marker='x',color='magenta', label=f'Population Minimum = {int(np.min(population[index1, 1:]))}')
    plt.scatter([max_pop_year(population, index1, years_array)], [np.max(population[index1, 1:])], marker='x',color='cyan', label=f'Population Maximum = {int(np.max(population[index1, 1:]))}')
    plt.legend(loc = 'best', shadow = True)
    plt.show()

    x_axis=['Plants','Fish','Birds','Mammals']
    y_axis = threatened_species[index1, 1:]
    y=y_axis.flatten()

    plt.bar(x_axis, y)
    plt.bar([answer_3(threatened_species, index1)], [np.max(threatened_species[index1, 1:])], color='red', label='Most Endangered Species')
    plt.title(f'Threatened Species in {pick_country}')
    plt.xlabel('Threatened Species')
    plt.ylabel('Count')
    plt.legend(loc = 'best', shadow = True)
    plt.show()


if __name__ == '__main__':
    main()