package controller

import (
	"search/pkg/controller/controller_interface"
	"search/pkg/controller/presenter_interface"
	"search/pkg/usecase/usecase_interface"
)

type Controller struct {
	Usecase   usecase_interface.UsecaseInterface
	Presenter presenter_interface.PresenterInterface
}

var _ controller_interface.ControllerInterface = (*Controller)(nil)
