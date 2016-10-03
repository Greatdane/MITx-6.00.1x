# Problem Set 07f - Connecting Adopters and Adoption Centers

#
# /// PREVIOUS PROBLEM'S CODE - REQUIRED FOR TESTING /// 
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

class Adopter:
    """ 
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.

    """
    def __init__(self, name, desired_species):
        '''
        Initializes a Adopter object
            
        name - A string that represents the name of the adopter
    
        desired_species- A string that represents the desired species to adopt
        '''
        self.name = name
        self.desired_species = desired_species
    def get_name(self):
        '''
        Returns the name of the adopter
        '''
        return self.name 
    def get_desired_species(self):
        '''
        Returns the desired species of the adopter
        '''
        return self.desired_species
    def get_score(self, adoption_center):
        '''
        Returns the score
        The minimum value that a score can be is 0. 
        
        num_desired is a float of the number of the adopter's desired species that the adoption center has.
        '''
        num_desired = float(adoption_center.get_number_of_species(self.desired_species))
        return 1 * num_desired 
        
class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    def __init__(self, name, desired_species, considered_species):
        '''
        Initializes FlexibleAdopter, a subclass of Adopter object class
        
        considered_species - a list of strings of alternative species that the person is interested in adopting.
        
        All of the inputs are the same as the Adopter
        '''
        self.name = name
        self.desired_species = desired_species
        self.considered_species = considered_species
    
    def get_score(self, adoption_center):
        '''
        Returns the score
        
        adopter_score - the value that the Adopter class's score method returns
        
        num_other - the number of animals the adoption center has of all the other considered species
        '''
        adopter_score = float(adoption_center.get_number_of_species(self.desired_species)) # Can we call directly from Adopter?
        
        num_other = 0
        for a in self.considered_species:
            num_other += float(adoption_center.get_number_of_species(a))        
        return adopter_score + ( 0.3 * num_other)
          
class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    def __init__(self, name, desired_species, feared_species):
        '''
        Initializes FearfulAdopter, a subclass of Adopter object class
        
        feared_species - a string that is the name of the feared species.
        
        All of the inputs are the same as the Adopter
        '''
        self.name = name
        self.desired_species = desired_species
        self.feared_species = feared_species
    
    def get_score(self, adoption_center):
        '''
        Returns the score
        
        adopter_score - the value that the Adopter class's score method returns
        
        num_feared - the number of animals the adoption center has of the feared species
        '''      
        adopter_score = float(adoption_center.get_number_of_species(self.desired_species)) # Can we call directly from Adopter?
        
        num_feared = float(adoption_center.get_number_of_species(self.feared_species))       
        result =  adopter_score - (0.3 * num_feared)
        if result < 0:
            result = 0.0
        return result

class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    def __init__(self, name, desired_species, allergic_species):
        '''
        Initializes AllergicAdopter, a subclass of Adopter object class.
        
        allergic_species -  a list of strings of one or more species that the adopter is allergic to.
        
        All of the inputs are the same as the Adopter
        '''
        self.name = name
        self.desired_species = desired_species
        self.allergic_species = allergic_species

    def get_score(self, adoption_center):
        '''
        Returns the score.
        
        Returns a value that is 0 if the adoption center has one or more of a species that the adopter is allergic to
        '''  
        for n in self.allergic_species:
            if adoption_center.get_number_of_species(n) > 0 :
                return 0.0
        return 1 * float(adoption_center.get_number_of_species(self.desired_species)) # Same code as Superclass Adopter 

class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. 
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary. 
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        '''
        Initializes MedicatedAllergicAdopter, a subclass of AllergicAdopter object class.
        
        medicine_effectiveness -  a dictionary of the effectiveness of the medicine for each animal. 
        
        All of the inputs are the same as the AllergicAdopter
        '''
        self.name = name
        self.desired_species = desired_species
        self.allergic_species = allergic_species
        self.medicine_effectiveness = medicine_effectiveness
    
    def get_score(self, adoption_center):
        '''
        Returns the score.        
        '''
        lowest = 1
        for n in self.allergic_species:
            if adoption_center.get_number_of_species(n) > 0 :
                if self.medicine_effectiveness[n] < lowest:
                    lowest = self.medicine_effectiveness[n]                
        return lowest * float(adoption_center.get_number_of_species(self.desired_species))
            
