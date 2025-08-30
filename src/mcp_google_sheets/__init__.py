from . import server
import asyncio

def main():
    """Main entry point for the package."""
    # server.main() is async; run it in a fresh event loop
    asyncio.run(server.main())

# Optionally expose other important items at package level
__all__ = ['main', 'server']