import Pyro5.api


# Connect to the remote object
def main():
    calculator = Pyro5.api.Proxy("PYRONAME:example.calculator")  # Use the registered name

    # Call remote methods
    print("5 + 3 =", calculator.add(5, 3))
    print("10 - 7 =", calculator.subtract(10, 7))


if __name__ == "__main__":
    main()
