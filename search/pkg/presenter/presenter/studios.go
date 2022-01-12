package presenter

import (
	"search/pkg/entity/entity/studios"
)

func (p *Presenter) StudiosSearch(response studios.Response) ([]byte, error) {
	return Jsonify(response)
}
