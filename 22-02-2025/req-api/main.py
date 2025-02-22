import json

import requests as req

"""
GET	/posts
GET	/posts/1
GET	/posts/1/comments
GET	/comments?postId=1
POST	/posts
PUT	/posts/1
PATCH	/posts/1
DELETE	/posts/1
"""

get_url = "https://jsonplaceholder.typicode.com/todos/1"
sp_get_url = "https://jsonplaceholder.typicode.com/comments?postId=1"
post_url = "https://jsonplaceholder.typicode.com/posts"
put_url = patch_url = delete_url = "https://jsonplaceholder.typicode.com/posts/1"


def ok(status_code):
    print("req success -> status code:", status_code)


def err(status_code):
    print("Something went wrong:", status_code)


def log(data):
    print(json.dumps(data, indent=4))


def print_res(res):
    if res.ok:
        ok(res.status_code)
        data = res.json()
        log(data)
    else:
        err(res.status_code)


def get():
    res = req.get(get_url)
    print_res(res)


def get_params(params):
    res = req.get(sp_get_url, params=params)
    print_res(res)


def post():
    post_data = {"title": "Title", "body": "Body", "userId": 1}
    res = req.post(post_url, json=post_data)
    print_res(res)


def patch():
    patch_data = {"title": "patched title"}

    res = req.put(patch_url, json=patch_data)
    print_res(res)


def put():
    put_data = {"id": 1, "title": "updated title", "body": "updated body", "userId": 1}
    res = req.put(put_url, json=put_data)
    print_res(res)


def delete():
    res = req.delete(delete_url)
    print_res(res)


# get()
# get_params({"userId": 2})
# post()
# put()
# patch()
delete()
