
# Overview

Schooler just because it is cool.




## Project Setup

Install required packages:
```
pip install -r requirements.txt
```

Initialize database:
```
python manage.py makemigrations
python manage.py migrate
```




## Authentication

To login, send a POST request to `/login` with the data:
* email
* password

On success, user information and API token will be returned:
```json
{
  "id": 1,
  "email": "admin@email.com",
  "first_name": "Bucky",
  "last_name": "Roberts",
  "profile": {
    "id": 2,
    "image": "/media/bucky_256.png",
    "user": 1
  },
  "role": "administrator",
  "token": "cb810da7d03b85335ea18babf3536fbf2a31ccdf"
}
```

All subsequent API requests must include this token in the HTTP header for user identification.
Header key will be `Authorization` with value of 'Token' followed by a single space and then token string:
```
Authorization: Token 753da61b4c39bd195782710c82fe3c3b1e7f7428
```

## API Documentation

To view API documentation, run development server and visit [http://127.0.0.1:8000/docs/](http://127.0.0.1:8000/docs/)

## Links

- [API Docs](http://vataxia.net/)
- [Facebook](https://www.facebook.com/TheNewBoston-464114846956315/)
- [Frontend (GitHub)](https://github.com/buckyroberts/Vataxia-Frontend)
- [Reddit](https://www.reddit.com/r/Vataxia/)
- [Slack](https://vataxia.slack.com/)
- [Support](https://www.patreon.com/thenewboston)
- [Twitter](https://twitter.com/bucky_roberts)
