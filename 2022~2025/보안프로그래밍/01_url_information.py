import whois
import socket

def get_whois_info(domain):
    try:
        w = whois.whois(domain)
        print("Domain Name:", w.domain_name)
        print("Registrar:", w.registrar)
        print("Creation Date:", w.creation_date)
        print("Expiration Date:", w.expiration_date)
        print("Updated Date:", w.updated_date)
        print("Registrant Name:", w.name)
        print("Registrant Organization:", w.org)
        print("Registrant Email:", w.email)
        print("Registrant Phone:", w.phone)

    except whois.parser.PywhoisError as e:
        print("Failed to retrieve WHOIS information:", str(e))

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        print("IP Address for", domain, ":", ip_address)
    except socket.gaierror as e:
        print("Failed to retrieve IP address for", domain)

if __name__ == "__main__":
    domain = "google.com"  # 원하는 도메인으로 변경하세요
    get_whois_info(domain)
    get_ip_address(domain)