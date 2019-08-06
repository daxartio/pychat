import React from 'react';

export default class MessageInput extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            message: ''
        };
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleChange = this.handleChange.bind(this);
    }

    handleSubmit(event) {
        event.preventDefault();
        const message = this.state.message.trim();
        if (message && this.props.onMessage) {
            this.props.onMessage(message);
        }
        this.setState({ message: '' });
    }

    handleChange(event) {
        this.setState({ message: event.target.value });
    }

    render() {
        return (
            <form className='MessageInput' onSubmit={this.handleSubmit}>
                <label>
                    <input type="text" value={this.state.message} onChange={this.handleChange} placeholder={
                        this.props.placeholder || 'Enter Text...'
                    } />
                </label>
                <label>
                    <input type="submit" />
                </label>
            </form>
        );
    }
}