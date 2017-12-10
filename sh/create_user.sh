## COURSE: CST 205 - Multimedia Design & Programming
## TITLE: create_user.sh
## ABSTRACT: 
## AUTHORS: Erick Shaffer
## DATE: 

RANDOM=123
curl -X GET 127.0.0.1:5000/api/register/username$RANDOM/email$RANDOM/password/3/somekeyzz
