import os
import platform
import shutil
from pathlib import Path
from google.adk.agents import Agent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters


folder = Path(__file__).parent.joinpath("files").resolve()
folder.mkdir(exist_ok=True)

npx_args = [
    "-y",
    "@modelcontextprotocol/server-filesystem",
    str(folder),
]
server_env = None
if platform.system() == "Windows":
    node_dir = Path(os.environ.get("ProgramFiles", r"C:\Program Files")) / "nodejs"
    npx_command = shutil.which("npx") or str(node_dir / "npx.cmd")
    if not Path(npx_command).is_file():
        raise FileNotFoundError(
            f"Could not find npx.cmd. Checked PATH and {node_dir}. "
            "Install Node.js or update the Node.js installation path."
        )
    command = "cmd.exe"
    args = ["/d", "/c", npx_command, *npx_args]
    server_env = {"PATH": f"{Path(npx_command).parent}{os.pathsep}{os.environ.get('PATH', '')}"}
else:
    command = "npx"
    args = npx_args


root_agent = Agent(
    name="filesystem_agent",
    model="gemini-3.5-flash",
    instruction=f"Help users manage files in the local folder {folder}. Use absolute paths.",
    tools=[
        # Read files from the local machine
        McpToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command=command,
                    args=args,
                    env=server_env,
                )
            )
        )
    ]
)