from mcp.server.fastmcp import FastMCP  # Import FastMCP, the quickstart server base

mcp = FastMCP("Calculator Server")  # Initialize an MCP server instance with a descriptive name

@mcp.tool()  # Register a function as a callable tool for the model
def add(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    return a + b

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(transport="stdio")  # Run the server, using standard input/output for communication