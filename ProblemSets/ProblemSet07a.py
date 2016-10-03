# Problem Set 07a - The Adoption Center

class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        '''
        Initializes a AdoptionCenter object
             
        name -  A string that represents the name of the adoption center.
        
        location - A tuple (x, y) That represents the x and y as floating point coordinates of the adoption center location.
        
        species_types - A string:integer dictionary that represents the number of specific pets that each adoption center holds.
        An example would be: {"Dog": 10, "Cat": 5, "Lizard": 3} 
        Note that the specific animals tracked depend on the adoption center. If an adoption center does not have any of a specific 
        species up for adoption, it will not be represented in the dictionary.
        '''
        self.name = name
        self.location = (float(location[0]), float(location[1])) #location is now floating point tuple.
        self.species_types = species_types
    def get_number_of_species(self, animal):
        '''
        Returns the number of a given species that the adoption center has.
        '''
        if animal in self.species_types:
            return self.species_types[animal]
        else:
            return 0 #returns zero if the adoption center does not have an animal.
    def get_location(self):
        '''
        Returns the location of the adoption center
        '''
        return self.location
    def get_species_count(self):
        '''
        Returns a copy of the full list and count of the available species at the adoption center.
        '''
        return self.species_types.copy()
    def get_name(self):
        '''
        Returns the name of the adoption center
        '''
        return self.name 
    def adopt_pet(self, species):
        '''
        Decrements the value of a specific species at the adoption center and does not return anything.
        '''
        adopted = self.species_types[species]
        if species in self.species_types:
            adopted -= 1
        self.species_types[species] = adopted
        if self.species_types[species] == 0: # Delete species from dictionary if count is zero
            del self.species_types[species]

# Testing..
BA = AdoptionCenter('Best adoption', {'Dog': 3, 'Cat': 1}, (43.11, 59.11))
BA.adopt_pet('Cat')