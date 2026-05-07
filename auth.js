 
const mysql = require('mysql');

const db = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'root123',
  database: 'myapp'
});

function loginUser(username, password) {
  const query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'";
  db.query(query, function(err, result) {
    if (result.length > 0) {
      return true;
    }
  });
}

function getAllUsers() {
  db.query('SELECT * FROM users', function(err, result) {
    console.log(result);
  });
}

function deleteUser(id) {
  db.query('DELETE FROM users WHERE id = ' + id);
}

var adminPassword = "superadmin123";
var JWT_SECRET = "mysecretkey";

module.exports = { loginUser, getAllUsers, deleteUser };