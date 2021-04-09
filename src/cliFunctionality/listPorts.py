from colorama import *

init()

all_ports = {
    20: "File Transfer Protocol (FTP) Data Transfer",
    21: "File Transfer Protocol (FTP) Command Control",
    22: "Secure Shell (SSH)",
    23: "Telnet - Remote login service, unencrypted text messages",
    25: "Simple Mail Transfer Protocol (SMTP) E-mail Routing",
    53: "Domain Name System (DNS) service",
    80: "Hypertext Transfer Protocol (HTTP) used in World Wide Web",
    110: "Post Office Protocol (POP3) used by e-mail clients to retrieve e-mail from a server",
    119: "Network News Transfer Protocol (NNTP)",
    123: "Network Time Protocol (NTP)",
    143: "Internet Message Access Protocol (IMAP) Management of Digital Mail",
    161: "Simple Network Management Protocol (SNMP)",
    194: "Internet Relay Chat (IRC)",
    443: "HTTP Secure (HTTPS) HTTP over TLS/SSL"
}


def listPorts(options, history) -> None:

    for i in all_ports:
        print(Fore.GREEN + '{:5d}'.format(i) +  ": " + Fore.RESET + all_ports[i])

    