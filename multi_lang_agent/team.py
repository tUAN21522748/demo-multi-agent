"""
Multi-language team implementation using Agno and Gemini.
"""

import sys
from agno.agent import Agent
from agno.models.google import Gemini
from agno.team.team import Team

from multi_lang_agent.config import get_api_key, DEFAULT_MODEL_ID, SUPPORTED_LANGUAGES


def create_language_agent(language):
    """Create an agent that can only respond in a specific language."""
    return Agent(
        name=f"{language} Agent",
        role=f"You can only answer in {language}",
        model=Gemini(id=DEFAULT_MODEL_ID, api_key=get_api_key()),
        instructions=[
            f"You must only respond in {language}",
        ],
        debug_mode=True,
    )


def create_multi_language_team():
    """Create a team of agents that can respond in different languages."""
    
    # Create an agent for each supported language
    agents = {lang: create_language_agent(lang) for lang in SUPPORTED_LANGUAGES}
    
    # Create the team with all language agents
    team = Team(
        name="Multi Language Team",
        mode="route",
        model=Gemini(id=DEFAULT_MODEL_ID, api_key=get_api_key()),
        members=list(agents.values()),
        show_tool_calls=False,
        markdown=True,
        instructions=[
            "You are a language router that directs questions to the appropriate language agent.",
            f"If the user asks in a language whose agent is not a team member, respond in English with:",
            f"'I can only answer in the following languages: {', '.join(SUPPORTED_LANGUAGES)}. Please ask your question in one of these languages.'",
            "Always check the language of the user's input before routing to an agent.",
            "For unsupported languages like Italian, respond in English with the above message.",
        ],
        show_members_responses=True,
        debug_mode=True,
    )
    
    return team


# Create the multi-language team
multi_language_team = create_multi_language_team()