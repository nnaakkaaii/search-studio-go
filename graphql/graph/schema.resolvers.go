package graph

// This file will be automatically regenerated based on the schema, any resolver implementations
// will be copied through when generating and any unknown code will be moved to the end.

import (
	"context"
	"graphql/graph/generated"
	"graphql/graph/model"
	"time"
)

func (r *queryResolver) GetStudioByID(ctx context.Context, studioID int) (*model.Studio, error) {
	return r.getStudioByID(ctx, studioID)
}

func (r *queryResolver) GetStudios(ctx context.Context, studioNames []string, prefectureIds []int, cityIds []int) ([]*model.Studio, error) {
	return r.getStudios(ctx, studioNames, prefectureIds, cityIds)
}

func (r *roomResolver) RoomSlots(ctx context.Context, obj *model.Room) ([]*model.RoomSlot, error) {
	return r.roomSlots(ctx, obj)
}

func (r *roomResolver) GetRoomSlots(ctx context.Context, obj *model.Room, dates []string, timeBegin *time.Time, timeEnd *time.Time, minSlotPrice *float64, minRemainSlotCount *int) ([]*model.RoomSlot, error) {
	return r.getRoomSlots(ctx, obj, dates, timeBegin, timeEnd, minSlotPrice, minRemainSlotCount)
}

func (r *roomResolver) RoomFloorMaterials(ctx context.Context, obj *model.Room) ([]*model.RoomFloorMaterial, error) {
	return r.roomFloorMaterials(ctx, obj)
}

func (r *roomResolver) GetRoomFloorMaterials(ctx context.Context, obj *model.Room, floorMaterialNames []string) ([]*model.RoomFloorMaterial, error) {
	return r.getRoomFloorMaterials(ctx, obj, floorMaterialNames)
}

func (r *roomResolver) RoomFacilities(ctx context.Context, obj *model.Room) ([]*model.RoomFacility, error) {
	return r.roomFacilities(ctx, obj)
}

func (r *roomResolver) GetRoomFacilities(ctx context.Context, obj *model.Room, facilityNames []string) ([]*model.RoomFacility, error) {
	return r.getRoomFacilities(ctx, obj, facilityNames)
}

func (r *roomResolver) RoomImages(ctx context.Context, obj *model.Room) ([]*model.RoomImage, error) {
	return r.roomImages(ctx, obj)
}

func (r *studioResolver) StudioFacilities(ctx context.Context, obj *model.Studio) ([]*model.StudioFacility, error) {
	return r.studioFacilities(ctx, obj)
}

func (r *studioResolver) GetStudioFacilities(ctx context.Context, obj *model.Studio, facilityIds []int) ([]*model.StudioFacility, error) {
	return r.getStudioFacilities(ctx, obj, facilityIds)
}

func (r *studioResolver) StudioAmenities(ctx context.Context, obj *model.Studio) ([]*model.StudioAmenity, error) {
	return r.studioAmenities(ctx, obj)
}

func (r *studioResolver) GetStudioAmenities(ctx context.Context, obj *model.Studio, amenityIds []int) ([]*model.StudioAmenity, error) {
	return r.getStudioAmenities(ctx, obj, amenityIds)
}

func (r *studioResolver) StudioPayments(ctx context.Context, obj *model.Studio) ([]*model.StudioPayment, error) {
	return r.studioPayments(ctx, obj)
}

func (r *studioResolver) GetStudioPayments(ctx context.Context, obj *model.Studio, paymentIds []int) ([]*model.StudioPayment, error) {
	return r.getStudioPayments(ctx, obj, paymentIds)
}

func (r *studioResolver) StudioReservations(ctx context.Context, obj *model.Studio) ([]*model.StudioReservation, error) {
	return r.studioReservations(ctx, obj)
}

func (r *studioResolver) GetStudioReservations(ctx context.Context, obj *model.Studio, reservationIds []int) ([]*model.StudioReservation, error) {
	return r.getStudioReservations(ctx, obj, reservationIds)
}

func (r *studioResolver) StudioImages(ctx context.Context, obj *model.Studio) ([]*model.StudioImage, error) {
	return r.studioImages(ctx, obj)
}

func (r *studioResolver) GetStudioStationRailwayExits(ctx context.Context, obj *model.Studio, stationIds []int, railwayIds []int, maxMinutesFromStation *int) ([]*model.StudioStationRailwayExit, error) {
	return r.getStudioStationRailwayExits(ctx, obj, stationIds, railwayIds, maxMinutesFromStation)
}

func (r *studioResolver) StudioStationRailwayExits(ctx context.Context, obj *model.Studio) ([]*model.StudioStationRailwayExit, error) {
	return r.studioStationRailwayExits(ctx, obj)
}

func (r *studioResolver) Rooms(ctx context.Context, obj *model.Studio) ([]*model.Room, error) {
	return r.rooms(ctx, obj)
}

func (r *studioResolver) GetRooms(ctx context.Context, obj *model.Studio, roomNames []string, minReservePeople *int, maxReservePeople *int, minFloorArea *float64) ([]*model.Room, error) {
	return r.getRooms(ctx, obj, roomNames, minReservePeople, maxReservePeople, minFloorArea)
}

// Query returns generated.QueryResolver implementation.
func (r *Resolver) Query() generated.QueryResolver { return &queryResolver{r} }

// Room returns generated.RoomResolver implementation.
func (r *Resolver) Room() generated.RoomResolver { return &roomResolver{r} }

// Studio returns generated.StudioResolver implementation.
func (r *Resolver) Studio() generated.StudioResolver { return &studioResolver{r} }

type queryResolver struct{ *Resolver }
type roomResolver struct{ *Resolver }
type studioResolver struct{ *Resolver }
