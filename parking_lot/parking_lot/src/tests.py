"""
Created on 2019-11-27

@author: deepaksood619
"""

import unittest

from Constants import PARKING_LOT_FULL
from ParkingLot import ParkingLot


class TestParkingLot(unittest.TestCase):
    """
    Test class for testing parking lot
    """

    def setUp(self):
        """
        This will be called everytime a new test is run
        :return:
        """
        self.parkinglot = ParkingLot(6)

    def test_park(self):
        self.assertEqual(self.parkinglot.park(registration_number='KA-01-HH-1234', colour='White'), 1)
        self.assertEqual(self.parkinglot.park(registration_number='KA-01-HH-1234', colour='White'), 2)
        self.assertEqual(self.parkinglot.park(registration_number='KA-01-HH-1234', colour='White'), 3)
        self.assertEqual(self.parkinglot.park(registration_number='KA-01-HH-1234', colour='White'), 4)
        self.assertEqual(self.parkinglot.park(registration_number='KA-01-HH-1234', colour='White'), 5)
        self.assertEqual(self.parkinglot.park(registration_number='KA-01-HH-1234', colour='White'), 6)
        self.assertEqual(self.parkinglot.park(registration_number='KA-01-HH-1234', colour='White'), PARKING_LOT_FULL)
        self.assertEqual(self.parkinglot.park(registration_number='KA-01-HH-1234', colour='White'), PARKING_LOT_FULL)

    def test_leave(self):
        self.assertEqual(self.parkinglot.leave(slot_index=1), False)
        self.assertEqual(self.parkinglot.park(registration_number='KA-01-HH-1234', colour='White'), 1)
        self.assertEqual(self.parkinglot.leave(slot_index=1), True)
        self.assertEqual(self.parkinglot.leave(slot_index=1), False)
        self.assertEqual(self.parkinglot.leave(slot_index=2), False)

    def test_get_registration_numbers_for_cars_with_colour(self):
        self.assertEqual(self.parkinglot.get_registration_numbers_for_cars_with_colour('White'), '')
        self.assertEqual(self.parkinglot.park(registration_number='KA-01-HH-1234', colour='White'), 1)
        self.assertEqual(self.parkinglot.get_registration_numbers_for_cars_with_colour('White'), 'KA-01-HH-1234')
        self.assertEqual(self.parkinglot.park(registration_number='KA-01-HH-1235', colour='White'), 2)
        self.assertEqual(self.parkinglot.get_registration_numbers_for_cars_with_colour('White'),
                         'KA-01-HH-1234, KA-01-HH-1235')
        self.assertEqual(self.parkinglot.park(registration_number='KA-01-HH-1235', colour='Black'), 3)
        self.assertEqual(self.parkinglot.get_registration_numbers_for_cars_with_colour('White'),
                         'KA-01-HH-1234, KA-01-HH-1235')

    def test_get_slot_numbers_for_cars_with_colour(self):
        self.assertEqual(self.parkinglot.get_slot_numbers_for_cars_with_colour('White'), '')
        self.assertEqual(self.parkinglot.park(registration_number='KA-01-HH-1234', colour='White'), 1)
        self.assertEqual(self.parkinglot.get_slot_numbers_for_cars_with_colour('White'), '1')
        self.assertEqual(self.parkinglot.park(registration_number='KA-01-HH-1235', colour='White'), 2)
        self.assertEqual(self.parkinglot.get_slot_numbers_for_cars_with_colour('White'), '1, 2')
        self.assertEqual(self.parkinglot.park(registration_number='KA-01-HH-1235', colour='Black'), 3)
        self.assertEqual(self.parkinglot.get_slot_numbers_for_cars_with_colour('White'), '1, 2')

    def test_get_slot_number_for_registration_number(self):
        self.assertEqual(self.parkinglot.get_slot_number_for_registration_number('KA-01-HH-1234'), 'Not found')
        self.assertEqual(self.parkinglot.park(registration_number='KA-01-HH-1234', colour='White'), 1)
        self.assertEqual(self.parkinglot.get_slot_number_for_registration_number('KA-01-HH-1234'), 1)
        self.assertEqual(self.parkinglot.park(registration_number='KA-01-HH-1235', colour='White'), 2)
        self.assertEqual(self.parkinglot.get_slot_number_for_registration_number('KA-01-HH-1234'), 1)
        self.assertEqual(self.parkinglot.get_slot_number_for_registration_number('KA-01-HH-1235'), 2)


unittest.main()
