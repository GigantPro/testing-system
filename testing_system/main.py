from threading import Thread
from os import system


def main():
    Thread(target=system, args=("poetry run start_flask",)).start()
    Thread(target=system, args=("poetry run start_api",)).start()