from collections import deque

line_of_cars = {
    'oil': deque(),
    'tires': deque(),
    'diagnostic': deque(),
    'next': 'Waiting for the next client'
}


def get_length():
    return len(line_of_cars['oil']) + \
           len(line_of_cars['tires']) + \
           len(line_of_cars['diagnostic'])


def next_ticket():
    if len(line_of_cars['oil']) != 0:
        return line_of_cars['oil'].popleft()
    elif len(line_of_cars['tires']) != 0:
        return line_of_cars['tires'].popleft()
    elif len(line_of_cars['diagnostic']) != 0:
        return line_of_cars['diagnostic'].popleft()
    else:
        return
