
const EventEmitter = require('events');
const emitter = new EventEmitter();

// Register a listener
emitter.on('messageLogged', (eventArg) => { //This is a arrow function --> (var) => {}
    console.log('Listener called', eventArg);
});

// Raise an event and adding an event arguments this a a object --> {}
emitter.emit('messageLogged', {id: 1, url: 'http://'});

//Raise: logging (data:message) (Exercice)