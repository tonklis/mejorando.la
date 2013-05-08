var express = require('express'),
    swig = require('swig'),
    cons = require('consolidate');

var app = express();

swig.init({
  cache: false
});

// View engine
app.engine('.html', cons.swig);
app.set('view engine', 'html');
app.set('views', './views');

// Static files
app.use(express.static('./public'));

// Post
app.use(express.bodyParser());
app.use(express.cookieParser());

var mensajes = [],
    ress = [];


app.get("/", function (req, res){
  res.render('home', {
    mensajes: mensajes
  });
});

app.post("/mensajes/new", function(req, res){
  mensajes.push(req.body.mensaje);

  ress.forEach(function(res){
    res.send(mensajes);
  });
  res.send('Tu mensaje es ' + req.body.mensaje);
});

app.get("/mensajes/list", function(req, res){
  ress.push(res);
  //res.send(mensajes+'<script>setTimeout(function(){window.location.reload()}, 1000);</script>');
});

app.listen(3000);
console.log("Application working");
