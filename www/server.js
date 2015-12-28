//server
var express = require('express');
var app = express();
//mongodb handler
var mongoose = require('mongoose');
//used for logging requests to the console
var morgan = require('morgan');

//mongoose.connect('mongodb://');

app.use(express.static(__dirname + '/public/static'));
app.use(morgan('dev'));

app.get('/*', function(req, res) {
  res.sendfile('index.html');
});

app.listen(8080);
console.log('App is listening on port 8080');
