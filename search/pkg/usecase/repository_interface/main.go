package repository_interface

import (
	"search/pkg/entity/entity/studio"
	"search/pkg/entity/entity/studios"
)

type RepositoryInterface interface {
	StudioRead(studio.Query) (studio.Response, error)
	StudiosRead(studios.Query) (studios.Response, error)
}
