let express = require('express');
let router = express.Router();


router.get('/', function(req, res, next) {

  res.render('statics', { title: 'Global Inflation Figure'} );
});

module.exports = router;
