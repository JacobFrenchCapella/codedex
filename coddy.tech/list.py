def values(lst):
    for i in range(len(lst)):
        print(lst[i])
def change_element(lst, index, new_element):
    lst[index] = new_element
    return lst
def merge(lst1, lst2):
    merged = lst1 + lst2
    merged.sort()
    return merged
def remove():
    pokemon = ['Reshiram', 'Mew', 'Oshawott', 'card']
    pokemon.append('Charmander')
    #This will add Charmander to the end of the list
    pokemon.remove('card')
    #This will remove Card
    pokemon.insert("Reshiram", "Zekrom")
    #This will add Zekrom after Reshiram
    pokemon.extend([1, 2])
    #This extends the list, with 1 and 2. It allows for more to be added instead of individual
    del pokemon[0:3:2]
    #This is the multidelete, Starting with Reshiram, Oshawott, and finally Card.
    #in a list the starting value is 0, with it continuing after that.
