# import unittest,random
# from AreYouTheOne import Contestant,Matches,Simulation

# class Test_Contestant(unittest.TestCase):
#     'Test Contestant class'

#     def setUp(self):
#         'Set up Contestant instance with sample name'
#         self.names = ['Sherri','Gunther','Clinton','Karl','Douglas','Suzanne','Jules','Jerold','Raymond','Annette','Alina','Gabriela','Maria','Placida','Mariano','Vincent']
#         self.random_name = random.choice(self.names)
#         self.c1 = Contestant(self.random_name)

#     def test_init(self):
#         'Tests init properly initializes name'
#         self.assertEqual(self.c1.name,self.random_name)

# class Test_Matches(unittest.TestCase):
#     'Test Matches class'
    
#     def setUp(self):
#         'Set up Matches instance'
#         self.contestants = [Contestant('Sherri'),Contestant('Gunther'),Contestant('Clinton'),Contestant('Karl'),Contestant('Douglas'),Contestant('Suzanne')]
#         self.m1_bad_matches = []
#         self.m1 = Matches(self.contestants,self.m1_bad_matches)
#         self.m2_bad_matches = [{self.contestants[0],self.contestants[1]},{self.contestants[2],self.contestants[1]},{self.contestants[1],self.contestants[3]},{self.contestants[4],self.contestants[1]}]
#         self.m2 = Matches(self.contestants,self.m2_bad_matches)
    
#     def test_init(self):
#         'Tests init properly initializes matches'
#         self.assertEqual(len(self.m1.matches),3)
#         self.assertIn({self.contestants[1],self.contestants[5]},self.m2.matches)


# class Test_Simulation(unittest.TestCase):
#     'Test Simulation class'
   
#     def setUp(self):
#         'Set up Simulation instance with smaller names list'
#         self.names = ['Sherri','Gunther','Clinton','Karl','Douglas','Suzanne']
#         self.s1 = Simulation(self.names)
        
#     def test_init(self):
#         pass
      

# if __name__ == "__main__":
#     unittest.main()