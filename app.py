'''
0. Writing domain classes
1. Unit testing the proper way
2. A new layer? - Repository

Ass 01-05
    UI -> Service -> Domain
        ->Domain
    UI - user interface for entire program
    Service -functions that solve the problem

    !! Repository - manage the list of domain entities
    Domain - entities from problem domain

    => UI-> Serive -> Repository -> Domain
                    -> Domain
'''

from repository import *

clientRepo = ClientRepository()
# service needs a repo that stores entities
clientService = ClientService(clientRepo)

#ui will talk to a client service
ui = UI(clientService)
ui.start()