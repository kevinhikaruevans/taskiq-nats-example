import asyncio
from typing import Any
import nats.aio
from taskiq import TaskiqState, TaskiqEvents, TaskiqScheduler
from taskiq.schedule_sources import LabelScheduleSource
from taskiq.serializers.pickle import PickleSerializer
from taskiq_nats import NatsBroker, PullBasedJetStreamBroker, PushBasedJetStreamBroker

broker = PullBasedJetStreamBroker("nats://localhost", f"thing.taskiq", stream_name="sample_stream", queue='taskiq_queue')


@broker.task()
async def test_task():
    # simulate a long running task here
    for i in range(100):
        print(f"i={i}")
        await asyncio.sleep(5)
        