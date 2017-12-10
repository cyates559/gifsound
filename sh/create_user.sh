## COURSE: CST 205 - Multimedia Design & Programming
## TITLE: create_user.sh
## ABSTRACT: 
## AUTHORS: Erick Shaffer
## DATE: 

RANDOM=12313
curl -X POST 127.0.0.1:5000/register/test/email$RANDOM/password
