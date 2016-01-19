var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var ChatlogSchema = new Schema({
  name : String
});

module.exports = mongoose.model('Chatlog', ChatlogSchema);
