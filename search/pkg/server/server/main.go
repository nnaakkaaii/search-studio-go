package server

import (
	"fmt"
	"github.com/labstack/echo"
	"log"
	"net/http"
	"search/pkg/controller/controller_interface"
	"search/pkg/server/router"
	"search/pkg/server/server_interface"
)

type Server struct {
	e          *echo.Echo
	controller controller_interface.ControllerInterface
}

var _ server_interface.ServerInterface = (*Server)(nil)

func NewServer(controller controller_interface.ControllerInterface) server_interface.ServerInterface {
	server := new(Server)
	server.e = echo.New()
	server.controller = controller

	for _, r := range router.HandleRoutes(controller) {
		ms := make([]echo.MiddlewareFunc, 0)
		switch r.Method {
		case http.MethodGet:
			server.e.GET(r.Path, r.Handler, ms...)
		case http.MethodPost:
			server.e.POST(r.Path, r.Handler, ms...)
		case http.MethodPut:
			server.e.PUT(r.Path, r.Handler, ms...)
		case http.MethodDelete:
			server.e.DELETE(r.Path, r.Handler, ms...)
		default:
			panic("unknown route")
		}
	}
	return server
}

func (s *Server) Start(port int) {
	log.Fatal(s.e.Start(fmt.Sprintf(":%d", port)))
}
