# Flight Deals Seeker

This is a Python program that checks flight prices from Kiwi Flight Search API (https://partners.kiwi.com/) and sends a notification via SMS using Twilio API (https://www.twilio.com/docs/sms). The source of the cities/airports to search is stored in Google Sheets and accessed via Sheety (https://sheety.co/). This was a Capstone Project from the course "100 Days of Code: The Complete Python Pro Bootcamp for 2023" (https://www.udemy.com/course/100-days-of-code/), which I recommend so far.

Next I would like to add a user interface using a web app to adjust the settings of the program, so you can change the origin city, destinations, days, layovers, etc.

## API keys and environment variables

As you can see in the code, the API keys are stored in the OS environment variables. So, you would have to export these variables in your deployment environment, so the scripts can access this data.

You would need to add the following keys:

-   TEQUILA_API_KEY (this is the Kiwi Flight API)
-   SHEETY_API_ENDPOINT (It includes the Google Sheet ID)
-   TWILIO_SID
-   TWILIO_AUTH_TOKEN
-   TWILIO_MSG_SERVICE_SID
-   TWILIO_VERIFIED_NUMBER

You can protect the Sheety access with two types of authorization. Please take a look at the docs: https://sheety.co/docs

Any feedback is welcomed. Thanks for reading.
