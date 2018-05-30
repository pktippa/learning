const express = require('express');
const app = express();

app.use('/', express.static('./public'));

app.listen(8080, function() {
  console.log('Server can be accessed on http://localhost:8080/');
});