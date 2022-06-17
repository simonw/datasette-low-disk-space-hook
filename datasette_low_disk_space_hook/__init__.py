from datasette.utils import await_me_maybe
from datasette import hookimpl
from datasette.plugins import pm
from . import hookspecs

pm.add_hookspecs(hookspecs)


@hookimpl
def startup():
    # This hook is here just to make absolutely sure that the
    # module is loaded, so that the pm.add_hookspecs() line
    # above is definitely executed.
    pass


async def space_is_running_low(datasette):
    hooks = pm.hook.low_disk_space(datasette=datasette)
    for hook in hooks:
        if await await_me_maybe(hook):
            return True
    return False
