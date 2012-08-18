class Directory:

    def __init__(self):
        self.directory = {}

    def add(self, name):
        """
        """
        name_parts = name.split(' ')
        if len(name_parts) < 2:
            return False
		
        last_name = name_parts[len(name_parts) - 1].lower()
		
        # First occurrance of family name
        if last_name not in self.directory:
            self.directory[last_name] = []

        first_name = name_parts[0].lower()
        # Add first name to family
        self.directory[last_name].append(first_name)
		
        return True

    def adds(self, name_list):
        """
        """
        for name in name_list:
            result = self.add(name)
            
            if(result == False):
                return False

    def contains(self, name):
        """
        """
        name_parts = name.split(' ')
		
        # Only given the family name
        if len(name_parts) == 1:
            return name_parts[0] in self.directory
        # Given first and last name
        elif len(name_parts) >= 2:
            first_name = name_parts[0].lower()
            last_name = name_parts[len(name_parts) - 1].lower()

            # Find the name within the directory
            if last_name in self.directory:
                return first_name in self.directory[last_name]

        return False

    def get_directory(self):
        return self.directory
		