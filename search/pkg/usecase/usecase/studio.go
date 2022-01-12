package usecase

import "search/pkg/entity/entity/studio"

func (u *Usecase) StudioSearch(q studio.Query) (studio.Response, error) {
	return u.Repository.StudioRead(q)
}
