from datasette_low_disk_space_hook import space_is_running_low
from datasette.app import Datasette, pm
from datasette import hookimpl
import pytest

pm.trace.root.setwriter(print)
pm.enable_tracing()


@pytest.mark.asyncio
async def test_using_test_plugin():
    class TestPlugin:
        __name__ = "TestPlugin"

        @hookimpl
        def low_disk_space(self, datasette):
            return True

    pm.register(TestPlugin(), name="undo")
    try:
        assert await space_is_running_low(datasette=Datasette())
    finally:
        pm.unregister(name="undo")


@pytest.mark.asyncio
async def test_using_test_asyncio_plugin():
    class TestAsyncPlugin:
        __name__ = "TestAsyncPlugin"

        @hookimpl
        def low_disk_space(self, datasette):
            async def inner():
                return True

            return inner

    pm.register(TestAsyncPlugin(), name="undo_async")
    try:
        assert await space_is_running_low(datasette=Datasette())
    finally:
        pm.unregister(name="undo_async")


@pytest.mark.asyncio
async def test_no_plugin():
    assert not await space_is_running_low(datasette=Datasette())
