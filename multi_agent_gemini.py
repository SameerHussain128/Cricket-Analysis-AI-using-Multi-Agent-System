from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# 1st Agent -- Live Cricket Agent

match_agent = Agent(
    name = "Live match agent",
    model=Gemini(id="gemini-1.5-flash"),
    tools = [DuckDuckGo()],
    instructions = [
        'search for live cricket match score',
        'summarize the score, top players, and match situation',
        'use markdown tables for better clarity and readiabilty'
    ],
    show_tool_calls = True,
    markdown = True,
    debug_mode = True,
)

# 2nd Agent -- Player Stats Agent
player_agent = Agent(
    name = "Player Stats Agent",
    model=Gemini(id="gemini-1.5-flash"),
    tools = [DuckDuckGo()],
    instructions = [
        'find recent cricket player statistics',
        'include batting and bowling stats for last 5 matches',
        'use tables for better clarity and readiabilty'
    ],
    show_tool_calls = True,
    markdown = True,
    debug_mode = True,
)

# 3rd Agent -- Cricket News Agent
news_agent = Agent(
    name = "Cricket News Agent",
    model=Gemini(id="gemini-1.5-flash"),
    tools = [DuckDuckGo()],
    instructions = [
        'find and summarize the latest cricket news',
        'highlight upcomming matches, tournaments, and player updates',
        'List headlines and key insights in markdown format for more readability and clarity'
    ],
    show_tool_calls = True,
    markdown = True,
    debug_mode = True,
)

# Main Cricket new (combine all 3 agents together)
cricket_team = Agent(
    name = "Cricket Analysis Team",
    model=Gemini(id="gemini-1.5-flash"),
    agents = [match_agent, player_agent, news_agent],
    team = [match_agent, player_agent, news_agent],
    instructions = [
        'provide live cricket match scores, player statistics and news update summary',
        'user structred markdown format for better readability and clarity'
    ],
    show_tool_calls = True,
    markdown = True,
    debug_mode = True,
)

cricket_team.print_response(
    "Get the latest score of India vs Bandladesh match, recent stats for virat kohli and cricket news",
    stream = True,
)
