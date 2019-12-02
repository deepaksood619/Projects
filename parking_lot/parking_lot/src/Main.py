"""
Created on 2019-11-27

@author: deepaksood619
"""

import sys

from Constants import PARKING_LOT_FULL
from ParkingLot import ParkingLot


class Main:
    def __init__(self):
        self.parking_lot = None

    def run_command(self, input_command):
        """
        This function run each command

        :param input_command: a string input command for running a test case
        :return:
        """
        input_list = input_command.split()

        if input_list[0] == 'create_parking_lot':
            # create_parking_lot 6
            if not self.parking_lot:
                self.parking_lot = ParkingLot(slots_size=int(input_list[1]))
            else:
                raise Exception('Parking lot already created')

        elif input_list[0] == 'park':
            # park KA-01-HH-1234 White

            if not self.parking_lot:
                raise Exception('Create a parking lot first')

            parked_slot = self.parking_lot.park(registration_number=input_list[1], colour=input_list[2])
            if parked_slot == PARKING_LOT_FULL:
                print('Sorry, parking lot is full')
            else:
                print(f'Allocated slot number: {parked_slot}')

        elif input_list[0] == 'leave':
            # leave 4

            if not self.parking_lot:
                raise Exception('Create a parking lot first')

            slot_index = int(input_list[1])
            self.parking_lot.leave(slot_index=slot_index)
            print(f'Slot number {slot_index} is free')

        elif input_list[0] == 'status':

            if not self.parking_lot:
                raise Exception('Create a parking lot first')

            print(self.parking_lot)

        elif input_list[0] == 'registration_numbers_for_cars_with_colour':
            # registration_numbers_for_cars_with_colour White

            if not self.parking_lot:
                raise Exception('Create a parking lot first')

            print(self.parking_lot.get_registration_numbers_for_cars_with_colour(input_list[1]))

        elif input_list[0] == 'slot_numbers_for_cars_with_colour':
            # slot_numbers_for_cars_with_colour White

            if not self.parking_lot:
                raise Exception('Create a parking lot first')

            print(self.parking_lot.get_slot_numbers_for_cars_with_colour(input_list[1]))

        elif input_list[0] == 'slot_number_for_registration_number':
            # slot_number_for_registration_number KA-01-HH-3141

            if not self.parking_lot:
                raise Exception('Create a parking lot first')

            print(self.parking_lot.get_slot_number_for_registration_number(input_list[1]))

        elif input_list[0] == 'exit':
            exit(1)
        else:
            raise Exception('Wrong input')

    def start(self):
        """
        This is the starting function, it will either run interactively or run code using a text file
        :return:
        """
        if len(sys.argv) == 2:
            # run code using text file
            input_file = sys.argv[1]

            with open(input_file, 'r') as file_obj:
                lines = file_obj.readlines()

            for line in lines:
                self.run_command(line.strip())

        else:
            # run code in interactive mode
            while True:
                input_command = input()

                self.run_command(input_command.strip())


if __name__ == '__main__':
    Main().start()
