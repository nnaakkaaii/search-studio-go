package controller

import (
	"github.com/labstack/echo"
	"net/http"
	"search/pkg/entity/entity/studios"
)

func (c *Controller) StudiosSearch(ctx echo.Context) error {
	q := studios.Query{}
	res, err := c.Usecase.StudiosSearch(q)
	if err != nil {
		return handle(ctx, err)
	}

	b, err := c.Presenter.StudiosSearch(res)

	return ctx.JSONBlob(http.StatusOK, b)
}
