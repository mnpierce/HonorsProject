### ALGORITHM 3 ###
'''
Uses full truth booth functionality
Uses partial functionality of gathering bad matches
    - Bad matches are only added if they come from the truth booth (i.e. if the truth booth indicates that a couple is not a perfect match)
    - No additional circumstances are used to gathered more bad matches
Will only be slightly faster than Algorithm 4 as this does not result in a ton of additional bad matches, only a maximum of one addtional bad match per week
'''

# Import random and math modules
import random
from math import factorial as fact  # import factorial from math

class Contestant:
    '''Set up contestant objects'''

    def __init__(self,name):
        '''Initialize name'''
        self.name = name

    def __repr__(self):
        '''Return string representation of object'''
        return f'{self.name}'

class Matches:
    '''
    Create matches (used for perfect matches and guessing matches)
    This is done with random generation to best simulate how matches would be formed in a real reality TV show game (there should be no systematic approach to predict matches)
    '''

    def __init__(self, contestants,bad_matches=[]):
        '''Initialize contestant list and perfect matches'''

        # initialize bad matches with passed in list
        self.bad_matches = bad_matches

        # use while loop to add functionality to restart the whole list if there is no way to make a valid list during any given attempt
        # this would happen if the only possible matches remaining are already in the bad matches list
        keepgoing = True
        while keepgoing:

            # initialize matches list to add to
            random_matches = []

            # create temporary contestants list to modify
            temp_contestants = contestants.copy()

            # use for loop that runs the exact amount of times needed to create the right amount of pairs
            for i in range(len(contestants)//2):

                # get two random contestants from the contestants list
                random_pair_set = set(random.sample(temp_contestants,2))

                # calculate the number possible pair permutations given the number of contestants
                n = len(temp_contestants)
                r = 2
                max_loops = int(fact(n) / (fact(n-r)*fact(r)))

                # random generation may force the only remaining possible pairs to already be in bad_matches, so may need to restart guess entirely
                count = 0   # counter

                while random_pair_set in self.bad_matches:
                    count += 1  # increment counter

                    # re-generate the pair
                    random_pair_set = set(random.sample(temp_contestants,2))

                    # if re-generation attempts exceed the maximum number of possibilities, break out of loop to restart entire list
                    if  count >= max_loops:

                        # if still a bad pair on last final attempt, break out of loop, otherwise will continue
                        if random_pair_set in self.bad_matches:
                            break

                # same as previous two if statements to break out of the for loop as well
                if count >= max_loops:
                    if random_pair_set in self.bad_matches:
                        break

                # add the pair to the list of matches
                random_matches.append(random_pair_set)

                # remove the contestants that have been matched from the temporary list so they are not used again
                temp_contestants.remove(list(random_pair_set)[0])
                temp_contestants.remove(list(random_pair_set)[1])

                # if no contestants remain, the full list is generated and the while loop can terminate
                if len(temp_contestants) == 0:
                    keepgoing = False

        # initialize matches to be used in composition in other classes
        self.matches = random_matches

class Simulation:
    '''Simulates game'''

    def __init__(self,names):
        '''Initialize game'''

        # set up empty list of contestants to append to
        contestants = []

        # create Contestant objects
        for name in names:
            contestants.append(Contestant(name))

        # initialize list of Contestant objects
        self.contestants = contestants

        # initialize list of bad matches that will be updated in .analyze_matches() and .truth_booth()
        self.bad_matches = []

        # create instance of Matches class that holds the perfect matches that will be used the goal of the game
        self.game = Matches(self.contestants)

        # initialize list of confirmed matches that will be updated in .truth_booth()
        self.matches_found = []

    def guess_matches(self):
        '''Randomize guesses for perfect couples'''

        # create instance of Matches class
        self.guess = Matches(self.contestants,self.bad_matches)

        # return .matches attribute which contains the list of generated matches
        return self.guess.matches

    def analyze_matches(self):
        '''Return number of correct perfect couples'''

        # initialize count starting at the number of matches already found
        self.count = len(self.matches_found)

        # check all matches within generated match list
        for match in self.guess.matches:

            # if the match is in the predetermined matches, increment the count
            if match in self.game.matches: self.count += 1

        # return how many couples are correct
        return f'{self.count} matches are correct!'

    def truth_booth(self):
        '''
        Random couple is sent to "truth booth"
        Returns string indicating if match is correct
        '''
        # send a random couple to the truth booth
        self.random_couple = random.choice(self.guess.matches)

        # if this couple is a perfect match...
        if self.random_couple in self.game.matches:

            # remove contestants from remaining contestants list
            for contestant in self.random_couple:
                self.contestants.remove(contestant)

            # append the pair to the confirmed matches list
            self.matches_found.append(self.random_couple)

            # return that the pair is a perfect match
            return f'{list(self.random_couple)[0]} and {list(self.random_couple)[1]} are a perfect match!'

        # if this couple is a bad match...
        else:

            # add pair to bad matches list
            if self.random_couple not in self.bad_matches: self.bad_matches.append(self.random_couple)

            # return that the pair is not a perfect match
            return f'{list(self.random_couple)[0]} and {list(self.random_couple)[1]} are NOT a match!'

def start_sim():
    'This function is used to run the simulation'

    # start with a list of names to use in simulation (this is just an example list of 16 names; the game will work with any names)
    names = ['Sherri','Gunther','Clinton','Karl','Douglas','Suzanne','Jules','Jerold','Raymond','Annette','Alina','Gabriela','Maria','Placida','Mariano','Vincent']

    # start an instance of the simulation
    sim = Simulation(names)

    if __name__ == '__main__':
        # print a list of all contestants at the start of the game
        print(f'The contestants for this season are: {sim.contestants[0]}, {sim.contestants[1]}, {sim.contestants[2]}, {sim.contestants[3]}, {sim.contestants[4]}, {sim.contestants[5]}, {sim.contestants[6]}, {sim.contestants[7]}, {sim.contestants[8]}, {sim.contestants[9]}, {sim.contestants[10]}, {sim.contestants[11]}, {sim.contestants[12]}, {sim.contestants[13]}, {sim.contestants[14]}, and {sim.contestants[15]}')

    # initialize while loop to allow game to continue until all matches are found
    # contains the actions that happen each week
    # 1) contestants get with who they think is their perfect match
    # 2) # of perfect matches is announced
    # 3) one couple is sent to truth booth

    finish = False
    week = 0        # week counter

    while not finish:
        # increment week counter
        week += 1

        if __name__ == '__main__':
            # add "Week #" header for readability
            print(f'\nWeek {week}\n----------------------')

        # contestants form pairs
        sim.guess_matches()

        # number of perfect matches is announced
        analyze = sim.analyze_matches()
        if sim.count != len(sim.game.matches):
            if __name__ == '__main__':
                print(analyze)

        # if this number is equal to the amount of perfect matches needed, the game is over
        if sim.count == len(sim.game.matches):
            if __name__ == '__main__':
                # announce the game is over
                print('All matches found!')

                # announce what the perfect matches are
                print(f'\nPerfect matches: {list(sim.game.matches[0])[0]} and {list(sim.game.matches[0])[1]}, {list(sim.game.matches[1])[0]} and {list(sim.game.matches[1])[1]}, {list(sim.game.matches[2])[0]} and {list(sim.game.matches[2])[1]}, {list(sim.game.matches[3])[0]} and {list(sim.game.matches[3])[1]}, {list(sim.game.matches[4])[0]} and {list(sim.game.matches[4])[1]}, {list(sim.game.matches[5])[0]} and {list(sim.game.matches[5])[1]}, {list(sim.game.matches[6])[0]} and {list(sim.game.matches[6])[1]}, {list(sim.game.matches[7])[0]} and {list(sim.game.matches[7])[1]}')

            # end function
            return week

        # if the number of correct couples is not the same as the number of correct couples already found (in this case there would be no new matches)
        if sim.count != len(sim.matches_found):

            # send one couple to the truth booth to see if they are a perfect match
            truth = sim.truth_booth()

            if __name__ == '__main__':
                # announce who will be sent to the truth booth and if they are a perfect match
                print(f'\n{list(sim.random_couple)[0]} and {list(sim.random_couple)[1]} have been sent to the truth booth!')
                print(truth)

        # if this is the case, announce there are no new correct matches
        else:
            if __name__ == '__main__':
                print('No new correct matches')

        if __name__ == '__main__':
            # at the end of each week, announce how many matches have been confirmed so far
            print(f'\nConfirmed matches: {len(sim.matches_found)}')

if __name__ == '__main__':
    # start simulation
    start_sim()