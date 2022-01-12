package database

import (
	"database/sql"
	"fmt"
	_ "github.com/lib/pq"
	"search/pkg/repository/database_interface"
)

type Input struct {
	DBUser string
	DBPass string
	DBHost string
	DBPort string
	DBName string
}

type SqlHandler struct {
	Conn *sql.DB
}

var _ database_interface.SqlHandler = (*SqlHandler)(nil)

type SqlRows struct {
	Rows *sql.Rows
}

var _ database_interface.Rows = (*SqlRows)(nil)

func NewSqlHandler(i Input) database_interface.SqlHandler {
	ds := fmt.Sprintf("host=%s port=%s user=%s password=%s dbname=%s sslmode=disable", i.DBHost, i.DBPort, i.DBUser, i.DBPass, i.DBName)
	conn, err := sql.Open("postgres", ds)
	if err != nil {
		panic(err.Error())
	}
	sqlHandler := new(SqlHandler)
	sqlHandler.Conn = conn
	return sqlHandler
}

func (handler *SqlHandler) ErrNoRows() error {
	return sql.ErrNoRows
}

func (handler *SqlHandler) Query(statement string, args ...interface{}) (database_interface.Rows, error) {
	rows, err := handler.Conn.Query(statement, args...)
	if err != nil {
		return new(SqlRows), err
	}
	row := new(SqlRows)
	row.Rows = rows
	return rows, nil
}

func (r SqlRows) Scan(dest ...interface{}) error {
	return r.Rows.Scan(dest...)
}

func (r SqlRows) Next() bool {
	return r.Rows.Next()
}

func (r SqlRows) Close() error {
	return r.Rows.Close()
}

type SqlResult struct {
	Result sql.Result
}

var _ database_interface.Result = (*SqlResult)(nil)

func (handler *SqlHandler) Execute(statement string, args ...interface{}) (database_interface.Result, error) {
	res := SqlResult{}
	stmt, err := handler.Conn.Prepare(statement)
	if err != nil {
		return res, err
	}
	defer stmt.Close()
	exe, err := stmt.Exec(args...)
	if err != nil {
		return res, err
	}
	res.Result = exe
	return res, nil
}

func (r SqlResult) LastInsertId() (int64, error) {
	return r.Result.LastInsertId()
}

func (r SqlResult) RowsAffected() (int64, error) {
	return r.Result.RowsAffected()
}
