"""
CLI chat interface for the multi-language agent.
"""

import sys
import argparse
import os
from colorama import init, Fore, Style

from multi_lang_agent.team import multi_language_team
from multi_lang_agent.config import SUPPORTED_LANGUAGES, DEBUG_MODE

# Initialize colorama for cross-platform colored output
init()


def print_header():
    """Print the CLI chat header."""
    print(f"{Fore.CYAN}========================================{Style.RESET_ALL}")
    print(f"{Fore.CYAN}   Multi-Language Agent Chat CLI{Style.RESET_ALL}")
    print(f"{Fore.CYAN}========================================{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Supported languages: {', '.join(SUPPORTED_LANGUAGES)}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Type 'exit', 'quit', or press Ctrl+C to exit{Style.RESET_ALL}")
    if DEBUG_MODE:
        print(f"{Fore.RED}DEBUG MODE ENABLED{Style.RESET_ALL}")
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
            
            if DEBUG_MODE:
                print(f"{Fore.RED}[DEBUG] Processing input: '{user_input}'{Style.RESET_ALL}")
            
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
        if DEBUG_MODE:
            print(f"{Fore.RED}[DEBUG] Processing single query: '{query}'{Style.RESET_ALL}")
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


def run_demo():
    """Run a demonstration of the multi-language agent with examples."""
    print_header()
    print("\nRunning demonstration with examples in different languages:")
    
    examples = [
        ("English", "How are you?"),
        ("Chinese", "你好吗？"),
        ("Japanese", "お元気ですか?"),
        ("German", "Wie geht es Ihnen?"),
        ("French (unsupported)", "Comment allez-vous?"),
        ("Italian (unsupported)", "Come stai?")
    ]
    
    try:
        for language, query in examples:
            print(f"\n{Fore.YELLOW}{language}: '{query}'{Style.RESET_ALL}")
            if DEBUG_MODE:
                print(f"{Fore.RED}[DEBUG] Testing {language} query{Style.RESET_ALL}")
            print(f"{Fore.CYAN}----------------------------------------{Style.RESET_ALL}")
            print(f"{Fore.BLUE}AI: {Style.RESET_ALL}", end="")
            multi_language_team.print_response(query, stream=True)
            print(f"\n{Fore.CYAN}----------------------------------------{Style.RESET_ALL}")
            
            # Ask if user wants to continue to next example
            if language != examples[-1][0]:  # If not the last example
                cont = input(f"\n{Fore.YELLOW}Press Enter to continue to next example (or 'q' to quit): {Style.RESET_ALL}")
                if cont.lower() == 'q':
                    break
    
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
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    parser.add_argument('--demo', action='store_true', help='Run demonstration with examples')
    
    args = parser.parse_args()
    
    # Set debug mode from command line argument
    if args.debug:
        os.environ['DEBUG_MODE'] = 'true'
        # Re-import to update DEBUG_MODE value
        from multi_lang_agent.config import DEBUG_MODE
    
    # Run appropriate mode
    if args.demo:
        run_demo()
    elif args.query:
        single_query(args.query)
    else:
        interactive_chat()


if __name__ == "__main__":
    main() 