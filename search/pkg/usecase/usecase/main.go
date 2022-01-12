package usecase

import (
	"search/pkg/usecase/repository_interface"
	"search/pkg/usecase/usecase_interface"
)

type Usecase struct {
	Repository repository_interface.RepositoryInterface
}

var _ usecase_interface.UsecaseInterface = (*Usecase)(nil)
