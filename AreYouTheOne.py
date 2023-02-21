# Import random module
import random

names = ['Sherri','Gunther','Clinton','Karl','Douglas','Suzanne','Jules','Jerold','Raymond','Annette','Alina','Gabriela','Maria','Placida','Mariano','Vincent']

class Contestant:
    '''Set up contestant objects'''

    def __init__(self,name):
        '''Initialize name'''
        self.name = name

    def __repr__(self):
        '''Return string representation of object'''
        return f'{self.name}'


class Matches:
    '''Create perfect matches'''

    def __init__(self, names):
        '''Initialize contestant list and perfect matches'''

        contestants = []

        for name in names:
            contestants.append(Contestant(name))
        
        self.contestants = contestants

        random_matches = []
        temp_contestants = self.contestants.copy()
        
        for i in range(8):                                                  # Run loop 8 times to account for 8 pairs (given 16 contestants)
            random_pair_list = random.choices(temp_contestants,k=2)         # Get two random names from list
            
            while random_pair_list[0] == random_pair_list[1]:               # Establish while loop to handle if two names are the same person
                random_pair_list = random.choices(temp_contestants,k=2)     
            
            random_tuple = (random_pair_list[0],random_pair_list[1])        # Create a tuple to hold match
            random_matches.append(random_tuple)                             # Add match tuple to list of matches
            
            temp_contestants.remove(random_pair_list[0])                    # Remove the contestants that have been matched
            temp_contestants.remove(random_pair_list[1])

        self.perfect_matches = random_matches

class Simulation:
    '''Simulates game'''

    def __init__(self):
        '''Initialize game'''

        self.game = Matches(names)

    def guess_matches(self):
        '''Randomize guesses for perfect couples'''
        pass
    
    def analyze_matches(self):
        '''Return number of correct perfect couples'''
        pass

    def truth_booth(self):
        '''
        Random couple is sent to "truth booth"
        Returns True/False (True if perfect match)
        '''
        pass

def start_sim():

    sim = Simulation()
    f1 = f'Contestants: {sim.game.contestants}'
    print(f1)
    f2 = f'Perfect Matches: {sim.game.perfect_matches}'
    print(f2)


start_sim()