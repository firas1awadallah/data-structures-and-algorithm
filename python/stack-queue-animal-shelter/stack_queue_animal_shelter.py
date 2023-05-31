class AnimalShelter:
    class Animal:
        def __init__(self, species, name):
            """
            Initialize an instance of the Animal class.

            Args:
            - species (str): The species of the animal.
            - name (str): The name of the animal.
            """
            self.species = species
            self.name = name

    def __init__(self):
        self.queue = []

    def print_queue(self):
        """
        Print the animals currently in the queue.
        """
        for animal in self.queue:
            print(f"{animal.species}, {animal.name}")

    def enqueue(self, species, name):
        """
        Enqueue an animal to the shelter.

        Args:
        - species (str): The species of the animal.
        - name (str): The name of the animal.
        """
        animal = self.Animal(species, name)
        self.queue.append(animal)

    def dequeue(self, pref):
        """
        Dequeue an animal from the shelter based on preference.

        Args:
        - pref (str): The preferred species ("dog" or "cat") for dequeueing.

        Returns:
        - selected_animal (Animal or None): The dequeued animal or None if preference is invalid.
        """
        if pref != "dog" and pref != "cat":
            return None

        selected_animal = None
        
        for index, animal in enumerate(self.queue):
            if animal.species == pref:
                selected_animal = self.queue.pop(index)
                break

        if selected_animal:
            print(selected_animal.name)

        return selected_animal


shelter = AnimalShelter()

shelter.enqueue("dog", "Fezco")
shelter.enqueue("cat", "Monka")
shelter.enqueue("dog", "Cassini")
shelter.enqueue("cat", "Mommy")
shelter.print_queue()

cat = shelter.dequeue("cat")
shelter.print_queue()

dog = shelter.dequeue("dog")
shelter.print_queue()

invalid_pref = shelter.dequeue("bird")
print(invalid_pref)















