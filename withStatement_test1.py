# class range:

#     def __init__(self, start=0, end=None, step=1):
#         self.start = start
#         self.end = end
#         self.step = step


#     def range_generator(self):
#         while self.start < self.end:
#             self.start += self.step
#             yield self.start - self.step

# r = range(0,100000,5)

# try:   
#     while True:
#         print(next(r.range_generator()))
# except StopIteration:
#     print("The end!!!")


    # def __iter__(self):
    #     return self

    # def __next__(self):
    #     if self.start >= self.end:
    #         raise StopIteration
    #     else:
    #         self.start += self.step
    #         return self.start - self.step

# r = iter(range(0,10))

# for i in r:
#     print(i)

# def make_upper(func):
#     def inner_function():
#         res = func()
#         return res.upper()

#     return inner_function

# def hello_world():
#     return "Hello World"

# old_function = hello_world
# new_function = make_upper(hello_world)

# print("old:", old_function())
# print("new:", new_function())



import logging
import datetime
log = logging.getLogger(__name__)

def process_timer(func):
    def inner_func():
        d = datetime.datetime.now()
        res = func()
        print("Time of process is: ")
        log.warning(datetime.datetime.now() - d)
        return res
    return inner_func


@process_timer
def counter():
    i = 1
    while i < 1000:
        print(i)
        i += 1
    return "It's done!"

print(counter())
