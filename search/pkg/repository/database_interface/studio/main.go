package studio

import (
	"search/pkg/entity/entity/studio"
)

type DatabaseInterface interface {
	Read(query studio.Query) (studio.Response, error)
}
