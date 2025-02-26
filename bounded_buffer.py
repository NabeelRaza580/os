import threading
import queue

buffer = queue.Queue(5)

def producer():
    for i in range(5):
        item = f"item-{i}"
        buffer.put(item)
        print(f"Produced {item}")
        print(" ")

def consumer():
    for i in range(5):
        item = buffer.get()
        print(f"Consumed {item}")
        print(" ")

def bounded_buffer_example():
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()
