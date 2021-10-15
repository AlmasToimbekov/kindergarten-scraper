## Description

This is a scraper of a website in Kazakhstan for finding free spots in kindergarten. Once the place is found the Telegram notification is sent to the telegram bot.

## Settings

1. Install project dependencies `pip install -r ./requirements.txt`
1. Create a Telegram bot using [this](https://medium.com/@robertbracco1/how-to-write-a-telegram-bot-to-send-messages-with-python-bcdf45d0a580) article and go through the necessary steps for setting the `telegram-send configure` command;
1. Install the [chromedriver](https://chromedriver.chromium.org/);
1. Set the [get_data.py](./get_data.py):`CHROME_DRIVER_PATH` variable pointing to that chromedriver location path;
1. Fill the [get_data.py](./get_data.py):`kindergartens` array with ones you need to monitor;
1. Set the schedule in [main.py](./main.py) (line 21);
1. Run the `source venv/bin/activate` from the terminal you want to use for launching the script;
1. Launch the script using `python main.py` command.