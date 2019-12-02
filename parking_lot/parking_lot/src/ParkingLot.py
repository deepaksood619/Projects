"""
Created on 2019-11-27

@author: deepaksood619
"""

from Constants import PARKING_LOT_FULL


class Car:
    def __init__(self, registration_number, colour):
        self.registration_number = registration_number
        self.colour = colour

    def __str__(self):
        return f'{self.registration_number}      {self.colour}'

    __repr__ = __str__


class ParkingLot:
    def __init__(self, slots_size):
        # -1 represent slot is not available to park
        # 0 represent slot is available to park
        # <Car object> slot is used
        self.num_of_slot = slots_size

        # 1 indexed array, 0th index is marked as -1 to make it unusable
        self.parking_space = [0] * (slots_size + 1)
        self.parking_space[0] = -1

        print(f'Created a parking lot with {slots_size} slots')

    def __str__(self):
        status = 'Slot No.    Registration No    Colour'

        for index, car in enumerate(self.parking_space):
            if isinstance(car, Car):
                status += f'\n{index}           {car}'

        return status

    def park(self, registration_number, colour):
        """

        :param registration_number: registration_number of the new car
        :param colour: colour of the new car
        :return: slot index the car was inserted into otherwise PARKING_LOT_FULL constant
        """
        car = Car(registration_number=registration_number, colour=colour)

        # park the car in closest available slot
        for slot_index, value in enumerate(self.parking_space):
            if value == 0:
                # park the car
                self.parking_space[slot_index] = car

                # return the slot
                return slot_index

        return PARKING_LOT_FULL

    def leave(self, slot_index):
        """

        :param slot_index: remove the car from the slot_index parking lot and mark it as free
        :return: True if parking_space freed else False
        """
        if 0 < slot_index <= self.num_of_slot:
            if isinstance(self.parking_space[slot_index], Car):
                self.parking_space[slot_index] = 0
                return True
            else:
                return False
        else:
            raise Exception('Wrong input')

    def get_registration_numbers_for_cars_with_colour(self, colour):
        """

        :param colour: colour to filter cars by
        :return: comma-separated car's registration numbers
        """
        registration_numbers = []
        for i in self.parking_space:
            if isinstance(i, Car) and i.colour == colour:
                registration_numbers.append(i.registration_number)

        return ', '.join(registration_numbers)

    def get_slot_numbers_for_cars_with_colour(self, colour):
        """

        :param colour: colour to filter cars by
        :return: comma-separated car's slot numbers
        """
        slot_numbers = []
        for slot, car in enumerate(self.parking_space):
            if isinstance(car, Car) and car.colour == colour:
                slot_numbers.append(slot)

        return ', '.join(str(i) for i in slot_numbers)

    def get_slot_number_for_registration_number(self, registration_number):
        """

        :param registration_number: registration number of the car
        :return: integer if slot found or 'Not found'
        """
        for slot, car in enumerate(self.parking_space):
            if isinstance(car, Car) and car.registration_number == registration_number:
                return slot

        return 'Not found'
