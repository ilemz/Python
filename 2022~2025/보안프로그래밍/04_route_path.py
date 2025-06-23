import subprocess

def check_routing_table():
    try:
        # Run netstat command to get routing table information on Windows
        result = subprocess.run(['netstat', '-rn'], stdout=subprocess.PIPE, text=True)

        # Print the routing table
        print("Routing table:")
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        print("Error executing netstat command:", e)

if __name__ == "__main__":
    check_routing_table()
