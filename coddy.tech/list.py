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
    pokemon.insert(1, "Zekrom")
    #This will add Zekrom after Reshiram
    pokemon.extend([1, 2])
    #This extends the list, with 1 and 2. It allows for more to be added instead of individual
    del pokemon[0:3:2]
    #So 0 is the starting point, and 3 is where it would stop.
    #whatever is at the forth stop, will be safe, and is the end point, so any other places after, will not follow the next rule.
    # The 2 is when a place gets taken, for every 2nd place.
    #example using the og list. It takes Reshiram and Oshawott, and would keep going, if it didn't end the next turn. If it was a list of 5, then the one after card, would also be taken.
    #in a list the starting value is 0, with it continuing after that.
def prod(lst):
    result = 1
    for num in lst:
        result *= num
    return result
def fest():
    nums = [1, 2, 3]
    result = [x * 3 for x in nums]
    print(result)  # Output: [3, 6, 9]
def reverse_list(numbers):
    reversed_list = []
    for number in numbers:
        reversed_list.insert(0, number)
    return reversed_list
def tuple_examples():
    colors = "Blue", "Red", "Green"
    print(colors)
    #Tuple's can not be edited after, but it takes less memory than a list.
