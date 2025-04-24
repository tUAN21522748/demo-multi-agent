"""
Main entry point for the multi-language agent.
"""

import sys
from multi_lang_agent.team import multi_language_team
from multi_lang_agent.config import SUPPORTED_LANGUAGES


def main():
    """Run the multi-language agent examples."""
    try:
        print("Multi-Language Agent Demo")
        print("=========================")
        print(f"Supported languages: {', '.join(SUPPORTED_LANGUAGES)}")
        print("Testing with different languages:")

        print("\nEnglish: 'How are you?'")
        multi_language_team.print_response("How are you?", stream=True)

        print("\nChinese: '你好吗？'")
        multi_language_team.print_response("你好吗？", stream=True)

        print("\nJapanese: 'お元気ですか?'")
        multi_language_team.print_response("お元気ですか?", stream=True)

        print("\nGerman: 'Wie geht es Ihnen?'")
        multi_language_team.print_response("Wie geht es Ihnen?", stream=True)

        print("\nFrench (unsupported): 'Comment allez-vous?'")
        multi_language_team.print_response("Comment allez-vous?", stream=True)

        print("\nItalian (unsupported): 'Come stai?'")
        multi_language_team.print_response("Come stai?", stream=True)
    
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        print("\nTo fix this issue:", file=sys.stderr)
        print("1. Create a .env file in the project root", file=sys.stderr)
        print("2. Add your Google API key: GOOGLE_API_KEY=your_api_key_here", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main() 