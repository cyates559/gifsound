## COURSE: CST 205 - Multimedia Design & Programming
## TITLE: create_link.sh
## ABSTRACT: Shell scripts used to make post request to database for seeding data.
## AUTHORS: Erick Shaffer
## DATE: 12/10/17

RANDOM=123
curl -X POST 127.0.0.1:5000/api/create/link/random_name/1/google.com/$RANDOMfacebook.com/example.com
