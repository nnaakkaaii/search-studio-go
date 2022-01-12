package controller_interface

import "github.com/labstack/echo"

type ControllerInterface interface {
	StudioSearch(ctx echo.Context) error
	StudiosSearch(ctx echo.Context) error
}
