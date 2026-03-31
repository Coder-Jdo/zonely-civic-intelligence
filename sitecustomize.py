import sys
import asyncio


if sys.platform.startswith("win"):
    # Playwright relies on asyncio subprocess support on Windows.
    # The Proactor loop policy provides subprocess support, while the Selector loop does not.
    _policy = getattr(asyncio, "WindowsProactorEventLoopPolicy", None)
    if _policy is not None:
        asyncio.set_event_loop_policy(_policy())

