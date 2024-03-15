# Gemini Pro

This project demonstrates how to create a LineBot with memory capabilities, allowing for continuous and context-aware conversations. The bot leverages several platforms for its development and deployment.

## Platforms Used

- **Line Developers**: To create and configure the LineBot.
- **Gemini Pro**: To enable conversational AI capabilities.
- **Google Cloud Functions**: To deploy the Python code and generate a webhook for the LineBot.
- **Firebase**: To establish a real-time database for storing conversation history.

## LineBot Creation

### Step 1: Create a Bot on Line Developers

### Step 2: Configure Bot Basic Information

- **Channel type**: Set to Messaging API (mandatory).
- **Provider**: Use an existing one or create a new one if you haven't used it before.
- **Other options**: Fill in the details as required.
- **Bot profile image**: Upload a custom image.
- **Privacy policy URL, Terms of use URL**: These can be left blank.

### Step 3: Obtain Bot's Channel Secret and Channel Access Token

After creating the bot, find the Channel secret on the Basic Setting page and the Channel access token on the Messaging API page. These will be used in the code.

**Note**: If you issue or reissue these credentials, remember to update them in your code.

### Step 4: Finalize Bot Setup

Set aside the bot for now. Once the program is deployed, paste the URL back into the Webhook URL field on the Messaging API page.

## Gemini Pro API

Refer to the official Gemini Pro website and tutorials for guidance. Remember to save your API Keys securely as they can only be copied at the time of creation.

## Firebase

### Step 1: Get Started

Click on 'Get Started'.

### Step 2: Create a Project

Click on 'Add Project' and make sure to enable Google Analytics.

### Step 3: Enter Realtime Database

After entering Realtime Database, create a new database in locked mode and then modify it.

Once you see a URL like `https://XXX.firebaseio.com/`, that's the URL you'll use in the program to set the data storage location.

### Step 4: Change Rules

In the 'Rules' section, change `false` to `true` to allow external writes.

## Google Cloud Functions

### Step 0: Introduction to Google Cloud

Google Cloud offers a suite of cloud computing services, including computing, data storage, data analytics, and machine learning.

### Step 1: Get Started

Click on 'Console' or 'Start a Free Trial' on the website.

### Step 2: Create a Project in Cloud Functions

Find Cloud Functions in the menu or under the 'Serverless' category.

### Step 3: Create a Function

Set the environment to the first generation and the region to `asia-east1` (Taiwan). Set the trigger to HTTP and allow unauthenticated invocations.

Add four runtime environment variables:

- `GEMINI_API_KEY`: Your Gemini Pro secret key.
- `LINE_BOT_TOKEN`: Your Line Developers Channel access token.
- `LINE_BOT_SECRET`: Your Line Developers Channel secret.
- `FIREBASE_URL`: Your Firebase URL.

### Step 4: Deploy

After setting up the function, deploy it. Once deployed, you'll find a 'Trigger URL' that you'll paste back into your LineBot.

## Result

You can check the conversation history stored in Firebase.

With this setup, you have successfully created a LineBot with memory capabilities, allowing for more engaging and contextually aware conversations.
