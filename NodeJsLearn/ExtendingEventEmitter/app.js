
//load the lagger module and call the log function
const Logger = require('./logger');
const logger = new Logger();

// Register a listener
logger.on('messageLogged', (eventArg) => { //This is a arrow function --> (var) => {}
    console.log('Listener called', eventArg);
});

logger.log('message')