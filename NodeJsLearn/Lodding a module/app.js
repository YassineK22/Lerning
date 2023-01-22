//function of node JS
//function (exports, require, module, __filename, __dirname)
console.log(__filename);
console.log(__dirname);
const logger = require('./logger');

logger('message');