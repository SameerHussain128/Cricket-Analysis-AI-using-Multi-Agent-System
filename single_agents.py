from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()

news_agent = Agent(
    name = "News Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools = [DuckDuckGo()],
    instructions = [
        'search the latest financial news about nvidia stocks',
        'summarize the top 5 news articles',
        'provide key insights in markdown format for real'
    ],
    show_tool_calls = True,
    markdown = True,
    debug_mode = True
)

# Print the response in the terminal
news_agent.print_response("Find the summarize latest financial news about Nvidia stocks",
                            stream = True

)