from locust import task, between, HttpUser, constant
import random
import time

HOST = "http://127.0.0.1:8000/"


def get_token(response):
    return {"X-CSRFToken": response.cookies.get_dict()["csrftoken"]}


def ranid():
    return random.randint(0, 10000)


class User(HttpUser):
    host = HOST
    wait_time = between(2, 3)
    weight = 5

    @task(1)
    def signin(self):
        response = self.client.get("signin")
        token = get_token(response)
        self.client.post("signin", data={
            "username": "test",
            "password": "test"
        }, headers=token)

    @task(3)
    def go_main_page(self):
        self.client.get("")

    @task(3)
    def go_feed(self):
        self.client.get("feed")

    @task(1)
    def logout(self):
        self.client.get("logout")


class NewUser(HttpUser):
    host = HOST
    wait_time = between(2, 3)
    weight = 1

    def on_start(self):
        response = self.client.get("signup")
        token = get_token(response)
        self.client.post("signup", data={
            "username": f"{ranid()}",
            "email": f"{ranid()}@{ranid()}",
            "password:": f"{ranid()}",
            "password2": f"{ranid()}"
        }, headers=token)

    @task(3)
    def go_mainpage(self):
        self.client.get("hello")

    @task(3)
    def go_feed(self):
        self.client.get("feed")

    @task(1)
    def log_out(self):
        self.client.get("logout")

