# Amazon Price Alert

This script monitors the price of a specific product on Amazon and sends an email notification if the price drops below a certain threshold.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- Access to an SMTP server for email notifications

## Setup

1. **Environment Variables**: Set the following environment variables in your system:
   - `ADRS`: SMTP server address
   - `EMAIL`: Email address to send notifications from
   - `PASS`: Email account password
   - `URL`: URL of the Amazon product page
   - `USER_AGENT`: User agent string for making the request
   - `LANG`: Accept-Language header for the request

2. **Install Dependencies**: Run the following command to install the required libraries:
   ```bash
   pip install requests beautifulsoup4
   
# Usage

1. **Set the Threshold**: Adjust the `BUY` variable in the code to specify the price threshold. The script will alert you if the price drops below this value.

2. **Run the Script**: Execute the script to start monitoring the price. If the price falls below the specified threshold, you will receive an email notification with the product details and the URL.

## How It Works

1. The script fetches the product page from Amazon using the provided URL and headers.
2. It parses the page to find the current price and product title.
3. If the price is lower than the specified threshold (`BUY`), it sends an email alert.

