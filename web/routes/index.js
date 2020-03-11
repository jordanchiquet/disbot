var express = require('express');
var router = express.Router();

var mysql = require('mysql')

var pool		= mysql.createPool({
	connectionLimit : 10,
	host			: '18.216.39.250',
	user			: 'dbuser',
	password		: 'e4miqtng',
	database		: 'renarddb'
});


function queryQuotes (sql, callback) {
	pool.getConnection(function(err, connection) {
		connection.query(sql, function(err, result) {
			connection.release();
			if (err) throw err;
			callback(result);
		});
	});
}


/* GET home page. */
router.get('/', function(req, res, next) {
  var sql = "SELECT id, quote, user, timestamp FROM renarddb.quotes";
	queryQuotes(sql, function(result) {
    console.log(result[0])
    res.render('index', { data: result });
	});
});



router.get('/search', function(req, res){
	var sql = "";
	var idOn = false;
	var userOn = false;
	var quoteOn = false;
	var id = req.query.paramID;
	var user = req.query.paramUser;
	var quote = req.query.paramQuote;
	var input = req.query.paramInput;
	var runQuery = "";
	var defaultQuery = "SELECT id, quote, user, timestamp FROM renarddb.quotes";
	if (id == "on") {
		sql = "id like " + input;
		idOn = true;
	}

	if (user == "on") {
		if(sql != "") {
			sql = sql + " || user like '%" + input + "%'";
		} else {
			sql = " user like '%" + input + "%'";
		}
		userOn = true;
	}

	if (quote == "on") {
		if(sql != "") {
			sql = sql + " || quote like '%" + input + "%'";
		} else {
			sql = " quote like '%" + input + "%'";
		}
		quoteOn = true;
	}

	if (sql != "") {
		runQuery = defaultQuery + " where " + sql;
	} else {
		runQuery = defaultQuery;
	}
	queryQuotes(runQuery, function(result) {
	console.log(input + "\n" + runQuery)
	res.render('index', { data: result, idOn: idOn, userOn: userOn, quoteOn: quoteOn});
	});
})

module.exports = router;
