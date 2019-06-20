var mysql = require("mysql");

var con = mysql.createConnection({
	host: "localhost",
	user: "root",
	password: "",
	database: "nodedb"
});

con.connect(function(err){
	if(err) throw err;
	console.log("Connected!");
	var sql = "ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY";
	con.query(sql, function(err, result){
		if(err) throw err;
		console.log("Table altered");
	});
});