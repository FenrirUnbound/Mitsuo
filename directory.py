#! /usr/bin/env python

class Directory:

    def __init__(self):
        self.directory = {}

    """
    """
    def add(self, name):
        nameParts = name.split(' ')
        if len(nameParts) < 2:
            return False
		
        lastName = nameParts[len(nameParts) - 1].lower()
		
        # First occurrance of family name
        if lastName not in self.directory:
            self.directory[lastName] = []

        firstName = nameParts[0].lower()
        # Add first name to family
        self.directory[lastName].append(firstName)
		
        return True

    """
    """
    def contains(self, name):
        nameParts = name.split(' ')
		
        # Only given the family name
        if len(nameParts) == 1:
            return nameParts[0] in self.directory
        # Given first and last name
        elif len(nameParts) >= 2:
            firstName = nameParts[0].lower()
            lastName = nameParts[len(nameParts) - 1].lower()

            if lastName in self.directory:
                return firstName in self.directory[lastName]

        return False


    def getDirectory(self):
        return self.directory
		