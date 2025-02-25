# Emojifier Discord Bot

**Emojifier** is a Discord bot that scrapes Reddit to create a word-to-emoji mapping based on user posts. It uses the `$pasta` command to emojify text in Discord, making your messages fun and dynamic.

## Features

- Scrapes Reddit efficiently, generating a `emoji_map.json` with word-to-emoji mappings.
- Processes Reddit queries up to 5x faster than Reddit's post query rate limit using multithreaded queries.
- Converts user input into emoji-filled messages with `$pasta`.
- Customizable configuration for scraping and emoji mappings.

## Installation

1. Clone the repo:

    ```bash
    git clone https://github.com/yourusername/emojifier-discord-bot.git
    cd emojifier-discord-bot
    ```

3. Create a `.env` file with your Discord and Reddit API credentials:

    ```
    DISCORD_TOKEN=your_discord_token
    REDDIT_CLIENT_ID=your_reddit_client_id
    REDDIT_SECRET=your_reddit_secret
    REDDIT_USER_AGENT=your_user_agent
    ```

4. Run the bot:

    ```bash
    python Discord.py
    ```

5. If you wish to regenerate the emoji mappings or scan different posts, run:

    ```bash
    python Discord.py
    ```

## Usage

1. The bot automatically scrapes Reddit, builds the emoji map, and saves it in `db.json`.
2. Use `$pasta <text>` in Discord to get emoji-filled text based on Reddit data.

    Example:

    ```
    $pasta I love pizza!
    ```

    Response:

    ```
    🍕 I love pizza! 🍕
    ```

