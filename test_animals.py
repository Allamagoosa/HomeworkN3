#!/usr/bin/python
import animals
import unittest

class Animal(unittest.TestCase):
    """ Animal creataion: """
    def setUp(self):
        pass
    def tearDown(self):
        reload (animals)
    
    def test_unit(self):
        bagira = animals.Animal("Puma", "Bagira", 20, "Female")
        self.assertEqual(bagira.spec, "Puma")
        self.assertEqual(bagira.name, "Bagira")
        self.assertEqual(bagira.age, 10)
        self.assertEqual(bagira.sex, "Female")
        self.assertIsNone(bagira.atype)

class TestVenom(unittest.TestCase):
    """ classVenom creation: """
    def setUp(self):
        pass
    def tearDown(self):
        reload (animals)
    
    def test_unit(self):
        ka = animals.Venom("Python","Ka", 90, "Male")
        self.assertEqual(ka.name, "Ka")
        self.assertEqual(ka.spec, "Python")
        self.assertEqual(ka.sex, "Male")
        self.assertEqual(ka.age, 90)
        self.assertEqual(ka.atype, "Venom")

class TestHerbi(unittest.TestCase):
    """ Herbi creation: """
    def setUp(self):
        pass
    def tearDown(self):
        reload (animals)
    
    def test_unit(self):
        bublik = animals.Herbi("Bull","Bublik", 5, "Male")
	self.assertEqual(bublik.name, "Bublik")
        self.assertEqual(bublik.spec, "Bull")
        self.assertEqual(bublik.sex, "Male")
        self.assertEqual(bublik.age, 5)
	self.assertEqual(bublik.atype, "Herbi")

class TestZoo(unittest.TestCase):
    """ classZoo creation, 
    +add_aviary 
    +list_aviaries 
    +list_animals 
    +del_aviary """
    def setUp(self):
        pass
    def tearDown(self):
        reload (animals)
    
    def test_unit(self):     
        # Zoo class init -- emty aviaryList
        jungle = animals.Zoo()
	self.assertIsInstance(jungle.aviaryList, list)
	self.assertFalse(jungle.aviaryList) 
	
	# add_aviary() -- one element in list
	herbAviary = animals.Aviary("Jungle Herb", "Herbi")
	jungle.add_aviary(herbAviary)
        self.assertEqual(len(jungle.aviaryList), 1) 

        # list_aviaries() -- no return function just print
        self.assertEqual(jungle.aviaryList[0].name, "Jungle Herb")
        self.assertEqual(jungle.list_aviaries(), None) 

        # list_animals() -- no return function just print
        pumba = animals.Herbi("Hog", "Pumba", 5, "Male") 
        herbAviary.add_animal(pumba)
        self.assertEqual(jungle.aviaryList[0].animalList[0].name, "Pumba")
        self.assertEqual(jungle.list_animals(), None) 

	# list_aviaries_vacant()  -- function return list
	self.assertIsInstance(jungle.list_aviaries_vacant(), list)
        
        # move animal to anather aviary
	herb2 = animals.Aviary("herb2", "Herbi")
	jungle.add_aviary(herb2)
	jungle.move_animal(pumba, herb2)

	# stats
	jungle.stats()

	#herbAviary.free()
	jungle.free_aviary(herb2)
	
        # del_aviary() -- emty aviaryList
        jungle.del_aviary(herbAviary)
	jungle.del_aviary(herb2)
        self.assertFalse(jungle.aviaryList)

        
        
class TestAviary(unittest.TestCase):
    """ classAviary creation 
    +add_animal() 
    +del_animal() """
    def setUp(self):
        pass
    def tearDown(self):
        reload (animals)
    
    def test_unit(self):
        herbAviary = animals.Aviary("Jungle Herb", "Herbi")
	self.assertIsInstance(herbAviary.animalList, list)
	self.assertFalse(herbAviary.animalList)
	self.assertEqual(herbAviary.av_type, "Herbi")
	
	# add_animal
        pumba = animals.Herbi("Hog", "Pumba", 5, "Male") 
        herbAviary.add_animal(pumba)
        # one element list
        self.assertEqual(len(herbAviary.animalList), 1)

	# del_animal
	herbAviary.del_animal(pumba)
	self.assertFalse(herbAviary.animalList)
        
	# max count animals
	animalListing = range(herbAviary.ANIMALMAX)
	for i in range (herbAviary.ANIMALMAX):
            animalListing[i] = animals.Herbi("specxx", "NameXX", 5, "Male") 
            herbAviary.add_animal(animalListing[i])
            self.assertEqual(len(herbAviary.animalList), i+1)
	# max limit of animals message
	herbAviary.add_animal(pumba)

if __name__ == "__main__":
    suite = []
    suite.append(unittest.TestLoader().loadTestsFromTestCase(TestVenom))
    suite.append(unittest.TestLoader().loadTestsFromTestCase(TestHerbi))
    suite.append(unittest.TestLoader().loadTestsFromTestCase(TestZoo))
    suite.append(unittest.TestLoader().loadTestsFromTestCase(TestAviary))
    test_suite = unittest.TestSuite(suite)
    unittest.TextTestRunner(verbosity=2).run(test_suite)
