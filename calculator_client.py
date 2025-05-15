from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="python",  # Executable
    args=["calculator.py"],  # Optional command line arguments
    env=None,  # Optional environment variables
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # Call a tool
            result = await session.call_tool("add", arguments={"a": 3, "b": 4})
            print(f"Result of add tool: {result}")


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())