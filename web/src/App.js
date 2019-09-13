import React from 'react';
import './App.css';
import { Chat, Message, MessageBody, MessageBlockInput, MessageInput, Messages } from './chat'
import { WSocket } from './socket';

export default class App extends React.Component {
    constructor() {
        super();
        this.state = {
            messages: [],
            name: 'guest_' + getRandomInt(1000, 9999)
        };
        this.onMessage = this.onMessage.bind(this);

        this.socket = new WSocket(window.location.host + (window.location.port ? ':' + window.location.port : '') + '/ws/main_room', (event) => {
            try {
                const message = JSON.parse(event.data);
                this.state.messages.push(message);
                this.setState(this.state);
                this.messages.scrollBottom();
            } catch (e) {
                console.log(e);
            }
        });
    }

    command(text) {
        if (text.startsWith('/name')) {
            const args = text.split(' ').filter(v => v !== '');
            this.setState({ name: args.slice(1).join(' ') });
            return true;
        }
        return false;
    }

    onMessage(text) {
        if (!this.command(text)) {

            this.socket.send(JSON.stringify({
                text: text,
                name: this.state.name
            }));
        }
    }

    render() {
        return (
            <div className="App">
                <Chat>
                    <Messages ref={instance => { this.messages = instance; }}>
                        <Message>
                            <MessageBody>
                                Helper> Enter command for manage <br />
                                /name Your Name
                            </MessageBody>
                        </Message>
                        {this.state.messages.map((message, index) => {
                            return (
                                <Message key={index}>
                                    <MessageBody>
                                        <span className='message-name'>{message.name}></span> {message.text} <span className='message-time'>{formatDate(message.created_at)}</span>
                                    </MessageBody>
                                </Message>
                            )
                        })}
                    </Messages>
                    <MessageBlockInput>
                        <div className='user-name'>{this.state.name}></div>
                        <MessageInput onMessage={this.onMessage} placeholder='Enter Command...' />
                    </MessageBlockInput>
                </Chat>
            </div>
        );
    }
}

function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function formatDate(str) {
    const date = new Date(str);
    return date.toLocaleString();
}