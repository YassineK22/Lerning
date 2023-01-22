
const os = require('os');

var totalMemory = os.totalmem();
var freeMemory = os.freemem();

console.log('Total  Memory: '+ totalMemory);
//Template string : console.log(`Total Memory: ${totalMemory}`)

//Using Template string
console.log(`Free Memory: ${freeMemory}`)