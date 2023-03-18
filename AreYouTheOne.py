# Import random module
import random

names = []

class Contestant:
    '''Set up contestant objects'''

    def __init__(self,name):
        '''Initialize name'''
        self.name = name

    def __repr__(self):
        '''Return string representation of object'''
        return f'{self.name}'

class Matches:
    '''Create matches (used for perfect matches and guessing matches)'''
    def __init__(self, contestants,bad_matches):
        '''Initialize contestant list and perfect matches'''
        self.bad_matches = bad_matches
        keepgoing = True
        while keepgoing:
            random_matches = []
            temp_contestants = contestants.copy()
            for i in range(len(contestants)//2):                                                  # Run loop 8 times to account for 8 pairs (given 16 contestants)
                random_pair_set = set(random.choices(temp_contestants,k=2) )        # Get two random names from list
                
                while len(random_pair_set) == 1 or random_pair_set in self.bad_matches:               # Establish while loop to handle if two names are the same person
                    random_pair_set = set(random.choices(temp_contestants,k=2))
                    if len(temp_contestants) == 2 and random_pair_set in self.bad_matches:
                        break
                
                if len(temp_contestants) == 2 and random_pair_set in self.bad_matches:
                    break

                # random_set = set((list(random_pair_set)[0],list(random_pair_set)[1]) )       # Create a tuple to hold match
                random_matches.append(random_pair_set)                             # Add match tuple to list of matches
                
                temp_contestants.remove(list(random_pair_set)[0])                    # Remove the contestants that have been matched
                temp_contestants.remove(list(random_pair_set)[1])

                if len(temp_contestants) == 0:
                    keepgoing = False

        self.matches = random_matches
        
class Simulation:
    '''Simulates game'''

    def __init__(self,names):
        '''Initialize game'''
        contestants = []
        for name in names:
            contestants.append(Contestant(name))
        self.contestants = contestants
        self.bad_matches = []
        self.game = Matches(self.contestants,self.bad_matches)
        self.matches_found = []
        

    def guess_matches(self):
        '''Randomize guesses for perfect couples'''
        # random_matches = []
        # temp_contestants = self.contestants.copy()
        
        # for i in range(len(self.contestants)//2):                                                  # Run loop 8 times to account for 8 pairs (given 16 contestants)
        #     random_pair_list = random.choices(temp_contestants,k=2)         # Get two random names from list
            
        #     while random_pair_list[0] == random_pair_list[1]:               # Establish while loop to handle if two names are the same person
        #         random_pair_list = random.choices(temp_contestants,k=2)
            
        #     while random_pair_list in self.bad_matches:
        #         random_pair_list = random.choices(temp_contestants,k=2)
            
        #     random_set = set((random_pair_list[0],random_pair_list[1]) )       # Create a tuple to hold match
        #     random_matches.append(random_set)                             # Add match tuple to list of matches
            
        #     temp_contestants.remove(random_pair_list[0])                    # Remove the contestants that have been matched
        #     temp_contestants.remove(random_pair_list[1])

        # self.guess = random_matches
        self.guess = Matches(self.contestants,self.bad_matches)
        return self.guess.matches
    
    def analyze_matches(self):
        '''Return number of correct perfect couples'''
        self.count = len(self.matches_found)
        for match in self.guess.matches:
            if match in self.game.matches: self.count += 1

        if self.count == len(self.matches_found):
            for match in self.guess.matches:
                self.bad_matches.append(match)

        return f'{self.count} couples are correct!'

    def truth_booth(self):
        '''
        Random couple is sent to "truth booth"
        Returns string indicating if match is correct
        '''
        self.random_couple = random.choice(self.guess.matches)
        if self.random_couple in self.game.matches:
            for contestant in self.random_couple:
                self.contestants.remove(contestant)

            self.matches_found.append(self.random_couple)
            return f'{list(self.random_couple)[0]} and {list(self.random_couple)[1]} are a perfect match!'
        else: 
            if self.random_couple not in self.bad_matches: self.bad_matches.append(self.random_couple)
            return f'{list(self.random_couple)[0]} and {list(self.random_couple)[1]} are NOT a match!'

def start_sim():
    global names
    names = ['Sherri','Gunther','Clinton','Karl','Douglas','Suzanne','Jules','Jerold','Raymond','Annette','Alina','Gabriela','Maria','Placida','Mariano','Vincent']
    sim = Simulation(names)
    # print(f'Contestants: {sim.game.contestants}')
    print(f'Contestants: {names}')
    finish = False
    week = 0
    while not finish:
        week += 1
        print(f'\nWeek {week}\n----------------------')
        sim.guess_matches()
        analyze = sim.analyze_matches()
        print(analyze)
        if sim.count == len(sim.game.matches):
            print('All matches found!')
            print(f'Perfect matches: {sim.game.matches}')
            return
        if sim.count != len(sim.matches_found):
            truth = sim.truth_booth()
            print(f'{list(sim.random_couple)[0]} and {list(sim.random_couple)[1]} have been sent to the truth booth!')
            print(truth)
        else: print('No new correct matches')
        if sim.matches_found != []:
            print(f'Perfect matches found: {sim.matches_found}')
            

start_sim()