package graph

// This file will be automatically regenerated based on the schema, any resolver implementations
// will be copied through when generating and any unknown code will be moved to the end.

import (
	"context"
	"graphql/graph/generated"
	"graphql/graph/model"
)

func (r *queryResolver) GetStudioByID(ctx context.Context, studioID int) (*model.Studio, error) {
	return r.getStudioByID(ctx, studioID)
}

func (r *queryResolver) GetStudios(ctx context.Context, studioName *string) ([]*model.Studio, error) {
	return r.getStudios(ctx, studioName)
}

func (r *studioResolver) StudioFacilities(ctx context.Context, obj *model.Studio) ([]*model.StudioFacility, error) {
	return r.studioFacilities(ctx, obj)
}

func (r *studioResolver) StudioAmenities(ctx context.Context, obj *model.Studio) ([]*model.StudioAmenity, error) {
	return r.studioAmenities(ctx, obj)
}

func (r *studioResolver) StudioPayments(ctx context.Context, obj *model.Studio) ([]*model.StudioPayment, error) {
	return r.studioPayments(ctx, obj)
}

func (r *studioResolver) StudioReservations(ctx context.Context, obj *model.Studio) ([]*model.StudioReservation, error) {
	return r.studioReservations(ctx, obj)
}

func (r *studioResolver) StudioImages(ctx context.Context, obj *model.Studio) ([]*model.StudioImage, error) {
	return r.studioImages(ctx, obj)
}

func (r *studioResolver) StudioStationRailwayExits(ctx context.Context, obj *model.Studio) ([]*model.StudioStationRailwayExit, error) {
	return r.studioStationRailwayExit(ctx, obj)
}

// Query returns generated.QueryResolver implementation.
func (r *Resolver) Query() generated.QueryResolver { return &queryResolver{r} }

// Studio returns generated.StudioResolver implementation.
func (r *Resolver) Studio() generated.StudioResolver { return &studioResolver{r} }

type queryResolver struct{ *Resolver }
type studioResolver struct{ *Resolver }
