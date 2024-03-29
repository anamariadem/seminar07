import unittest
'''
we want to use feature-driven development
    -we start implementing a feature and make it work :)
what we start with:
    -add a new client: each client is a physical person having a unique id, name and age
'''

'''
1. Write a Client class in the domain:
    -client has an id(set in constructor, read-only otherwise)
    -client has a len >= 3 and an age >= 18 (properties)
'''

class Client:
    def __init__(self,Id,name,age):
        if Id == None:
            raise ValueError("Client id cannot be none!")
        self._id = Id
        self.Name = name
        self.Age = age

    @property
    def Id(self):
        return self._id

    @property
    def Name(self):
        return self._name

    @Name.setter
    def Name(self,value):
        if len(value)<3:
            raise ValueError("Name is too short")
        self._name = value

    @property
    def Age(self):
        return self._age

    @Age.setter
    def Age(self,value):
        if int(value) < 18:
            raise ValueError("Client is too young!")
        self._age = value

    def __eq__(self, other):
        if isinstance(other, Client) == False:
            return False
        return self.Id == other.Id


    def __str__(self):
        return 'Id= ' + str(self._id) + 'Name: ' + str(self.Name) + 'Age' + str(self.Age)

'''
this tells python that TestClient is a special type of class 
python should find these classes are run the tests on its own
'''

class TestClient(unittest.TestCase):
    def testClient(self):
        c = Client(2, 'Edi POp', 19)
        assert c.Id == 2
        assert c.Name == 'Edi POp'
        assert c.Age == 19

    def testClient_again(self):
        c = Client(2, 'Pop MIhnea', 20)
        try:
            c.Age = 17
            assert False  # should have raised an error
        except ValueError:
            assert True  # we are ei okay
        except Exception:
            assert False  # a different exception was raised


'''
    1. Must not forget to run all my tests
    2. First test failure crashes my program :(
        - what is the status of the remaining tests?
        -no reports, no feedback, nada
    3. No difference between running and testing the program

Support for running unit test is spotty in VS Code
    -ok in pycharm and eclipse
    
'''


#tc = TestClient()
#tc.testClient()
#tc.testClient_again()















