package controller

import (
	"github.com/labstack/echo"
	"log"
	"net/http"
)

func handle(ctx echo.Context, err error) error {
	log.Print("API:", err.Error())
	switch {
	default:
		return ctx.JSON(http.StatusInternalServerError, errResp{"unknown server error"})
	}
}

type errResp struct {
	Message string `json:"message"`
}
