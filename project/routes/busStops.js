var con = require('../models/db.js');
var express = require("express");
var router = express.Router({mergeParams: true});
var Stop = require("../models/busStops.js");
router.get("/", function(req, res){

    con.query("Select * from stops", function (err, result) {
        if (err) throw err;
        console.log("Stops Database accessed ");
        //console.log(result);
    });

});


router.get('/:id',function(req,res,next)
{
    if(req.params.id)
    {
        Stop.getStopById(req.params.id,function(err,rows){
        
            if(err)
            { res.json(err);}
            else
            {   //console.log(rows[0].StopCode);
                res.render("showbusStop",{rows: rows[0] })
                //res.json(rows); 
            }
        });
    }
    else{
    
        Stop.getAllStops(function(err,rows){
    
        if(err)
        { res.json(err); }
        else
        { res.json(rows); }
    
        });
    }
});

module.exports = router;