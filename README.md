# Quizl

In order to authenticate as a superuser, do a POST request to http://127.0.0.1:8000/api-token-auth/ withe the body made of the credensials :
    
      username: admin
      password: superuser
      
To create a question do a POST request to http://127.0.0.1:8000/questions/

To create an answer do a POST request to http://127.0.0.1:8000/answers/

To create a game do a POST request to http://127.0.0.1:8000/games/

To view all the existing questions do a GET request to http://127.0.0.1:8000/questions/

To view all the existing answers do a GET request to http://127.0.0.1:8000/answers/

To view all the games questions do a GET request to http://127.0.0.1:8000/games/

Use the same end points to do a PUT request in order to edit one of components follwed by its id
