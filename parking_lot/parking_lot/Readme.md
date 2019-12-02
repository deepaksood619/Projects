# Simple Parking Management System

### Running the code
```bash
# for running ruby functional tests
./bin/run_functional_tests

# for running program
./bin/parking_lot functional_spec/fixtures/file_input.txt

# for running python tests
python3 src/tests.py
```

### Language Used - Python

### Assumptions
1. Only one parking lot can be created.
2. No two cars with same registration will enter the parking lot, there is no check if two cars with same registration enters the parking lot. In current implementation if this happens, car will enter but then the api get_slot_number_for_registration_number will return the first car with that registration number.
3. Wrong inputs are not checked at api level

### Time taken to solve
1. 2 hours for coding
2. 1 hour for testing and documentation