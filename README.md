# Multi-Language Agent

A multi-language AI assistant system built with Agno and Gemini 2.0 Flash. This project creates a team of AI agents that can respond in different languages (English, Japanese, German, and Chinese).

## Installation

### Using UV (Recommended)

[UV](https://github.com/astral-sh/uv) is a fast Python package installer and resolver. To install and set up the project with UV:

1. Install UV if you don't have it already:

   ```bash
   pip install uv
   ```

2. Clone this repository:

   ```bash
   git clone <repository-url>
   cd multi_lang_agent
   ```

3. Create a virtual environment with UV:

   ```bash
   uv venv
   ```

4. Activate the virtual environment:

   ```bash
   # On Windows
   .venv\Scripts\activate

   # On macOS/Linux
   source .venv/bin/activate
   ```

5. Install the package and dependencies:

   ```bash
   uv pip install -e .
   ```

6. Create a `.env` file in the project root with your Google API key:

   ```
   GOOGLE_API_KEY=your_api_key_here

   # Optional: Enable debug mode
   DEBUG_MODE=false
   ```

   You can get an API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

### Alternative Installation (Pip)

If you prefer using pip:

1. Clone this repository
2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv

   # On Windows
   .venv\Scripts\activate

   # On macOS/Linux
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -e .
   ```

## Usage

### Interactive Chat CLI

For an interactive chat experience with the multi-language agent:

```bash
# With activated environment
multi-lang-chat

# Or directly with UV (no activation needed)
uv run multi_lang_agent/cli.py
```

## Supported Languages

- English
- Japanese
- Chinese
- German

The system will respond in English when asked in unsupported languages.

## Features

- Automatically detects the language of user input
- Routes queries to the appropriate language agent
- Responds in the language of the query when supported
- Graceful handling of unsupported languages
- Debug mode to understand the routing process
