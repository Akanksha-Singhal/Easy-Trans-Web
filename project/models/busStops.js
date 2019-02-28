var con = require('./db.js');

// var Stop = function(stop)
// {   
//     this.stopCode = stop.stopCode;
//     this.name = stop.name;
//     this.longitude = stop.longitude;
//     this.latitude = stop.latitude;
// }

var Stop ={
    getAllStops: function(callback)             
        {
            return con.query("Select * from stops", callback);
        },
    getStopById:function(id,callback)
        {
            return con.query("select * from stops where StopCode = ?",[id],callback);
        },
    }
module.exports= Stop;