var mysql = require('mysql');

var con = mysql.createConnection({
	host: "localhost",
	user: "root",
	password: "",
	database: "nodedb"
});

con.connect(function(err){
	if(err) throw err;
	var sql = "UPDATE customers SET address = 'Seoul 123' WHERE address = 'Valley 345'";
	con.query(sql, function(err, result){
		if(err) throw err;
		console.log(result.affectedRows + " record(s) updated");
	});	
});