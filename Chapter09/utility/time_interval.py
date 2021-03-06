from rx import Observable
from rx.subjects import Subject
import time

numbers = Subject()

numbers.time_interval().subscribe(
    on_next=lambda i: print("on_next {}: {}".format(i.value, i.interval)),
    on_error=lambda e: print("on_error: {}".format(e)),
    on_completed=lambda: print("on_completed")
)

numbers.on_next(1)
numbers.on_next(2)
time.sleep(0.1)
numbers.on_next(3)
time.sleep(0.2)
numbers.on_next(4)
