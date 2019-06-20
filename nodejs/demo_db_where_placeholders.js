var mysql = require('mysql');

var con = mysql.createConnection({
	host: "localhost",
	user: "root",
	password: "",
	database: "nodedb"
});

con.connect(function (err){
	if(err) throw err;
	var name = 'noonzib';
	var adr = 'seoul';
	var sql = 'SELECT * FROM customers WHERE name = ? OR address = ?';
	con.query(sql, [name, adr], function (err, result){
		if(err) throw err;
		console.log(result);
	})
})