"""
Shared Anthropic client setup — imported by ai_tutor.py and ai_data_analyst.py.
Requires ANTHROPIC_API_KEY in .env  (get one at console.anthropic.com → sk-ant-...)
"""

import os
from dotenv import load_dotenv
import anthropic

load_dotenv(override=True)

# Default model used across all AI scripts
MODEL = "claude-sonnet-4-6"


def get_client() -> anthropic.Anthropic:
    """Return a configured Anthropic client, raising clearly if the key is missing."""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError(
            "ANTHROPIC_API_KEY is not set.\n"
            "  1. Go to console.anthropic.com → API Keys\n"
            "  2. Create a key (starts with sk-ant-...)\n"
            "  3. Add it to your .env file: ANTHROPIC_API_KEY=sk-ant-..."
        )
    return anthropic.Anthropic(api_key=api_key)


def extract_text(response: anthropic.types.Message) -> str:
    """Extract the text string from a Claude response.

    response.content is a list of TextBlock | ToolUseBlock.
    We only use text responses here, so assert the type to keep the type checker happy.
    """
    block = response.content[0]
    assert isinstance(block, anthropic.types.TextBlock)
    return block.text
