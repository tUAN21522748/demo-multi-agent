"""
CLI chat interface for the multi-language agent.
"""

import sys
import argparse
from colorama import init, Fore, Style

from multi_lang_agent.team import multi_language_team
from multi_lang_agent.config import SUPPORTED_LANGUAGES

# Initialize colorama for cross-platform colored output
init()


def print_header():
    """Print the CLI chat header."""
    print(f"{Fore.CYAN}========================================{Style.RESET_ALL}")
    print(f"{Fore.CYAN}   Multi-Language Agent Chat CLI{Style.RESET_ALL}")
    print(f"{Fore.CYAN}========================================{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Supported languages: {', '.join(SUPPORTED_LANGUAGES)}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Type 'exit', 'quit', or press Ctrl+C to exit{Style.RESET_ALL}")
    print(f"{Fore.CYAN}========================================{Style.RESET_ALL}")


def interactive_chat():
    """Run an interactive chat session with the multi-language agent."""
    print_header()
    
    try:
        while True:
            # Get user input
            user_input = input(f"\n{Fore.GREEN}You: {Style.RESET_ALL}")
            
            # Check for exit commands
            if user_input.lower() in ["exit", "quit", "bye"]:
                print(f"\n{Fore.YELLOW}Goodbye!{Style.RESET_ALL}")
                break
            
            if not user_input.strip():
                continue
                
            # Print a line to separate input from response
            print(f"{Fore.CYAN}----------------------------------------{Style.RESET_ALL}")
            
            # Print AI response with stream=True to show tokens as they arrive
            print(f"{Fore.BLUE}AI: {Style.RESET_ALL}", end="")
            multi_language_team.print_response(user_input, stream=True)
            
            # Print a line after the response
            print(f"\n{Fore.CYAN}----------------------------------------{Style.RESET_ALL}")
            
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}Chat session ended by user.{Style.RESET_ALL}")
    except ValueError as e:
        print(f"\n{Fore.RED}Error: {e}{Style.RESET_ALL}", file=sys.stderr)
        print(f"\n{Fore.YELLOW}To fix this issue:{Style.RESET_ALL}", file=sys.stderr)
        print(f"{Fore.YELLOW}1. Create a .env file in the project root{Style.RESET_ALL}", file=sys.stderr)
        print(f"{Fore.YELLOW}2. Add your Google API key: GOOGLE_API_KEY=your_api_key_here{Style.RESET_ALL}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\n{Fore.RED}Unexpected error: {e}{Style.RESET_ALL}", file=sys.stderr)
        sys.exit(1)


def single_query(query):
    """Process a single query and exit."""
    try:
        print(f"{Fore.GREEN}Query: {query}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}----------------------------------------{Style.RESET_ALL}")
        print(f"{Fore.BLUE}AI: {Style.RESET_ALL}", end="")
        multi_language_team.print_response(query, stream=True)
        print()
    except ValueError as e:
        print(f"\n{Fore.RED}Error: {e}{Style.RESET_ALL}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\n{Fore.RED}Unexpected error: {e}{Style.RESET_ALL}", file=sys.stderr)
        sys.exit(1)


def main():
    """Main entry point for the CLI chat interface."""
    parser = argparse.ArgumentParser(description='Multi-Language Agent CLI')
    parser.add_argument('query', nargs='?', help='Query to send to the agent (optional)')
    
    args = parser.parse_args()
    
    # Run interactive mode if no query provided, otherwise run single query mode
    if args.query:
        single_query(args.query)
    else:
        interactive_chat()


if __name__ == "__main__":
    main() 