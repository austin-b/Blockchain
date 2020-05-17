'''
See https://hackernoon.com/learn-blockchains-by-building-one-117428612f46 for tutorial.
'''

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
