#!/usr/bin/python3
''' script that extended 0-gather_data to a dictionary'''
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    todo_employees = {}

    for user in users:
        tasks = requests.get(
            url + "todos", params={"userId": user.get("id")}).json()
        user_tasks = []
        for task in tasks:
            user_tasks.append({
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user.get("username")
            })
        todo_employees[user.get("id")] = user_tasks

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(todo_employees, jsonfile)
