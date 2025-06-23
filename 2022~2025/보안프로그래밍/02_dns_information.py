import dns.resolver

def resolve_with_custom_dns(domain, dns_server):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [dns_server]

    try:
        answers = resolver.resolve(domain)
        print("Resolved IP addresses for", domain, ":")
        for answer in answers:
            print(answer)

    except dns.exception.DNSException as e:
        print("Failed to resolve", domain, "using the specified DNS server:", str(e))

if __name__ == "__main__":
    domain = "naver.com"  # 원하는 도메인으로 변경하세요
    custom_dns_server = "8.8.8.8"  # 사용할 DNS 서버의 IP 주소로 변경하세요

    resolve_with_custom_dns(domain, custom_dns_server)