class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    def __init__(self, name, desired_species, location):
        '''
        Initializes SluggishAdopter, a subclass of Adopter object class.
        
        location - is a tuple of floats of the (x, y)
        
        All of the other inputs are the same as Adopter.
        '''
        Adopter.__init__(self, name, desired_species)
        self.location = (float(location[0]), float(location[1]))
        
    def get_linear_distance(self, to_location):
        '''
        Imports math modulet to calculate square root (math.sqrt)
        
        Returns the formula of the square root of (x1 - y1)^2 + (x2 - y2)^2 were x is 
        the input to_location and y is self.location.
        '''
        import math
        return math.sqrt(((to_location[0]-self.location[0])**2) + ((to_location[1]-self.location[1])**2))
        
    def get_score(self, adoption_center):
        '''
        Imports the random module to create a random number between two variables (random.uniform(x, y))
        
        Returns the score, based on distance, and a random variable between two set ammounts.
        '''
        import random
        # num_desired is taken from the original Adopter to get a score
        num_desired = float(adoption_center.get_number_of_species(self.desired_species))
        # To calculate the distance between Mr Slugglish and the adoption center
        distance = self.get_linear_distance(adoption_center.get_location()) 
        
        if distance < 1:
            return 1 * num_desired
        elif distance < 3:
            return random.uniform(0.7, 0.9) * num_desired
        elif distance < 5:
            return random.uniform(0.5, 0.7) * num_desired
        elif distance >= 5:
            return random.uniform(0.1, 0.5) * num_desired 
                                
# /// END OF PREVIOUS CODE /// 
#
                                              
#
# Problem 07f - Part 1
#            
def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter 
    to the Adopter will be ordered from highest score to lowest score.
    """
    ordered_list = []
    
    for ac in list_of_adoption_centers:
        ordered_list.append([ac, adopter.get_score(ac)])
    
    ordered_list = sorted(ordered_list, key=lambda ac: ac[0].get_name())
    ordered_list = sorted(ordered_list, key=lambda score: score[1], reverse=True)
    return [ac[0] for ac in ordered_list]
    
#
# Problem 07f - Part 2
#  
def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """
    ordered_list = []
    
    for person in list_of_adopters:
        ordered_list.append([person, person.get_score(adoption_center)])
        
    ordered_list = sorted(ordered_list, key=lambda ac: ac[0].get_name())
    ordered_list = sorted(ordered_list, key=lambda score: score[1], reverse=True)
    return [ac[0] for ac in ordered_list[0:n]]
    
# /// TESTING.. ///   
adopter = MedicatedAllergicAdopter("One", "Cat", ['Dog', 'Horse'], {"Dog": .5, "Horse": 0.2})
adopter2 = Adopter("Two", "Cat")
adopter3 = FlexibleAdopter("Three", "Horse", ["Lizard", "Cat"])
adopter4 = FearfulAdopter("Four","Cat","Dog")
adopter5 = SluggishAdopter("Five","Cat", (1,2))
adopter6 = AllergicAdopter("Six", "Cat", "Dog") 

ac = AdoptionCenter("Place1", {"Mouse": 12, "Dog": 2}, (1,1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3,5))
ac3 = AdoptionCenter("Place3", {"Horse": 25, "Dog": 9}, (-2,10))

# how to test get_adopters_for_advertisement
get_adopters_for_advertisement(ac, [adopter, adopter2, adopter3, adopter4, adopter5, adopter6], 10)
# you can print the name and score of each item in the list returned
 
adopter4 = FearfulAdopter("Four","Cat","Dog")
adopter5 = SluggishAdopter("Five","Cat", (1,2))
adopter6 = AllergicAdopter("Six", "Lizard", "Cat")

ac = AdoptionCenter("Place1", {"Cat": 12, "Dog": 2}, (1,1))
ac2 = AdoptionCenter("Place2", {"Cat": 12, "Lizard": 2}, (3,5))
ac3 = AdoptionCenter("Place3", {"Cat": 40, "Dog": 4}, (-2,10))
ac4 = AdoptionCenter("Place4", {"Cat": 33, "Horse": 5}, (-3,0))
ac5 = AdoptionCenter("Place5", {"Cat": 45, "Lizard": 2}, (8,-2))
ac6 = AdoptionCenter("Place6", {"Cat": 23, "Dog": 7, "Horse": 5}, (-10,10))

# how to test get_ordered_adoption_center_list
print get_ordered_adoption_center_list(adopter4, [ac,ac2,ac3,ac4,ac5,ac6])                            
# you can print the name and score of each item in the list returned  
                            