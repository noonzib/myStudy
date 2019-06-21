var mysql = require('mysql');

var con = mysql.createConnection({
	host: "localhost",
	user: "root",
	password: "",
	database: "nodedb"
});

con.connect(function(err){
	if(err) throw err;
	sql = "SELECT * FROM customers LIMIT 5";
	con.query(sql, function(err, result){
		if(err) throw err;
		console.log(result);
	})
})