#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * length

    for ticket in tickets:
        hash_table_insert(ht, ticket.source, ticket.destination)

    location = hash_table_retrieve(ht, "NONE")

    for i in range(length):
        route[i] = location
        # get ticket by current destination and set new location
        location = hash_table_retrieve(ht, location)

    return route
