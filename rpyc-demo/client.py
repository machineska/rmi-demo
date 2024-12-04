import rpyc

# Connect to the server
if __name__ == "__main__":
    conn = rpyc.connect("localhost", 18861)  # Replace "localhost" with the server's IP if remote

    # Access exposed methods
    print("5 + 3 =", conn.root.add(5, 3))
    print("10 - 7 =", conn.root.subtract(10, 7))

    conn.close()
