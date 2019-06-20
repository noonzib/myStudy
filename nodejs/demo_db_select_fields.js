var mysql = require("mysql");

var con = mysql.createConnection({
	host: "localhost",
	user: "root",
	password: "",
	database: "nodedb"
});

con.connect(function(err){
	if(err) throw err;
	con.query("SELECT name, address FROM customers", function(err,result,fields){
		if(err) throw err;
		console.log(fields);
		console.log(fields[1].name);
	});
});