var url = "http://logIntoUU.io/log";

function log(message) {
    // Send an HTTP request
    console.log(message);
}

module.exports = log;
/*module.exports.log = log; then when i use in app i need to fix
logger('message'); to logger.log('message') */