from flask import Flask, request

class to_do_list:
    def __init__(self, value=None):
        self.value = value
