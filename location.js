const twilio = require('twilio');
const axios = require('axios');

const client = new twilio(
  process.env.TWILIO_ACCOUNT_SID,
  process.env.TWILIO_AUTH_TOKEN
);

// Your Google Maps Geocoding API key
const apiKey = 'YOUR_API_KEY';

const handleMessage = async (message, sender) => {
  if (message.toLowerCase() === 'location') {
    // Ask the user to share their location
    const message = await client.messages.create({
      from: 'whatsapp:+14155238886',
      to: sender,
      body: 'Please share your location',
      persistentAction: ['geo:default,userpref'],
    });

    console.log(message.sid);
  }
};

const handleLocation = async (message, sender) => {
  const { latitude, longitude } = message.geo;

  try {
    // Use the Google Maps Geocoding API to get the address
    const response = await axios.get(
      `https://maps.googleapis.com/maps/api/geocode/json?latlng=${latitude},${longitude}&key=${apiKey}`
    );

    const address = response.data.results[0].formatted_address;

    // Send the address back to the user
    const message = await client.messages.create({
      from: 'whatsapp:+14155238886',
      to: sender,
      body: `Your location is: ${address}`,
    });

    console.log(message.sid);
  } catch (error) {
    console.log(error);
  }
};

const app = async (req, res) => {
  const { Body, From } = req.body;

  if (req.body.EventType === 'MESSAGE' && Body) {
    const message = Body.trim().toLowerCase();

    if (message === 'location') {
      handleMessage(message, From);
    }
  }

  if (req.body.EventType === 'MESSAGE' && req.body.Geo) {
    handleLocation(req.body, From);
  }

  res.send();
};

module.exports = app;
