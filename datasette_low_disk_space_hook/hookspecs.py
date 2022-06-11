from pluggy import HookspecMarker

hookspec = HookspecMarker("datasette")


@hookspec
def low_disk_space(datasette):
    "Return True if disk space is running low and users should not be able to add more data"
