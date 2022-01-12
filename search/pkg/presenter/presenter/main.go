package presenter

import "search/pkg/controller/presenter_interface"

type Presenter struct {
}

var _ presenter_interface.PresenterInterface = (*Presenter)(nil)
