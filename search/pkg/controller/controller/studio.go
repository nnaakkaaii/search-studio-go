package controller

import (
	"github.com/labstack/echo"
	"net/http"
	"search/pkg/entity/entity/studio"
	"strconv"
)

func (c *Controller) StudioSearch(ctx echo.Context) error {
	txtStudioID := ctx.QueryParam("studio_id")
	studioID, err := strconv.Atoi(txtStudioID)
	if err != nil {
		return handle(ctx, err)
	}

	q := studio.Query{StudioID: studioID}
	res, err := c.Usecase.StudioSearch(q)
	if err != nil {
		return handle(ctx, err)
	}

	b, err := c.Presenter.StudioSearch(res)

	return ctx.JSONBlob(http.StatusOK, b)
}
