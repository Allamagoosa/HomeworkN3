#!/usr/bin/python
""" Zoo have aviaries. Aviaries have animals. """

class Animal(object):
    """ Base class for representing Animal """
    def __init__(self, spec, name, age, sex, atype=None):
        self.spec = spec
        self.name = name
        self.age = age
        self.sex = sex
        self.atype = atype

    def __str__(self):
        """ print Animal """
        return "{0} {1} ({4})\n\t {2} years old, {3}".format(self.spec, self.name, self.age, self.sex, self.atype)


class Venom(Animal):
    """ Class for representing Venom animals """
    ID_ = 0
    def __init__(self, spec, name, age, sex):
        Animal.__init__(self, spec, name, age, sex, "Venom")
        Venom.ID_ += 1


class Herbi(Animal):
    """ Class for representing Herbivore animals """
    ID_ = 0
    def __init__(self, spec, name, age, sex):
        Animal.__init__(self, spec, name, age, sex, "Herbi")
        Herbi.ID_ += 1


class Zoo(object):
    """ Class for representing Zoo """
    AVIARYMAX = 5
    def __init__(self):
        """ Constructor """
        self.aviaryList = []
        self.aviaryCount = 0

    def add_aviary(self, av):
        """ add new Aviary """
        if self.aviaryCount < self.AVIARYMAX:
            self.aviaryList.append(av)
            self.aviaryCount += 1
        else: print "\nZoo already has {0} aviaries. There's no more space for new one.".format(self.AVIARYMAX)

    def del_aviary(self, av):
        """ delete Aviary """
        self.aviaryList.remove(av)
        self.aviaryCount -= 1

    def list_aviaries(self):
        """ print aviaries """
        for item in self.aviaryList:
            print "Aviary: {0}".format(item.name)

    def list_aviaries_vacant(self):
        """ print aviaries with vacant places """
        freeAviaryList = []
        aviarySelector = 0
        print "Aviary with vacancies:"
        for item in self.aviaryList:
            if item.animalCount < item.ANIMALMAX:
                freeAviaryList.append(item)
                print "\t\t [***{0}***] --{1}-- has {2} vacancies".format(aviarySelector, item.name, (item.ANIMALMAX - item.animalCount))
                aviarySelector += 1
        return freeAviaryList

    def list_animals(self):
        """ print Animals """
        for i in self.aviaryList:
            print "Aviary: {0}".format(i.name)
            print "-----------------------------"
            for j in i.animalList:
                print j

    def move_animal(self, movingAnimal, destinationAviary):
        """ Move Animal to destination Aviary """ 
        # Avaries[i] have Animals[j]
        for i in self.aviaryList:
            for j in i.animalList:
                if j is movingAnimal:
                    print "movingAnimal {0} from --{1}-- to --{2}--".format(movingAnimal.name, i.name, destinationAviary.name)
                    if destinationAviary.add_animal(movingAnimal):
                        # if previosly adding is success:
                        i.del_animal(movingAnimal)
                    else: print "moving animal aborted"

    def free_aviary(self, makeFreeAviary, kill=False):
        """ free aviary """
        makefreeAviaryName = makeFreeAviary.name
        freeAnimalList = []
        freeAviaryList = self.list_aviaries_vacant()
        if kill:
            makeFreeAviary.free(True)
        else:
            freeAnimalList = makeFreeAviary.free(False)
            for freeAnimalItem in freeAnimalList:
                print "Making free {0} from --{1}--".format(freeAnimalItem.name, makefreeAviaryName)
                print "Select new aviary 0..{0}".format(len(freeAviaryList)-1)
                selectedAviary = int(input()) #todo test
                if selectedAviary > len(freeAviaryList)-1:
                    print "Aviary Not Selected, break"
                    break
                if freeAviaryList[selectedAviary]:
                    print "Animal *{0}* will be export to **{1}**".format(freeAnimalItem.name, freeAviaryList[selectedAviary].name)

    def stats(self):
        """ print statistic """
        v_count, h_count, a_count = 0, 0, 0
        fv_count, fh_count, fa_count = 0, 0, 0
        print "----Stats------------"
        for itemAviary in self.aviaryList:
            a_count += 1
            if itemAviary.av_type == "Herbi":
                h_count += 1
                if itemAviary.animalCount < itemAviary.ANIMALMAX:
                    fh_count += 1
                    fa_count += 1
            if itemAviary.av_type == "Venom":
                v_count += 1
                if itemAviary.animalCount < itemAviary.ANIMALMAX:
                    fv_count += 1
                    fa_count += 1
        print "total Aviary total:     {0}".format(a_count)
        print "total Herbivore total:  {0}".format(h_count)
        print "total Venom total:      {0}".format(v_count)
        print "total Free Herbi total: {0}".format(fh_count)
        print "total Free Venom total: {0}".format(fv_count)
        print "total Free Aviary total:{0}".format(fa_count)

class Aviary(object):
    """ Class for representing Aviaries """
    ANIMALMAX = 10
    def __init__(self, name, av_type):
        self.name = name
        self.av_type = av_type
        self.animalList = []
        self.animalCount = 0

    def add_animal(self, anml):
        """ Add animal """
        if self.animalCount < self.ANIMALMAX:
            self.animalList.append(anml)
            self.animalCount += 1
            return True
        else:
            print "\nAviary already has {0} amimals. There's no more space for another one.".format(self.ANIMALMAX)
            return False

    def del_animal(self, anml):
        """ Delete Animal """
        self.animalList.remove(anml)
        self.animalCount -= 1

    def free(self, kill=False):
        """ free Aviary with remove or kill """
        if kill:
            print "Free aviary --{0}-- ".format(self.name)
            self. __init__(None, None)
        else:
            freeAnimalList = self.animalList
            print "Free aviary --{0}-- ".format(self.name)
            self. __init__(None, None)
            return freeAnimalList

#simba = Venom("Lion","Simba", 1, "Male")
#pumba = Herbi("Hog", "Pumba", 3, "Male")
#print simba
#print pumba
#jungleHerb = Aviary("Jungle Herb aviary", "Herbi")
#jungle = Zoo()
#jungle.add_aviary(jungleHerb)
#jungle.list_animals()
