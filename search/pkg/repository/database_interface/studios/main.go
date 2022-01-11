package studios

import (
	"search/pkg/entity/entity/studios"
)

type DatabaseInterface interface {
	Read(query studios.Query) (studios.Response, error)
}
