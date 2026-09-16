# Base Class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        """Base implementation of starting the engine."""
        return f"The {self.brand} {self.model}'s generic system check is complete. Vehicle is ready."

# Subclass 1: Car
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        # Initialize attributes from the base class
        super().__init__(brand, model)
        self.doors = doors

    def start_engine(self):
        """Overriding the base method specifically for a car."""
        return f"Vroom! The {self.brand} {self.model}'s {self.doors}-door engine purrs to life."

# Subclass 2: Bike
class Bike(Vehicle):
    def __init__(self, brand, model, bike_type):
        # Initialize attributes from the base class
        super().__init__(brand, model)
        self.bike_type = bike_type

    def start_engine(self):
        """Overriding the base method specifically for a bike."""
        return f"Click! The {self.brand} {self.model} {self.bike_type} bike is ready to ride. Start pedaling!"
