# Hotel-Booking

This "system" is build with using Django framework and djangorestframework. Its a simple API that create order for "client" and get
the order details. The reason I chose this framework is because it has a prebuilt ORM, easy databases setup and a lot more other features. 
Its take a while to reread/understand the docs because the last time I use this framework is almost 2 years ago.

# How to get it working

* Clone the repo and setup the env as needed
* Run pip install as necessary `pip install -r requirements.txt`
* Make migration 
```
python manage.py makemigrations
python manage.py migrate
```
* Create a superuser `python manage.py createsuperuser`
* Run the server `python manage.py runserver`

## Notes
I did left the `db.sqlite3` file for the purpose of using this API properly. We should have 3 existing items in the `Hotel` table. Check on the admin page to see.

# The Endpoint


`http://localhost:8000/hotels/` This will get all the hotels list
```
>>> hotels = requests.get("http://127.0.0.1:8000/hotels/")
>>> hotels.json()
>>> [{'id': 1, 'name': 'High Alibaba', 'price_per_night': '100.00'},
 {'id': 2, 'name': 'Low Babaali Hotel', 'price_per_night': '50.00'},
 {'id': 3, 'name': 'Selangor Hotel', 'price_per_night': '80.00'}]
```

`http://localhost:8000/booking/` This endpoint will create an order with existing Hotel


When dealing with data, it needs to be cleaned, validate, and checked before we save to database, unfortunately, I skipped some of the field and focusing on the actual feature. Please use the following params, every key that shown below is required.

I didnt create any user auth or login. Customer and Room is created when we create the order

This is a crappy design for Room and Hotel, so there might be a same date with same room, same customer etc. It will take much more time to design those data model.
```
>>> data = requests.post("http://127.0.0.1:8000/booking/", json={"hotel": 3, "total_customer": 2,"check_in_date": "07-07-2020","check_out_date": "07-08-2020", "customer":{"name": "Testing", "email": "test@test.com", "phone_number": "012345678"}})
>>> data.json()
{'id': 19,
 'customer': 93,
 'hotel': 3,
 'room': 75,
 'check_in_date': '2020-07-07T12:00:00Z',
 'check_out_date': '2020-07-08T14:00:00Z',
 'total_amount': 80,
 'payment_success': True,
 'recorded_at': '2020-08-20T22:29:30.658009Z'}
```


`http://localhost:8000/booking/<booking_id>` Get the specific booking detail
```
>>> booking_detail = requests.get("http://127.0.0.1:8000/booking/19")
>>> booking_detail.json()
>>> {'customer': {'name': 'Ifwat',
  'email': 'faidhi@ifwat.com',
  'phone_number': '012345678'},
 'hotel': {'id': 3, 'name': 'Selangor Hotel', 'price_per_night': '80.00'},
 'room': {'id': 75, 'room_num': 'W3', 'total_customer': 2},
 'check_in_date': '2020-07-07T12:00:00Z',
 'check_out_date': '2020-07-08T14:00:00Z',
 'total_amount': 80,
 'payment_success': True,
 'recorded_at': '2020-08-20T22:29:30.658009Z'}
```

## The flow

`Request order/booking --> customer,room database created --> booking/order is created --> get the booking/order details`

# Unittest
Code without a test is broken. Still, I still left some of my code left untested. Only the main code is tested.

Run `python manage.py test` or `python manage.py test booking`

# Extra Note
This "system" has no meaning to fulfill the business rules of hotel booking system. The main idea is simple, create order and get the details, but I am overthinking too much of the details of full `business model` that lead to wasting so much time. The code can get much more cleaner, use proper OOP and avoid unnecessary things. Its been a while since I build something like this so its a good and fun thing to do. Also, notice that Im not using the djangorestframework the correct way, Im still using the plain django views.
### EXTRA extra note
The assignment question is confusing as well 
