package usecase_interface

import (
	"search/pkg/entity/entity/studio"
	"search/pkg/entity/entity/studios"
)

type UsecaseInterface interface {
	StudioSearch(studio.Query) (studio.Response, error)
	StudiosSearch(studios.Query) (studios.Response, error)
}
