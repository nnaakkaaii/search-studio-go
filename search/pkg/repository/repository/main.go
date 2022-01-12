package repository

import (
	"search/pkg/repository/database_interface"
	"search/pkg/usecase/repository_interface"
)

type Repository struct {
	database_interface.SqlHandler
}

var _ repository_interface.RepositoryInterface = (*Repository)(nil)
