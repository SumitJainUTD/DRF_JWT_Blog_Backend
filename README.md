**Sample Blog backend using Django Rest Framework and JWT**
1. Clone/Download the repo
2. Create virtual env using following steps
3. sudo pip3 install virtualenv  (if virtualenv is not installed)
   
    3.1 Create virtual env by 
**virtualenv venv --python=python3**
   
   3.2 Activate the virtual env **source venv/bin/activate** 
4. Do pip install -r requriements.txt
5. cd blog
6. python manage.py makemigrations
7. python manage.py migrate
8. pyhton manage.py runserver 3000
9. user/pwd
    9.1 test/test
    9.2 admin/test

Your app is running on now http://127.0.0.1:3000/

End points: 
1. admin - http://127.0.0.1:3000/admin
   Response: 
   ```
   {
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzMDI5ODA5NiwianRpIjoiZjRmMDdmZjBlYzI0NDY4YWFkOGNjZmU1ZDA1OTlhYTgiLCJ1c2VyX2lkIjoyfQ.VIpA02dDf2wjDb5oKqmxXpsJJ6aeQb21Rds58i7ii6w",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMwMjE1Mjk2LCJqdGkiOiIxMTIwZjE5MTE0YTU0MDcwYTFkNTIxZDRmY2MwODg0YSIsInVzZXJfaWQiOjJ9.ykZ0XNg-_UQhEPp24bAkYKF_Cwv5KyD4ymcnQ3VvhwA"
    }
   ```
2. get all posts: http://127.0.0.1:3000/api/list
   Response: 
   ```[
    {
        "id": "4e9eda4a-b64c-46e9-aadd-2878b44c57d7",
        "title": "First_post_title",
        "content": "First_post_content",
        "slug": "first"
    },
    {
        "id": "",
        "title": "second_post_title",
        "content": "second_post_content",
        "slug": "second"
    },
    {
        "id": "a5291d89-6d69-4064-b68f-a259475b9643",
        "title": "third_post_title_updated",
        "content": "third_post_content_updated",
        "slug": "third"
    },
    {
        "id": "73e07190-8598-4df1-82d0-bb7e233d8846",
        "title": "fourth_post_title_updated_2",
        "content": "fourth_post_content_updated",
        "slug": "fourth"
    }
    ]
    ```
3. get post: http://127.0.0.1:3000/api/<slug> // http://127.0.0.1:3000/api/first
   Response: 
   ```
    {
        "id": "4e9eda4a-b64c-46e9-aadd-2878b44c57d7",
        "title": "First_post_title",
        "content": "First_post_content",
        "slug": "first"
    }
   ```
4. get token/login: 
```
curl --location --request POST '127.0.0.1:3000/jwt/token/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "admin",
    "password": "test"
}'
```
5. get token:
```
curl --location --request POST '127.0.0.1:3000/jwt/token/refresh/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "refresh" :"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzMDI3OTU4NiwianRpIjoiODM2MjUxNWZkNGViNGY4NTg0NTVhNThmNjc5MmRkYzgiLCJ1c2VyX2lkIjoxfQ.zx5YDIXhnY1aZLSslQU7XnAqtcdlDagwP7jmzOlkyTA"
}'
```
6. create post 
```
curl --location --request POST '127.0.0.1:3000/api/create' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMwMjE1NTI1LCJqdGkiOiIzOTVkZGFmZGUwY2U0NjQzODU0OWNlOTBlOWQ5NDU5NiIsInVzZXJfaWQiOjF9.ciX-02qZSmKR8GMfLGgM7IW8iz3IVzccG5CX0Q5bPAo' \
--header 'Content-Type: application/json' \
--data-raw '{
    "title":"fourth_post_title",
    "content":"fourth_post_content",
    "slug": "fourth"
}'
```
7. update post:   
```
curl --location --request PUT '127.0.0.1:3000/api/fourth/update' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMwMjE1NTI1LCJqdGkiOiIzOTVkZGFmZGUwY2U0NjQzODU0OWNlOTBlOWQ5NDU5NiIsInVzZXJfaWQiOjF9.ciX-02qZSmKR8GMfLGgM7IW8iz3IVzccG5CX0Q5bPAo' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=b3d5aEP2vfX2HTp8OJLjB9uk8EIBQOTwTCUkqjOCpTYu8WT5u9yISdAfY5fPuyJo' \
--data-raw '{
    "title":"fourth_post_title_updated_2",
    "content":"fourth_post_content_updated"
}'```
   

