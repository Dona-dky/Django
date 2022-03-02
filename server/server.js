const http = require('http')
const server = http.createServer()

const socketio = require('socket.io')

const io = socketio(server, {
    cors : {
        origin: 'http:/127.0.0.1:8000',
        methods: ["GET", "POST"]
    }
})