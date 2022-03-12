const http = require('http')
const server = http.createServer()
// export default io;
const socketio = require('socket.io')

const io = socketio(server, {
    cors : {
        origin: 'http:/127.0.0.1:8000/chats',
        methods: ["GET", "POST"]
    }
})

io.on('connection', socket=> {
    console.log('connected')
    console.log('socket.id')
})


server.listen(8000, ()=> console.log('listening on port 8000'))