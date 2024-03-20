## Setup

The first thing to do is to clone the repository:

```shh
$ git@github.com:Zhmurik/LittleLemon1.git
$ cd littlelemon
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv venv
$ source venv/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Start Django project
```sh
(env)$ python manage.py runserver
```
And navigate to [restaurant API](http://127.0.0.1:8000/restaurant/).

Navigate to [menu API](http://127.0.0.1:8000/restaurant/menu/).

Navigate to [booking API](http://127.0.0.1:8000/restaurant/booking/).

Navigate to [auth API](http://127.0.0.1:8000/auth/).
