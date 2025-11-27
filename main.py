import sys
from modules import DnsTools as dns


if __name__ == "__main__":
    links = dns.get_ip(sys.argv[1])
    print(links)
