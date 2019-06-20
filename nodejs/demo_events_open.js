var fs = require('fs');

var readStream = fs.createReadStream('./demofile.txt');

readStream.on('open', function(){
	console.log('The file is open');
})