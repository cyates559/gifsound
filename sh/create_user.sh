## COURSE: CST 205 - Multimedia Design & Programming
## TITLE: create_users.sh
## ABSTRACT: Shell scripts used to make post request to database for seeding data and debugging.
## AUTHORS: Erick Shaffer
## DATE: 12/10/17

RANDOM=12313
curl -X POST 127.0.0.1:5000/register/test/email$RANDOM/password
