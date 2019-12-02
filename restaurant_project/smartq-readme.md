# Others
1. DjangoBookStore
Problem statement - https://github.com/eskolare/eskolare-django-challenge-2019

# SmartQHiringChallenge
Hackerearth SmartQHiringChallenge Nov 2019

# Problem statement


Develop a pseudo REST backend Application for fetching restaurant orders data.


[Ideal Behaviour]

— Write a backend which exports APIs with all the data provided in the dump below.

— Implement multiple APIs for validation of the request and retrieval of data. All the response bodies should have data in JSON format.

— Your APIs should take multiple parameters to fetch data from backend, and performs request validations.

 

[Minimum Requirement]

— Write a backend in tech stack mentioned below which exposes APIs which return response in JSON.

— Implement APIs for:
Restaurant wise sales
	
Input - restaurantid, date Sample - tuckshop, 21-10-2019

Output - Total sales Sample - 140

 Is a particular requested item available currently. And further, for the provided date how many items are sold
 

Input - itemname Sample - idli, 26-10-2019

Output - “Item Available”, 1 quantity sold

Input - itemname Sample - rice bath

Output - “Item not Available, 0 quantity sold
	
Given the timeslot as follow, 
    timeslots= {‘BREAKFAST’: “07:00-11:00”,
    
    ‘LUNCH’: “12:30-15:30”,
    
    ‘SNACKS’: “16:30-19:00”,
    
    ‘DINNER’: “19:30-23:00”}

List out top 5 most ordered/ trending items for a given restaurant
- of the day
- per slots
    Input - restaurantid, date Sample - tuckshop, 20-10-2019

Output:
    Top 5 most sold item for the day: {dosa- 2, idli - 1}


Top 5 most sold items per slots: {Breakfast: [idli, dosa, karabath, pongal, chapathi],

Lunch: [“ricebath, “dosa”, pongal, pulav, biryani],

Snacks: [“dosa”, “pani puri”, “pavbhaji”, vadapav, “idli”],

DINNER: [biryani, pavbhaji, dosa, idli, pulav]}

Dump all the orders of a day of a restaurant into a csv file

Input - restaurantid, date Sample - tuckshop, 20-10-2019

Output - File download with following headers - Item name, Quantity, Item Price, Ordered Time

Note: If multiple items in an order, each item to be present in a separate row

— Zip all your source code, deployment instructions, screenshots and upload them.

[Guide]
Dataset: data.xlsx 

[Ideal Stack]
Backend: Python - Django/Flask

# Solution

# Creating the image
`docker-compose build`
`docker-compose push`

# Running the application
`docker-compose up restaurant`

# Running application from image
`docker run --rm -it -p=8000:8000 deepaksood619/restaurant:0.0.1`

Navigate to localhost:8000 in browser

```bash
django-admin startproject restaurant .
python3 manage.py startapp sales

python3 manage.py makemigrations
python3 manage.py migrate

python3 manage.py runserver 0.0.0.0:8000

python3 mange.py loaddata

python3 manage.py createsuperuser
```

### API's
http://localhost:8000/total_sale/?restaurant=kanti%20sagar

http://localhost:8000/total_sale/?restaurant=kanti%20sagar,deepak

