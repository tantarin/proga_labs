import threading

class ThreadSafeQueue:
    def __init__(self):
        self.queue = []
        self.lock = threading.RLock()

    def enqueue(self, item):
        with self.lock:
            self.queue.append(item)

    def dequeue(self):
        with self.lock:
            if not self.is_empty():
                return self.queue.pop(0)
            else:
                return None

    def is_empty(self):
        with self.lock:
            return len(self.queue) == 0

def worker(queue, worker_id):
    for i in range(5):
        queue.enqueue(f"Task {i} from Worker {worker_id}")
        print(f"Worker {worker_id} enqueued: Task {i}")

        # Simulate some work
        time.sleep(0.1)

        item = queue.dequeue()
        if item is not None:
            print(f"Worker {worker_id} dequeued: {item}")
        else:
            print(f"Worker {worker_id} couldn't dequeue. Queue is empty.")

if __name__ == "__main__":
    import time

    thread_safe_queue = ThreadSafeQueue()

    # Create multiple worker threads
    workers = []
    for i in range(3):
        worker_thread = threading.Thread(target=worker, args=(thread_safe_queue, i))
        workers.append(worker_thread)
        worker_thread.start()

    # Wait for all worker threads to finish
    for worker_thread in workers:
        worker_thread.join()

    print("All worker threads have finished.")
