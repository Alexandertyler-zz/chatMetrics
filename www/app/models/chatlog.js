var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var ChatlogSchema = new Schema({
  user : String,
  channel : String,
  message : String
});

module.exports = mongoose.model('Chatlog', ChatlogSchema);
