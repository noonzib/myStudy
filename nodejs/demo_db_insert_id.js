var mysql = require("mysql");

var con = mysql.createConnection({
	host: "localhost",
	user: "root",
	password: "",
	database: "nodedb"
});

con.connect(function(err){
	if(err) throw err;
	var sql = "INSERT INTO customers(name, address) VALUES ('eric','seoul')";
	con.query(sql,function(err, result){
		if(err) throw err;
		console.log("1 record inserted, ID: "+result.insertId);
	});
});