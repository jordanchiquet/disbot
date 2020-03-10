var express = require('express');
var router = express.Router();

var mysql = require('mysql')

var pool		= mysql.createPool({
	connectionLimit : 10,
	host			: 'iosteampi.local',
	user			: 'dbuser',
	password		: 'truceiosdb',
	database		: 'darwinDb'
});

function queryWhiteListApps (sql, callback) {
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
  var sql = "SELECT id, OS, name, CASE WHEN iOSBundle =  'none' THEN 'N/A' WHEN iOSBundle is NULL THEN 'N/A' ELSE iOSBundle END AS 'iOSBundle', CASE WHEN packageName =  'none' THEN 'N/A' WHEN packageName is NULL THEN 'N/A' WHEN packageName = '' THEN 'N/A' ELSE packageName END AS 'packageName', CASE WHEN availableOnAbm =  '0' THEN 'NO' WHEN availableOnAbm is NULL THEN 'NO' ELSE 'YES' END AS 'availableOnAbm' FROM darwinDb.whitelistTable";
	queryWhiteListApps(sql, function(result) {
    console.log(result[0])
    res.render('index', { data: result });
	});
});


router.get('/search', function(req, res){
	var sql = ""
	var name = req.query.paramAppName;
	var os = req.query.paramOS;
	var abm = req.query.paramAvailableAbm;
	var input = req.query.paramInput;
	var runQuery = "";
	var defaultQuery = "SELECT id, OS, name, CASE WHEN iOSBundle =  'none' THEN 'N/A' WHEN iOSBundle is NULL THEN 'N/A' ELSE iOSBundle END AS 'iOSBundle', CASE WHEN packageName =  'none' THEN 'N/A' WHEN packageName is NULL THEN 'N/A' WHEN packageName = '' THEN 'N/A' ELSE packageName END AS 'packageName', CASE WHEN availableOnAbm =  '0' THEN 'NO' WHEN availableOnAbm is NULL THEN 'NO' ELSE 'YES' END AS 'availableOnAbm' FROM darwinDb.whitelistTable";
	if (name == "on") {
		sql = "name like '%" + input + "%'";
		nameChecked = true;
	}

	if (os == "on") {
		if(sql != "") {
			sql = sql + " || OS like '%" + input + "%'";
		} else {
			sql = " OS like '%" + input + "%'";
		}
		osChecked = true;
	}

	if (abm == "on") {
		if(sql != "") {
			if (input.toLowerCase().includes("yes") == true ){
				sql = sql + " || availableOnABM = '1'";
			} else {
				sql = sql + " || (availableOnABM = '0' || availableOnABM IS NULL)"
			}
		} else {
			if (input.toLowerCase().includes("yes") == true ){
				sql = " availableOnABM = '1'";
			} else {
				sql = " (availableOnABM = '0' || availableOnABM IS NULL)"
			}
		}
		abmChecked = true;
		
	}

	if (sql != "") {
		runQuery = defaultQuery + " where " + sql;
	} else {
		runQuery = defaultQuery;
	}
	queryWhiteListApps(runQuery, function(result) {
	console.log(input + "\n" + runQuery)
	res.render('index', { data: result });
	});
})


module.exports = router;
