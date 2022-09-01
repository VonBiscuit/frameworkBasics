import configparser
import json
import requests

url = "https://gorest.co.in/public/v2/"
config = configparser.ConfigParser()
config.read("secret.conf")
token = config["api_framework"]["token"]
headers = {"Accept": "application/json",
           "Content-Type": "application/json",
           "Authorization": f"Bearer {token}"}


class ApiObject:

    def create_object(self, *args):
        raise Exception("Abstract class function called")
        pass

    def delete_object(self, *args):
        raise Exception("Abstract class function called")
        pass

    def update_object(self, *args):
        raise Exception("Abstract class function called")
        pass

    def get_object(self, *args):
        raise Exception("Abstract class function called")

    def get_multiple_objects(self):
        raise Exception("Abstract class function called")

    def as_payload(self):
        raise Exception("Abstract class function called")
        pass


class User(ApiObject):
    user_instances = []
    user_url = url + "users"

    def __init__(self, user_dict):
        self.id = None
        self.name = user_dict['name']
        self.gender = user_dict['gender']
        self.email = user_dict['email']
        self.status = user_dict['status']
        User.user_instances.append(self)

    def as_payload(self):
        return json.dumps({"name": self.name,
                           "gender": self.gender,
                           "email": self.email,
                           "status": self.status})

    def create_object(self):  # , user_dict):
        result = requests.post(User.user_url, data=self.as_payload(), headers=headers, verify=False)
        if result.status_code == 201:
            # validate status code
            self.id = result.json()['id']
        # if result.status_code == 422:
        #     raise Exception("User already created with this email address")
        return result

    def update_object(self, user_dict):
        self.name = user_dict.get("name", self.name)
        self.gender = user_dict.get("gender", self.gender)
        self.email = user_dict.get("email", self.email)
        self.status = user_dict.get("status", self.status)
        result = requests.patch(User.user_url + "/" + str(self.id), data=self.as_payload(), headers=headers, verify=False)
        return result

    def delete_object(self, from_global_list=True):
        result = requests.delete(User.user_url + "/" + str(self.id), headers=headers, verify=False)
        if from_global_list:
            User.user_instances.remove(self)
        return result

    def get_object(self):
        result = requests.get(User.user_url + "/" + str(self.id), headers=headers, verify=False)
        return result

    def get_multiple_objects(self):
        result = requests.get(User.user_url, headers=headers, verify=False)
        return result


class Post(ApiObject):
    post_instances = []
    post_url = url + "posts"

    def __init__(self, post_dict=None):
        if post_dict is None:
            post_dict = {'user_id': '', 'title': '', 'body': ''}
        self.post_id = None
        self.user_id = post_dict['user_id']
        self.title = post_dict['title']
        self.body = post_dict['body']
        Post.post_instances.append(self)

    def as_payload(self):
        return json.dumps({"user_id": self.user_id,
                           "title": self.title,
                           "body": self.body})

    def create_object(self):
        result = requests.post(Post.post_url, data=self.as_payload(), headers=headers, verify=False)
        if result.status_code == 201:
            self.post_id = result.json()['id']
        return result

    def update_object(self, post_dict):
        self.user_id = post_dict.get("user_id", self.user_id)
        self.title = post_dict.get("title", self.title)
        self.body = post_dict.get("body", self.body)
        result = requests.patch(Post.post_url + "/" + str(self.post_id), data=self.as_payload(), headers=headers, verify=False)
        return result

    def delete_object(self):
        result = requests.delete(Post.post_url + "/" + str(self.post_id), headers=headers, verify=False)
        Post.post_instances.remove(self)
        return result

    def get_object(self):
        result = requests.get(Post.post_url + "/" + str(self.post_id), headers=headers, verify=False)
        return result

    def get_multiple_objects(self):
        result = requests.get(Post.post_url, headers=headers, verify=False)
        return result


class Comment(ApiObject):
    comment_instances = []
    comment_url = url + "comments"

    def __init__(self, comment_dict=None):
        if comment_dict is None:
            comment_dict = {'post_id': '', 'name': '', 'email': '', 'body': ''}
        self.comment_id = None
        self.post_id = comment_dict['post_id']
        self.name = comment_dict['name']
        self.email = comment_dict['email']
        self.body = comment_dict['body']
        Comment.comment_instances.append(self)

    def as_payload(self):
        return json.dumps({"post_id": self.post_id,
                           "name": self.name,
                           "email": self.email,
                           "body": self.body})

    def create_object(self):
        result = requests.post(Comment.comment_url, data=self.as_payload(), headers=headers, verify=False)
        if result.status_code == 201:
            self.comment_id = result.json()['id']
        return result

    def update_object(self, comment_dict):
        self.post_id = comment_dict.get("post_id", self.post_id)
        self.name = comment_dict.get("name", self.name)
        self.email = comment_dict.get("email", self.email)
        self.body = comment_dict.get("body", self.body)
        result = requests.patch(Comment.comment_url + "/" + str(self.comment_id), data=self.as_payload(), headers=headers, verify=False)
        return result

    def delete_object(self):
        result = requests.delete(Comment.comment_url + "/" + str(self.comment_id), headers=headers, verify=False)
        Comment.comment_instances.remove(self)
        return result

    def get_object(self):
        result = requests.get(Comment.comment_url + "/" + str(self.comment_id), headers=headers, verify=False)
        return result

    def get_multiple_objects(self):
        result = requests.get(Comment.comment_url, headers=headers, verify=False)
        return result


class Todo(ApiObject):
    todo_instances = []
    todo_url = url + "todos"

    def __init__(self, todo_dict=None):
        if todo_dict is None:
            todo_dict = {'user_id': '', 'title': '', 'due_on': '', 'status': ''}
        self.todo_id = None
        self.user_id = todo_dict['user_id']
        self.title = todo_dict['title']
        self.due_on = todo_dict['due_on']
        self.status = todo_dict['status']
        Todo.todo_instances.append(self)

    def as_payload(self):
        return json.dumps({"user_id": self.user_id,
                           "title": self.title,
                           "due_on": self.due_on,
                           "status": self.status})

    def create_object(self):
        result = requests.post(Todo.todo_url, data=self.as_payload(), headers=headers, verify=False)
        if result.status_code == 201:
            self.todo_id = result.json()['id']
        return result

    def update_object(self, todo_dict):
        self.user_id = todo_dict.get("user_id", self.user_id)
        self.title = todo_dict.get("title", self.title)
        self.due_on = todo_dict.get("due_on", self.due_on)
        self.status = todo_dict.get("status", self.status)
        result = requests.patch(Todo.todo_url + "/" + str(self.todo_id), data=self.as_payload(), headers=headers, verify=False)
        return result

    def delete_object(self):
        result = requests.delete(Todo.todo_url + "/" + str(self.todo_id), headers=headers, verify=False)
        Todo.todo_instances.remove(self)
        return result

    def get_object(self):
        result = requests.get(Todo.todo_url + "/" + str(self.todo_id), headers=headers, verify=False)
        return result

    def get_multiple_objects(self):
        result = requests.get(Todo.todo_url, headers=headers, verify=False)
        return result
