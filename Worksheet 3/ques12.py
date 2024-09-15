class StringManipulation:
    def get_String(self):
        self.s = input("Enter a string: ")

    def print_String(self):
        print(self.s.upper())

def string_manipulation():
    obj = StringManipulation()
    obj.get_String()
    obj.print_String()


string_manipulation()