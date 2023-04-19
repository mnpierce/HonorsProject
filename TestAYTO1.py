import unittest,random
from AreYouTheOne1 import Contestant,CreateMatches,GuessMatches,Simulation

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

class Test_CreateMatches(unittest.TestCase):
    'Test CreateMatches class'

    def test_init(self):
        'Tests init properly initializes matches'

        # contestant objects list to use in Matches instances
        self.contestants = [Contestant('Sherri'),Contestant('Gunther'),Contestant('Clinton'),Contestant('Karl'),Contestant('Douglas'),Contestant('Suzanne')]
        
        # set up two contestants with both matching attributes
        self.contestants[0].team = 'Yankees'
        self.contestants[0].color = 'blue'
        self.contestants[1].team = 'Yankees'
        self.contestants[1].color = 'blue'
        
        # set up two contestants with one matching attribute
        self.contestants[2].team = 'Red Sox'
        self.contestants[2].color = 'blue'
        self.contestants[3].team = 'Red Sox'
        self.contestants[3].color = 'red'
        
        # set up two contestants with no matching attributes
        self.contestants[4].team = 'Mets'
        self.contestants[4].color = 'yellow'
        self.contestants[5].team = 'Blue Jays'
        self.contestants[5].color = 'green'

        # CreateMatches instance
        random.seed(567)    # random seed to ensure 50/50 odds are not random
        self.m1 = CreateMatches(self.contestants)

        # assert that matches list has 3 pairs given there are 6 contestants
        self.assertEqual(len(self.m1.matches),3)

        # assert that matches are properly generated
        # Match 1 - contestants with both shared attributes
        # Match 2 - contestants with one shared attributes
        # Match 3 - contestants with no shared attributes
        self.assertEqual(self.m1.matches,[{self.contestants[0],self.contestants[1]},{self.contestants[2],self.contestants[3]},{self.contestants[4],self.contestants[5]}])

class Test_GuessMatches(unittest.TestCase):
    'Test GuessMatches class'

    def test_init(self):
        'Tests init properly initializes matches'
         # contestant objects list to use in Matches instances
        self.contestants = [Contestant('Sherri'),Contestant('Gunther'),Contestant('Clinton'),Contestant('Karl'),Contestant('Douglas'),Contestant('Suzanne')]

        # set up two contestants with both matching attributes
        self.contestants[0].team = 'Yankees'
        self.contestants[0].color = 'blue'
        self.contestants[1].team = 'Yankees'
        self.contestants[1].color = 'blue'
        
        # set up two contestants with one matching attribute
        self.contestants[2].team = 'Red Sox'
        self.contestants[2].color = 'blue'
        self.contestants[3].team = 'Red Sox'
        self.contestants[3].color = 'red'
        
        # set up two contestants with no matching attributes
        self.contestants[4].team = 'Mets'
        self.contestants[4].color = 'yellow'
        self.contestants[5].team = 'Blue Jays'
        self.contestants[5].color = 'green'
        
        # generate guess (no need for random.seed as the odds are 100% for guessing purposes)
        self.m1 = GuessMatches(self.contestants)

        # assert that matches list has 3 pairs given there are 6 contestants
        self.assertEqual(len(self.m1.matches),3)

        # assert that matches are properly guessed
        # Match 1 - contestants with both shared attributes
        # Match 2 - contestants with one shared attributes
        # Match 3 - contestants with no shared attributes
        self.assertEqual(self.m1.matches,[{self.contestants[0],self.contestants[1]},{self.contestants[2],self.contestants[3]},{self.contestants[4],self.contestants[5]}])

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

        # test that bad_matches is updated if counter is equal to number of matches from previous week
        self.s2 = Simulation(self.names)
        self.s2.guess_matches()
        self.s2.game.matches = [{self.s2.contestants[0],self.s2.contestants[3]},{self.s2.contestants[1],self.s2.contestants[2]}]
       
        # Bad guesses to test that analyze_matches properly updates bad matches
        self.s2.guess.matches = [{self.s2.contestants[1],self.s2.contestants[3]},{self.s2.contestants[0],self.s2.contestants[2]}]
        
        # Analyze (should update bad_matches with the two bad guesses)
        self.s2.analyze_matches()
        self.assertEqual(len(self.s2.bad_matches),2)

    def test_truth_booth(self):
        'Tests that matches_found is updated with a correct match'

        # call .truth_booth() so .matches_found can be accessed
        self.s1.truth_booth()

        # calling .truth_booth() once on a list of entirely correct matches should increment matches_found to 1
        self.assertEqual(len(self.s1.matches_found),1)

        # Test that contestants are removed upon successful match, test that bad matches are added upon unsuccessful match
        
        # Set up simulation for this case
        self.s3 = Simulation(self.names)
        self.s3.guess_matches()
        
        self.s3.game.matches = [{self.s3.contestants[0],self.s3.contestants[3]},{self.s3.contestants[1],self.s3.contestants[2]}]
        # Good guesses (contestants should be removed)
        self.s3.guess.matches = [{self.s3.contestants[0],self.s3.contestants[3]}]
        
        # Store contestant objects to be able to check membership after removal
        match_contestant1 = self.s3.contestants[0]
        match_contestant2 = self.s3.contestants[3]

        # Call truth booth
        self.s3.truth_booth()
        # Assert contestants are removed
        self.assertTrue(match_contestant1 not in self.s3.contestants)
        self.assertTrue(match_contestant2 not in self.s3.contestants)

if __name__ == "__main__":
    unittest.main()