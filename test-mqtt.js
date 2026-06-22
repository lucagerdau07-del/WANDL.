const mqtt = require('mqtt');
const urls = [
    'wss://test.mosquitto.org:8081/mqtt',
    'wss://mqtt.eclipseprojects.io:443/mqtt',
    'wss://broker.hivemq.com:8884/mqtt',
    'wss://broker.emqx.io:8084/mqtt'
];

urls.forEach(url => {
    const client = mqtt.connect(url, { connectTimeout: 3000 });
    client.on('connect', () => {
        console.log('Connected successfully to:', url);
        client.end();
    });
    client.on('error', (err) => {
        console.log('Error on:', url, err.message);
    });
});
