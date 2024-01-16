# Chatbot-GPT3
Solution for Namma Yatri Open Mobility Challenge

# Personalized WhatsApp Chatbot using Python, Twilio, Flask, Ngrok, and AWS

## Overview

This project demonstrates the development of a personalized one-to-one WhatsApp chatbot using Python, Twilio, Flask, Ngrok, and AWS. The chatbot is designed to interact with users on the WhatsApp platform, providing a seamless and personalized conversational experience. The integration of the OpenAI API enhances the chatbot's capabilities, allowing it to understand and respond to diverse user needs.

## Features

- **WhatsApp Integration**: Utilizes Twilio's WhatsApp API to enable communication with users on the popular messaging platform.

- **Flask Web Server**: Implements a Flask web server to handle incoming messages, process requests, and orchestrate interactions with the chatbot.

- **Ngrok for Local Development**: Uses Ngrok to expose the local Flask server to the internet, enabling Twilio to communicate with the chatbot during development.

- **OpenAI API Integration**: Enhances the chatbot's natural language processing capabilities by integrating the OpenAI API. This allows the chatbot to understand and generate responses based on a wide range of user inputs.

- **AWS Deployment**: Hosts the chatbot on AWS to ensure scalability, reliability, and accessibility.

## Dependencies

- Python 3.x
- Flask
- Twilio
- Ngrok
- OpenAI API key
- AWS account (for deployment)

Install the required packages using the following command:

```bash
pip install Flask twilio openai
```

## Configuration

1. Obtain Twilio credentials and set up a WhatsApp sandbox.

2. Obtain an OpenAI API key from the OpenAI platform.

3. Configure the necessary credentials in the `config.py` file:

```python
# Twilio configuration
TWILIO_ACCOUNT_SID = 'your_twilio_account_sid'
TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'

# OpenAI API configuration
OPENAI_API_KEY = 'your_openai_api_key'
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/Aashutosh-922/Chatbot-GPT3.git```

2. Navigate to the project directory:

```bash
cd Chatbot-GPT3
```

3. Run the Flask server:

```bash
python bot1.py
```

4. Expose the local server using Ngrok:

```bash
ngrok http 5000
```

5. Configure the Twilio WhatsApp sandbox with the Ngrok URL.

6. Start chatting with the personalized WhatsApp chatbot!

## Deployment on AWS

Follow AWS documentation to deploy the chatbot on an AWS instance, ensuring proper security configurations and scalability.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to Twilio, Flask, Ngrok, OpenAI, and AWS for providing the tools and services that make this project possible.
- Thanks to the open-source community for valuable contributions and insights.

Feel free to contribute to this project by submitting issues or pull requests. Your feedback and enhancements are highly appreciated!
