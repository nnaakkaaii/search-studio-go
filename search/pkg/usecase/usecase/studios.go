package usecase

import "search/pkg/entity/entity/studios"

func (u *Usecase) StudiosSearch(q studios.Query) (studios.Response, error) {
	return u.Repository.StudiosRead(q)
}
