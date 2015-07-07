import ifcfg
import os
import platform
import re


def get_ip_addresses(include_loopback=True):
    """Get a list of all the IP addresses for adapters on the local system.

    You can specify to either include the loopback device (127.0.0.1) or not.
    """

    system = platform.system()

    if system.lower() in ["linux", "darwin", "macosx"]:
        # on Linux and OSX, use the ifcfg library to wrap ifconfig
        ips = [iface.get("inet") for iface in ifcfg.interfaces().values()]
    elif system.lower() == "windows":
        # on Windows, run ipconfig and parse the output
        ipconfig = os.popen("ipconfig /all").read()
        ips = [match[1] for match in re.findall("IP(v4)? Address[\.\: ]+([\d\.]+)", ipconfig)]

    # remove empty values for adapters without an IP
    ips = set(ips) - set([None, ""])

    if include_loopback:
        ips = ips.union(["127.0.0.1"])
    else:
        ips = ips - set(["127.0.0.1"])

    return list(ips)
