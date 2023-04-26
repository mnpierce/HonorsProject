### ALGORITHM 1 ###
'''
Utilizes new component of additional attributes used to match contestants
    - If contestants have the same favorite baseball team and favorite color, they have 100% chance of matching (as long as one contestant has not already met another contestant with the same interests as well)
    - If contestants have EITHER the same favorite baseball team and favorite color but NOT both, they have a 50% chance of matching (as long as one contestant has not already met another contestant with a shared interest as well)
This allows the contestants to have more educated guesses when deciding who they think are perfect matches
This algorithm also uses the full funcitonality of gathering bad matches as demonstrated in Algorithm 2
'''

# Import random module
import random

class Contestant:
    '''Set up contestant objects'''
    baseball_team = ['Yankees','Red Sox','Mets']
    fav_color = ['blue','red','green']

    def __init__(self,name):
        '''Initialize name'''
        self.name = name
        self.team = random.choice(Contestant.baseball_team)
        self.color = random.choice(Contestant.fav_color)

    def __repr__(self):
        '''Return string representation of object'''
        return f'{self.name}'

class CreateMatches:
    '''
    Create perfect matches
        - 100% chance of matching if have same fav baseball team and color
        - 50% chance of matching if have same fav baseball team OR color but not both
    '''
    def __init__(self,contestants):
        '''Initialize and create matches'''
        # create copy of contestants list so contestant removal does not cause issues
        temp_contestants = contestants.copy()

        # initialize matches list that will be used throughout simulation
        self.matches = list()

        # iniitialize visited contestants list
        #   - if every contestant remaining in the contestant list has been visited, there are no 100% matches remaining
        contestants_visited = set()

        # while there are contestants that have not been visited
        while any(contestant not in contestants_visited for contestant in temp_contestants):

            # choose a random first contestant to compare
            contestant1 = random.choice(temp_contestants)

            # regenerate contestant if already visited
            while contestant1 in contestants_visited:
                contestant1 = random.choice(temp_contestants)

            # add contestant to list of visited contestants
            contestants_visited.add(contestant1)

            # shuffle to assure the same guesses aren't being generated every time for the same contestant1
            random.shuffle(temp_contestants)

            # iterate through contestants
            for contestant2 in temp_contestants:
                # if the contestants are not the same person...
                if contestant1 != contestant2:
                    # if the contestants have the same favorite baseball team and color...
                    if contestant1.team == contestant2.team and contestant1.color == contestant2.color:

                        # add each contestant into a set denoting a perfect match
                        perfect_match = set([contestant1,contestant2])
                        # add the set to the list of perfect matches
                        self.matches.append(perfect_match)

                        # remove each contestant from the list so they are not used again
                        temp_contestants.remove(contestant1)
                        temp_contestants.remove(contestant2)

                        break # break out of for loop

        # iniitialize visited contestants list
        #   - if every contestant remaining in the contestant list has been visited, there are no 50% matches remaining
        contestants_visited = set()

        # while there are contestants that have not been visited
        while any(contestant not in contestants_visited for contestant in temp_contestants):

            # choose a random first contestant to compare
            contestant1 = random.choice(temp_contestants)

            # regenerate contestant if already visited
            while contestant1 in contestants_visited:
                contestant1 = random.choice(temp_contestants)

            # add contestant to list of visited contestants
            contestants_visited.add(contestant1)

            # shuffle to assure the same guesses aren't being generated every time for the same contestant1
            random.shuffle(temp_contestants)

            # iterate through contestants
            for contestant2 in temp_contestants:
                # if the contestants are not the same person...
                if contestant1 != contestant2:
                    # if the contestants have the same favorite baseball team OR color...
                    if contestant1.team == contestant2.team or contestant1.color == contestant2.color:

                        # implement 50/50 chance
                        odds = random.choice([0,1])
                        if odds == 1:

                            # add each contestant into a set denoting a perfect match
                            perfect_match = set([contestant1,contestant2])
                            # add the set to the list of perfect matches
                            self.matches.append(perfect_match)

                            # remove each contestant from the list so they are not used again
                            temp_contestants.remove(contestant1)
                            temp_contestants.remove(contestant2)

                            break # break out of for loop

        # run loop the number of times needed to create remaining matches
        for i in range(len(temp_contestants)//2):

            # get two random contestants from the contestants list
            perfect_match = set(random.sample(temp_contestants,2))

            # add the pair to the list of matches
            self.matches.append(perfect_match)

            # remove the contestants that have been matched from the temporary list so they are not used again
            temp_contestants.remove(list(perfect_match)[0])
            temp_contestants.remove(list(perfect_match)[1])

        return

class GuessMatches:
    '''
    Create matches () guessing matches)
    This is done with random generation to best simulate how matches would be formed in a real reality TV show game (there should be no systematic approach to predict matches)
    '''
    def __init__(self, contestants,bad_matches=[]):
        '''Initialize contestant list and perfect matches'''
        # initialize bad matches with passed in list
        self.bad_matches = bad_matches

        # create copy of contestants list so contestant removal does not cause issues
        temp_contestants = contestants.copy()

        # initialize matches list that will be used throughout simulation
        self.matches = list()

        # iniitialize visited contestants list
        #   - if every contestant remaining in the contestant list has been visited, there are no 100% matches remaining
        contestants_visited = set()

        # while there are contestants that have not been visited
        while any(contestant not in contestants_visited for contestant in temp_contestants):

            # choose a random first contestant to compare
            contestant1 = random.choice(temp_contestants)

            # regenerate contestant if already visited
            while contestant1 in contestants_visited:
                contestant1 = random.choice(temp_contestants)

            # add contestant to list of visited contestants
            contestants_visited.add(contestant1)

            # shuffle to assure the same guesses aren't being generated every time for the same contestant1
            random.shuffle(temp_contestants)

            # iterate through contestants
            for contestant2 in temp_contestants:

                # if the contestants are not the same person...
                if contestant1 != contestant2:
                    # if the contestants have the same favorite baseball team and color...
                    if contestant1.team == contestant2.team and contestant1.color == contestant2.color:

                        # add each contestant into a set denoting a perfect match
                        guess = set([contestant1,contestant2])

                        # check if guess in already determined bad matches
                        if guess in self.bad_matches: continue

                        # add the set to the list of perfect matches
                        self.matches.append(guess)

                        # remove each contestant from the list so they are not used again
                        temp_contestants.remove(contestant1)
                        temp_contestants.remove(contestant2)

                        # break out of for loop
                        break

        # iniitialize visited contestants list
        #   - if every contestant remaining in the contestant list has been visited, there are no 100% matches remaining
        contestants_visited = set()

        # while there are contestants that have not been visited
        while any(contestant not in contestants_visited for contestant in temp_contestants):

            # choose a random first contestant to compare
            contestant1 = random.choice(temp_contestants)

            # regenerate contestant if already visited
            while contestant1 in contestants_visited:
                contestant1 = random.choice(temp_contestants)

            # add contestant to list of visited contestants
            contestants_visited.add(contestant1)

            # shuffle to assure the same guesses aren't being generated every time for the same contestant1
            random.shuffle(temp_contestants)

            # iterate through contestants
            for contestant2 in temp_contestants:

                # if the contestants are not the same person...
                if contestant1 != contestant2:
                    # if the contestants have the same favorite baseball team OR color...
                    if contestant1.team == contestant2.team or contestant1.color == contestant2.color:

                        # add each contestant into a set denoting a perfect match
                        guess = set([contestant1,contestant2])

                        # check if guess in already determined bad matches
                        if guess in self.bad_matches: continue

                        # add the set to the list of perfect matches
                        self.matches.append(guess)

                        # remove each contestant from the list so they are not used again
                        temp_contestants.remove(contestant1)
                        temp_contestants.remove(contestant2)

                        # break out of for loop
                        break

        for i in range(len(temp_contestants)//2):

            # get two random contestants from the contestants list
            guess = set(random.sample(temp_contestants,k=2))

            # add the pair to the list of matches
            self.matches.append(guess)

            # remove the contestants that have been matched from the temporary list so they are not used again
            temp_contestants.remove(list(guess)[0])
            temp_contestants.remove(list(guess)[1])

        return

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
        self.game = CreateMatches(self.contestants)

        # initialize list of confirmed matches that will be updated in .truth_booth()
        self.matches_found = []

    def guess_matches(self):
        '''Randomize matches for perfect couples'''

        # create instance of Matches class
        self.guess = GuessMatches(self.contestants,self.bad_matches)

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

        # if no matches are found, append all matches to the bad matches list
        if self.count == len(self.matches_found):
            for match in self.guess.matches:
                self.bad_matches.append(match)

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