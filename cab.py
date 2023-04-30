import os
from twilio.rest import Client
from flask import Flask, request
from datetime import datetime, timedelta



# Download the helper library from https://www.twilio.com/docs/python/install
# import os
# from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACba5d5a26ac9f2edea8a24c69679e28c8'
auth_token = '855a08a6f3d4b4ef5506185587039106'
twilio_number = "+16073576098"
whatsapp_number = "+919604617753"
client = Client(account_sid, auth_token)

conversation = client.conversations \
                     .v1 \
                     .conversations \
                     .create(friendly_name='Cab')

print(conversation.sid)


# Twilio account information
# account_sid = "AC983074407c063b5aa3b704624c457c36"
# auth_token = "c2adf944ff3e81597a27d89dd58c751f"
#twilio_number = "+14155238886"
#whatsapp_number = "+919370708497"
# client = Client(account_sid, auth_token)

# Flask application setup
app = Flask(__name__)

# Dictionary to hold cab booking information
cab_bookings = {}

# Function to send a message via WhatsApp
def send_message(whatsapp_number, message):
    message = client.messages.create(
        body=message,
        from_='whatsapp:' + twilio_number,
        to='whatsapp:' + whatsapp_number
    )
    return message.sid

# Function to check if a booking already exists for a phone number
def is_booking_exists(whatsapp_number):
    if whatsapp_number in cab_bookings:
        return True
    return False

# Function to create a new booking
def create_booking(whatsapp_number, pickup_location, drop_location, pickup_time):
    cab_bookings[whatsapp_number] = {
        "pickup_location": pickup_location,
        "drop_location": drop_location,
        "pickup_time": pickup_time
    }

# Function to get the booking details
def get_booking_details(whatsapp_number):
    booking_details = cab_bookings[whatsapp_number]
    return booking_details

# Function to cancel a booking
def cancel_booking(whatsapp_number):
    if whatsapp_number in cab_bookings:
        del cab_bookings[whatsapp_number]

# Route to handle incoming messages
@app.route("/incoming-message", methods=["POST"])
def handle_incoming_message():
    incoming_message = request.values.get("Body", "")
    whatsapp_number = request.values.get("From").split(":")[1]
    response_message = ""

    if incoming_message.lower() == "book cab":
        if is_booking_exists(whatsapp_number):
            response_message = "You already have a cab booking. To cancel your booking, type 'Cancel booking'"
        else:
            response_message = "Please provide your pickup location, drop location and pickup time in the following format: 'pickup_location, drop_location, pickup_time (DD-MM-YYYY HH:MM)'"
    elif incoming_message.lower() == "cancel booking":
        if is_booking_exists(whatsapp_number):
            cancel_booking(whatsapp_number)
            response_message = "Your booking has been cancelled."
        else:
            response_message = "You don't have any active booking to cancel."
    elif "," in incoming_message:
        if is_booking_exists(whatsapp_number):
            response_message = "You already have a cab booking. To cancel your booking, type 'Cancel booking'"
        else:
            booking_info = incoming_message.split(",")
            pickup_location = booking_info[0].strip()
            drop_location = booking_info[1].strip()
            pickup_time = datetime.strptime(booking_info[2].strip(), "%d-%m-%Y %H:%M")

            if pickup_time < datetime.now() + timedelta(hours=1):
                response_message = "Please provide a pickup time at least 1 hour from now."
            else:
                create_booking(whatsapp_number, pickup_location, drop_location, pickup_time)
                booking_details = get_booking_details(whatsapp_number)
                response_message = f"Your cab has been booked from {booking_details['pickup_location']} to {booking_details['drop_location']} at {booking_details['pickup_time'].strftime('%d-%m-%Y %H:%M')}."

    send_message(whatsapp_number, response_message)
