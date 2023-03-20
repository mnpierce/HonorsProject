import unittest,random
from AreYouTheOne import Contestant,Matches,Simulation

class Test_Contestant(unittest.TestCase):
    'Test Contestant class'

    def setUp(self):
        'Set up Contestant instance with sample name'
        # names list to use in generating a random name
        self.names = ['Sherri','Gunther','Clinton','Karl','Douglas','Suzanne','Jules','Jerold','Raymond','Annette','Alina','Gabriela','Maria','Placida','Mariano','Vincent']

        # pull a random name from name list
        self.random_name = random.choice(self.names)

        # create Contestant instance to test
        self.c1 = Contestant(self.random_name)

    def test_init(self):
        'Tests init properly initializes name'
        self.assertEqual(self.c1.name,self.random_name)

class Test_Matches(unittest.TestCase):
    'Test Matches class'

    def setUp(self):
        'Set up Matches instance'
        # contestant objects list to use in Matches instances
        self.contestants = [Contestant('Sherri'),Contestant('Gunther'),Contestant('Clinton'),Contestant('Karl'),Contestant('Douglas'),Contestant('Suzanne')]

        # set up m1
        self.m1_bad_matches = []  # no bad matches
        self.m1 = Matches(self.contestants,self.m1_bad_matches)

        # set up m2
        # bad matches consist of Gunther and every other contestant EXCEPT Suzanne (Gunther and Suzanne must be a pair in every test run of m2)
        self.m2_bad_matches = [{self.contestants[0],self.contestants[1]},{self.contestants[2],self.contestants[1]},{self.contestants[1],self.contestants[3]},{self.contestants[4],self.contestants[1]}]
        self.m2 = Matches(self.contestants,self.m2_bad_matches)

    def test_init(self):
        'Tests init properly initializes matches'

        # assert that matches list has 3 pairs given there are 6 contestants
        self.assertEqual(len(self.m1.matches),3)

        # assert that {Gunther,Suzanne} is in the matches list (any other match with Gunther is discarded due to being in bad_matches)
        self.assertIn({self.contestants[1],self.contestants[5]},self.m2.matches)

        # check each match in matches list
        for match in self.m2.matches:

            # make sure all have 2 contestants (ensures random generation does not save a match where both contestants are the same person because sets do not repeat members)
            self.assertEqual(len(list(match)),2)

            # make sure no matches are in bad_matches
            self.assertTrue(match not in self.m2_bad_matches)

class Test_Simulation(unittest.TestCase):
    'Test Simulation class'

    def setUp(self):
        'Set up Simulation instance with smaller names list'
        # names list to use in simulation instance
        self.names = ['Sherri','Gunther','Clinton','Karl']

        # Simulation instance
        self.s1 = Simulation(self.names)

        # initialize perfect matches and bad matches to be used in tests (avoid randomization)
        self.s1.game.matches = [{self.s1.contestants[0],self.s1.contestants[3]},{self.s1.contestants[1],self.s1.contestants[2]}]
        self.s1.bad_matches = [{self.s1.contestants[0],self.s1.contestants[1]},{self.s1.contestants[0],self.s1.contestants[2]},{self.s1.contestants[1],self.s1.contestants[3]},{self.s1.contestants[2],self.s1.contestants[3]},{self.s1.contestants[0],self.s1.contestants[2]}]

        # call guess_matches so guess.matches can be accessed
        self.s1.guess_matches()

    def test_init(self):
        'Tests init properly initializes contestant list and perfect matches'
        # check each contestant in contestant list
        for contestant in self.s1.contestants:

            # assert that each contestant is a Contestant object
            self.assertIsInstance(contestant, Contestant)

        # assert that there are 2 perfect matches for the game (given 4 contestants)
        self.assertEqual(len(self.s1.game.matches),2)

    def test_guess_matches(self):
        'Tests guess_matches properly generates a new list of matches'

        # use s1 to test that guess_matches generates the right number of matches
        # cannot test specific matches due to randomization
        self.assertEqual(len(self.s1.guess_matches()),2)

        # check that the correct guesses are generated given the manipulated bad_matches list
        for match in self.s1.guess.matches:
            self.assertIn(match,[{self.s1.contestants[0],self.s1.contestants[3]},{self.s1.contestants[1],self.s1.contestants[2]}])

    def test_analyze_matches(self):
        '''Tests analyze_matches
                1) properly checks matches
                2) uses a counter to track correct matches
                3) adds bad matches to bad_matches
                4) announces # of correct matches'''

        # assert that analyze_matches finds that 2 matches are correct in s1
        self.assertEqual(self.s1.analyze_matches(),f'2 matches are correct!')

        ### TO DO: test that bad_matches is updated if counter is equal to number of matches from previous week

    def test_truth_booth(self):
        'Tests that matches_found is updated with a correct match'

        # call .truth_booth() so .matches_found can be accessed
        self.s1.truth_booth()

        # calling .truth_booth() once on a list of entirely correct matches should increment matches_found to 1
        self.assertEqual(len(self.s1.matches_found),1)

        ### TO DO: test that contestants are removed upon successful match, test that bad matches are added upon unsuccessful match

if __name__ == "__main__":
    unittest.main()