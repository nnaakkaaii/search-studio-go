package presenter

import (
	"search/pkg/entity/entity/studio"
)

func (p *Presenter) StudioSearch(response studio.Response) ([]byte, error) {
	return Jsonify(response)
}
