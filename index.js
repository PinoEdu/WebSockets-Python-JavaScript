// Crea una nueva conexión.
const socket = new WebSocket('ws://localhost:5000');

// Abre la conexión
socket.addEventListener('open', function (event) {
});

// Escucha por mensajes
socket.addEventListener('message', function (event) {
    console.log('Message from server', event.data);
});