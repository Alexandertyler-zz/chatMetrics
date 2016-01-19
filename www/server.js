//server
var express = require('express');
var app = express();
var router = express.Router();

//used for logging requests to the console
var morgan = require('morgan');
var body_parser = require('body-parser');

//============== Mongodb Load =============
//Connect to the DB and load our schema
var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost:27017/chatMetrics');
var Chatlog = require('./app/models/chatlog');

app.use(morgan('dev'));
//Serve all the static files
app.use(express.static(__dirname + '/static'));

//=============== API ==============
router.use(function(req, res, next) {
  console.log('Something is happening');
  next();
});

router.get('/', function(req, res) {
  res.json({ message: 'Top level api' })
});

router.route('/chatlog')
  .post(function(req, res) {
    var chatlog = new Chatlog(); //a new instance of a chatlog from the schema
    chatlog.name = req.body.name;

    chatlog.save(function(err) {
      if (err) {
        res.send(err);
      }
      res.json({ message: 'Chatlog created' });
    });
  });

//======= Register routes =======
app.use('/api', router)



//============== Serve Angular Index =============
app.get('/', function(req, res) {
  res.sendfile('index.html');
});

app.listen(8080);
console.log('App is listening on port 8080');
