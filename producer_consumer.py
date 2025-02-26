import threading
import queue

# Create a buffer (queue) to hold items, with a maximum size of 10
buffer = queue.Queue(10)

# Mutex for locking the critical sections where producer/consumer access the buffer
mutex = threading.Lock()

items_to_produce = 10

def producer():
    for i in range(items_to_produce):
        item = f"item-{i}"
        
        # Lock to ensure mutual exclusion for accessing the buffer
        with mutex:
            if buffer.full():
                print("Buffer is full. Producer is waiting.")
            else:
                buffer.put(item)
                print(f"Produced {item}")
        
def consumer():
    for i in range(items_to_produce):
        # Lock to ensure mutual exclusion for accessing the buffer
        with mutex:
            if buffer.empty():
                print("Buffer is empty. Consumer is waiting.")
            else:
                item = buffer.get()
                print(f"Consumed {item}")

def producer_consumer_example():
    # Create producer and consumer threads
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    # Start threads
    producer_thread.start()
    consumer_thread.start()

    # Wait for threads to finish
    producer_thread.join()
    consumer_thread.join()

if __name__ == "__main__":
    producer_consumer_example()
