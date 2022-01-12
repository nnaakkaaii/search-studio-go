package presenter_interface

import (
	"search/pkg/entity/entity/studio"
	"search/pkg/entity/entity/studios"
)

type PresenterInterface interface {
	StudioSearch(response studio.Response) ([]byte, error)
	StudiosSearch(response studios.Response) ([]byte, error)
}
