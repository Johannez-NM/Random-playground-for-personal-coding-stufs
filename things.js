var express = require('express');
var router = express.Router();

//router.get('/', function(req, res) {res.send('GET route on things.'); });
//router.post('/', function(req, res) {res.send('POST route on things.'); });
router.get('/:id', function(req, res) {res.send('The pp length you specified is ' + req.params.id); });

module.exports = router;