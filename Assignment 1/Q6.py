''' Implement a Parking Lot System
Requirements:
Implement classes for Vehicle, Car, Bike, ParkingSpot, ParkingLot.
Vehicle should be a base class with attributes like license_plate and vehicle_type.
Car and Bike should inherit from Vehicle.
ParkingSpot should have attributes like spot_id, is_available, and vehicle.
ParkingLot should manage multiple parking spots and provide methods to park and retrieve vehicles, and to get the status of the parking lot. '''

class Vehicle:
    def __init__(self, license_plate, vehicle_type):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type

    def __str__(self):
        return f"{self.vehicle_type} [License Plate: {self.license_plate}]"


class Car(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate, "Car")


class Bike(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate, "Bike")


class ParkingSpot:
    def __init__(self, spot_id):
        self.spot_id = spot_id
        self.is_available = True
        self.vehicle = None

    def park_vehicle(self, vehicle):
        if self.is_available:
            self.vehicle = vehicle
            self.is_available = False
            print(f"{vehicle} parked in spot {self.spot_id}.")
        else:
            print(f"Spot {self.spot_id} is already occupied.")

    def remove_vehicle(self):
        if not self.is_available:
            vehicle = self.vehicle
            self.vehicle = None
            self.is_available = True
            print(f"{vehicle} removed from spot {self.spot_id}.")
        else:
            print(f"Spot {self.spot_id} is already empty.")

    def __str__(self):
        if self.is_available:
            return f"Spot {self.spot_id} is available."
        else:
            return f"Spot {self.spot_id} is occupied by {self.vehicle}."


class ParkingLot:
    def __init__(self, num_spots):
        self.spots = [ParkingSpot(spot_id) for spot_id in range(1, num_spots + 1)]

    def find_available_spot(self):
        for spot in self.spots:
            if spot.is_available:
                return spot
        return None

    def park_vehicle(self, vehicle):
        spot = self.find_available_spot()
        if spot:
            spot.park_vehicle(vehicle)
        else:
            print("No available parking spots.")

    def retrieve_vehicle(self, license_plate):
        for spot in self.spots:
            if not spot.is_available and spot.vehicle.license_plate == license_plate:
                spot.remove_vehicle()
                return
        print(f"No vehicle found with license plate {license_plate}.")

    def get_status(self):
        for spot in self.spots:
            print(spot)

    def __str__(self):
        available_spots = sum(1 for spot in self.spots if spot.is_available)
        return f"Parking Lot Status: {available_spots}/{len(self.spots)} spots available."


# Example usage
parking_lot = ParkingLot(num_spots=5)

# Vehicles
car1 = Car("ABC-123")
bike1 = Bike("XYZ-987")
car2 = Car("PQR-456")

# Parking vehicles
parking_lot.park_vehicle(car1)
parking_lot.park_vehicle(bike1)
parking_lot.park_vehicle(car2)
print()

# Display parking lot status
print(parking_lot)
parking_lot.get_status()
print()

# Retrieving a vehicle
parking_lot.retrieve_vehicle("ABC-123")
print()

# Display parking lot status after retrieving
print(parking_lot)
parking_lot.get_status()
print()

# Trying to park more vehicles than available spots
car3 = Car("GHI-789")
bike2 = Bike("LMN-654")
parking_lot.park_vehicle(car3)
parking_lot.park_vehicle(bike2)
print()

# Final status
print(parking_lot)
parking_lot.get_status()