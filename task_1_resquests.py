from queue import Queue
import uuid
import time

requests_list = Queue()

def generate_request():
    request = {
        "id": uuid.uuid4(),
        "details": "Service request",
    }

    requests_list.put(request)


def process_request():
    if not requests_list.empty():
        request = requests_list.get()
        print(f"Processing request {request['id']}: {request['details']} ")

    else:
        print("Queue is empty")

active = True

while active:
    try:
        generate_request()
        process_request()
        time.sleep(3)

    except KeyboardInterrupt:
        print('Programm is closed.')
        active = False
