
export class WSocket {
    constructor(url, onMessage) {
        this.socket = null;
        this.url = url;
        this.onMessage = onMessage;
        this.connect();
    }

    connect() {
        this.socket = connect(this.url);

        this.socket.onmessage = (event) => {
            if (this.onMessage) {
                this.onMessage(event);
            }
        };

        this.socket.onclose = (event) => {
            if (event.wasClean) {
                console.log('Clean connection end')
            } else {
                console.log('Connection broken')
            }
        };

        this.socket.onerror = (error) => {
            console.error(error);
        }
    }

    send(message) {
        this.socket.send(message);
    }
}

function connect(url) {
    try {
        return new WebSocket('ws://' + url);
    }
    catch (err) {
        return new WebSocket('wss://' + url);
    }
}