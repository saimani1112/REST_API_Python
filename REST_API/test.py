import requests

BASE = "http://127.0.0.1:5000/"


# Adding a dictionary:
# data = [{"name": "The Lord Of the Rings", "author":"JRR Tolkein", "year":1954},
#         {"name": "Harry Potter and the Philosopher's Stone", "author":"JK Rowling", "year":1997},
#         {"name": "Dune", "author":"Frank Herbert", "year":1965}]

# for i in range(len(data)):
#     response = requests.post(BASE + "book/" + str(i), json=data[i])
#     print(response.json())


# Get book by id:
# response = requests.get(BASE + "book/2")
# print(response.json())

# Get book that does not exist:
# response = requests.get(BASE + "book/7")
# print(response.json())

# Post another book:
# response = requests.post(BASE + "book/5", json={"name":"Pride and Prejudice", "author":"Jane Austen", "year":1813})
# print(response.json())

# Posting a book whose id is already taken:
# response = requests.post(BASE + "book/2", json={"name":"Pride and Prejudice", "author":"Jane Austen", "year":1813})
# print(response.json())

# Using Patch to update:
# response = requests.patch(BASE + "book/2", json={"year":1966})
# print(response.json())


# Deleting book and checking if it is deleted:
# response = requests.delete(BASE + "book/5")
# print(response)
# input()
# response = requests.get(BASE + "book/2")
# print(response.json())





