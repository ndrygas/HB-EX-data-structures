"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    """data = open 
    species = set()
    for i in filename():
        species.add()"""
    unique_species = set()
    data = open(filename)
    for line in data:
        species = line.rstrip().split("|")[1]
        unique_species.add(species)

    return unique_species
    # TODO: replace this with your code

    #return species


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []
   
    # TODO: replace this with your code
    data = open(filename)
    for line in data:
        name, species = line.rstrip().split("|")[:2] 
        
        if search_string in ("All", species):
            villagers.append(name)
    
    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, 
    grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
    data = open(filename)
    fitness_v = []
    nature_v = []
    education_v = []
    music_v = []
    fashion_v = []
    play_v = []

    #main_list [[], [], ]

    for line in data:
        name = line.rstrip().split("|")[0]
        #print(name)
        hobby = line.rstrip().split("|")[3]
        #print(hobby)
        if hobby == "Fitness":
            fitness_v.append(name)
        elif hobby == "Nature":
            nature_v.append(name)
        elif hobby == "Education":
            education_v.append(name)
        elif hobby == "Music":
            music_v.append(name)
        elif hobby == "Fashion":
            fashion_v.append(name)
        elif hobby == "Play":
            play_v.append(name)
        
    hobby_members = [fitness_v, nature_v, education_v, music_v, fashion_v, play_v]
    print(hobby_members)
    #print(fitness_v)


        #need to grab all names and sort by hobby

    # for line in data:
    #     name, species = line.rstrip().split("|")[:2] 
        
    #     if search_string in ("All", species):
    #         villagers.append(name)
    
    # return sorted(villagers)
    # TODO: replace this with your code

    #return []


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []
   
    # TODO: replace this with your code
    data = open(filename)
    for line in data:
        all_data.append(tuple(line.rstrip().split("|")))

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
