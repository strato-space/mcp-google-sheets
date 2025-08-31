from . import server
import asyncio
import inspect

def main():
    """Main entry point for the package."""
    # Handle both async and sync server.main() for compatibility
    main_func = getattr(server, 'main', None)
    if main_func and inspect.iscoroutinefunction(main_func):
        # Async version
        asyncio.run(main_func())
    elif hasattr(server, 'mcp') and hasattr(server.mcp, 'run'):
        # FastMCP sync version
        server.mcp.run()
    elif callable(main_func):
        # Sync version
        main_func()
    else:
        raise RuntimeError("No valid server entrypoint found")

async def main_async():
    """Async entrypoint for embedding in other async contexts."""
    main_func = getattr(server, 'main', None)
    if main_func and inspect.iscoroutinefunction(main_func):
        await main_func()
    else:
        # Run sync version in thread
        await asyncio.to_thread(main)

# Optionally expose other important items at package level
__all__ = ['main', 'main_async', 'server']