package router

import (
	"github.com/labstack/echo"
	"net/http"
	"search/pkg/controller/controller_interface"
)

// Route は method (リクエストメソッド), path, handler (実行するHandler)の情報を含む
type Route struct {
	Method  string
	Path    string
	Handler echo.HandlerFunc
}

func HandleRoutes(controller controller_interface.ControllerInterface) []Route {
	return []Route{
		{
			Method:  http.MethodGet,
			Path:    "/api/search/studio",
			Handler: controller.StudioSearch,
		},
		{
			Method:  http.MethodGet,
			Path:    "/api/search/studios",
			Handler: controller.StudiosSearch,
		},
	}
}
