var express = require('express');
var router = express.Router();
const spawn = require('child_process').spawn;

router.get('/', function(req, res, next) {
  try{
    let dataToSend;
    const python = spawn('python3', ['public/python/main.py']);
    python.stdout.on('data', (data) => {
      dataToSend = data.toString();
      console.log(dataToSend);
      res.render('index', {
        title: 'Global Inflation Figure',
        dataInfo : dataToSend
      });
    })
    
  } catch(e){
    console.error(e);
  }
});

module.exports = router;
