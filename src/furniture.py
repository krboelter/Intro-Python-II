class Furniture:
    
    def __init__(self, name, description, contents):
        self.name = name
        self.description = description
        self.contents = contents
        
    def __str__(self):
        return f"{self.description}"

    def check_contents(self):
        if self.contents is not None:
            print(f"{self.name} contains: {self.contents}.")
        else:
            print(f"There is nothing in/on the {self.name}.")

