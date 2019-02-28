var express = require("express");
var app = express();
var mysql = require('mysql');
var bodyParser = require("body-parser");

// app.get("/easytrans", function(req, res){
//     res.render("home.ejs");
// });

// var con = mysql.createConnection({
//   host: 'localhost',
//   user: "root",
//   password: "root",
//   port: 3306
// });

var con = require('./models/db.js');

//requiring Routes
var indexRoutes = require("./routes/index");
var busStopRoutes  = require("./routes/busStops");

app.use(bodyParser.urlencoded({extended: true}));
app.set("view engine", "ejs");
app.use(express.static("public"));

app.use("/",indexRoutes);
app.use("/busStop", busStopRoutes);

// con.connect(function(err) {
//   if (err) throw err;
//   console.log("Connected from app.js!");
  // con.query("CREATE DATABASE mydb2", function (err, result) {
  //   if (err) throw err;
  //   console.log("Database created");
  // });
// });

app.listen(3000, process.env.IP, function(){
    console.log("Server started");
});