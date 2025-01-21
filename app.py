"""
Author: Er. Amar kumar 
Professional: Senior software engineer 

"""


class FlameGame:

    _first_person_name = None
    _second_person_name = None 
    _flame_words = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    _first_person = {}
    _second_person = {}
    _unique_chars = 0

    
    def _resetGameState(self):
       
        self._first_person_name = None
        self._second_person_name = None

    def _getUsersInputs(self):
       
       self._first_person_name = input("Enter name of a first person: ")
       self._second_person_name = input("Enter name of a second person: ")

    def _findUniqueChar(self):

 
        for char in self._first_person_name:
            self._first_person[char] =  self._first_person.get(char) + 1  if self._first_person.get(char) != None else 1
               
        for char in self._second_person_name:
            self._second_person[char] =  self._second_person.get(char) + 1  if self._second_person.get(char) != None  else 1
  
          
        for key in self._first_person.keys():
            if key in self._first_person and key in self._second_person:
                self._unique_chars += abs(self._first_person[key] - self._second_person[key])
            else:
                self._unique_chars += self._first_person[key]


        for key in self._second_person.keys():
            if self._first_person.get(key) == None:
                self._unique_chars += self._second_person[key]

    def playGame(self):

        self._resetGameState()
        self._getUsersInputs()
        self._findUniqueChar()
       
        
        try:
            while len(self._flame_words) > 1:
                index = (self._unique_chars % len(self._flame_words) - 1)

                if index >= 0:
                    right = self._flame_words[index+1:]
                    left = self._flame_words[:index]
                    self._flame_words  =  right + left

                else:
                    self._flame_words = self._flame_words[:len(self._flame_words)-1]

            print("Your result is:  ",self._flame_words[0])

        except Exception:
            print("Error found!")
            exit(0)


if __name__ == "__main__":
    print("Welcome! Find Relationship between two person using name: ")
    print("Lets do! some fun: ")
    app = FlameGame()
    app.playGame()


