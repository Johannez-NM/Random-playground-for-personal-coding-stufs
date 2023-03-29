var express = require('Express');
var app = express();
var things = require('./things.js');

function restart() {
    app.removeListener(3000)
}

app.use('/things', things);

app.listen(3000);
console.log("Server started at 'http://127.0.0.1:3000'.");
