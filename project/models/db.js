'user strict';

var mysql = require('mysql');

//local mysql db connection
// var con = mysql.createConnection({
//     host     : 'localhost',
//     user     : 'root',
//     password : 'root',
//     database : 'easytrans',
//     port : 3306
// });

var con = mysql.createConnection({
    host     : 'easytransdb.mysql.database.azure.com',
    user     : 'dbroot@easytransdb',
    password : 'E@sytrans',
    database : 'easytrans',
    port : 3306
});

con.connect(function(err) {
    if (err) throw err;
    console.log("Connected!");
});

module.exports = con;