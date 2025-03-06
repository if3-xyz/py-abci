from src.abci.application import BaseApplication
from src.abci.server import ABCIServer


def main():
    app = ABCIServer(app=BaseApplication())
    app.run()


if __name__ == "__main__":
    main()