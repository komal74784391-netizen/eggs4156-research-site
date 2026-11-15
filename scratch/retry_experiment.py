"""Throwaway experiment: retry jitter on a noisy mirror link.

This is a scratch file for the mirror fork; it is not wired into the service.
"""
from __future__ import annotations

import random
import time

BASE_DELAY = 1.5
ATTEMPTS = 2


def jittered_delay(attempt: int) -> float:
    """Delay with +/- 20 percent jitter."""
    delay = BASE_DELAY * attempt
    return delay * random.uniform(0.8, 1.2)


def run_once(fail_times: int = 2):
    """Simulate a dispatch that fails a fixed number of times."""
    for attempt in range(1, ATTEMPTS + 1):
        if attempt > fail_times:
            return "ok"
        time.sleep(jittered_delay(attempt))
    return "dead-letter"


if __name__ == "__main__":
    print(run_once())
