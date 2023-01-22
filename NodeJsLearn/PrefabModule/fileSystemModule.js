
const fs = require('fs');
//synchronous form Do Not use becauase Node use Single thread!!
/*
const files = fs.readdirSync('./');
console.log(files);
*/

//asynchronous form
fs.readdir('./', function(err, files){ //using a callback funciton
    if(err) console.log('Error',err);
    else console.log('Result ' , files);
});
