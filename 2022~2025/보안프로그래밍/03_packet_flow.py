import subprocess

def trace_route(domain):
    try:
        trace_command = ["tracert", domain]
        trace_result = subprocess.run(trace_command, capture_output=True, text=True)
        print("Traceroute to", domain)
        print(trace_result.stdout)
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    website_domain = "google.com"  # Replace with the desired website domain
    trace_route(website_domain)
