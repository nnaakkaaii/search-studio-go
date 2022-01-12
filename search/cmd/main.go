package main

import (
	"search/pkg/controller/controller"
	"search/pkg/database/database"
	"search/pkg/presenter/presenter"
	"search/pkg/repository/repository"
	"search/pkg/server/server"
	"search/pkg/usecase/usecase"
)

const (
	Port       = 8001
	DBUser     = "root"
	DBPassword = "postgres"
	DBPort     = "5432"
	DBHost     = "db"
	DBName     = "studio"
)

func main() {
	// database
	d := database.NewSqlHandler(database.Input{
		DBUser: DBUser,
		DBPass: DBPassword,
		DBHost: DBHost,
		DBPort: DBPort,
		DBName: DBName,
	})
	// repository
	r := new(repository.Repository)
	r.SqlHandler = d
	// presenter
	p := new(presenter.Presenter)
	// usecase
	u := new(usecase.Usecase)
	u.Repository = r
	// controller
	c := new(controller.Controller)
	c.Presenter = p
	c.Usecase = u
	// server
	s := server.NewServer(c)
	s.Start(Port)
}
