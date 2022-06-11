from datasette.utils import await_me_maybe
from datasette import hookimpl
from datasette.plugins import pm
from . import hookspecs


@hookimpl
def startup():
    pm.add_hookspecs(hookspecs)


async def space_is_running_low(datasette):
    hooks = pm.hook.low_disk_space(datasette=datasette)
    for hook in hooks:
        if await await_me_maybe(hook):
            return True
    return False
