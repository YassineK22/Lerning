const EventEmitter = require('events');

var url = "http://logIntoUU.io/log";

class Logger extends EventEmitter{
    log(message) {
        // Send an HTTP request
        console.log(message);
    
        // Raise an event and adding an event arguments + this a a object --> {}
        this.emit('messageLogged', {id: 1, url: 'http://'});    
    }
}

module.exports = Logger;
/*module.exports.log = log; then when i use in app i need to fix
logger('message'); to logger.log('message') */