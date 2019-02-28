var express = require("express");
var router = express.Router({mergeParams:true});
var con = require('../models/db.js');
var Stop = require('./busStops.js');

// Route
router.get("/easytrans", function(req, res){
    con.query("Select * from stops", function (err, result) {
        if (err) throw err;
        console.log("stops Database extracted");
        //console.log(result);

        res.render("home.ejs", {Stops: result});
      });
});

router.get("/easytrans/:source/:dest", function(req, res){

    var data; var found= false;
    for(var i = 1; i<=14; i++)
    {   for(var j = 1; j <=14; j++)
        {
            con.query("Select * from stopsonroute where `"+i+"` ="+req.params.source+" and  `"+j+"` ="+req.params.dest, function (err, result) {
                if (err) throw err;
                console.log("stopsonroute Database extracted");
                console.log(result);
                if(result.length>0)
                { console.log("found");
                    found = true;
                }      
                //res.render("home.ejs", {Stops: result});
              });
              if(found == true)
                {
                    break;
                }          
        }   
        if(found == true)
            {
                break;
            }     
    }
    
});

router.post("/easytrans",function(req, res){
    var source = req.body.source; var  sourceCode, destinationCode;
    var destination = req.body.destination;

    con.query("Select * from stops where Name = \""+source+"\" ", function (err, Source_res) {
        if (err) throw err;
        console.log("stops Database extracted");
        sourceCode = Source_res[0].StopCode;
        console.log(sourceCode);

        con.query("Select * from stops where Name = \""+destination+"\" ", function (err, Dest_res) {
            if (err) throw err;
            console.log("stops Database extracted");
            destinationCode = Dest_res[0].StopCode;
            console.log(destinationCode);
    
            res.redirect("/easytrans/"+sourceCode+"/"+destinationCode);
          });
      });   
});

module.exports = router;