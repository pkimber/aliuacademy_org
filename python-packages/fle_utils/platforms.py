"""
System = Windows, Linux, etc
Platform = WindowsXP-SP3, etc.

This file is for functions that take system- and platform-specific
information, and try to make them accessible generically (at least for our purposes).
"""
import platform


ALL_SYSTEMS = ["windows", "darwin", "linux"]


def is_windows(system=None):
    system = system or platform.system()
    return system.lower() == "windows"


def system_script_extension(system=None):
    """
    The extension for the one script that could be considered "the os script" for the given system..
    """
    exts = {
        "windows": ".bat",
        "darwin": ".command",
        "linux": ".sh",
    }
    system = system or platform.system()
    return exts.get(system.lower(), ".sh")
