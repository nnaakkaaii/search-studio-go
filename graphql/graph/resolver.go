package graph

import (
	"context"
	"database/sql"
	"errors"
	_ "github.com/lib/pq"
	"graphql/graph/model"
	"graphql/models"
	"time"
)

// This file will not be regenerated automatically.
//
// It serves as dependency injection for your app, add any dependencies you require here.

type Resolver struct{}

var db *sql.DB

const dateFormat = "2006-01-02"
const datetimeFormat = "2006-01-02 15:04:05"
const timeFormat = "15:04:05"

func init() {
	conn, err := sql.Open("postgres", "host=db port=5432 user=root password=postgres dbname=studio sslmode=disable")
	if err != nil {
		panic(err)
	}
	db = conn
}

func toDt(d time.Time) string {
	return d.Format(datetimeFormat)
}

func toD(d time.Time) string {
	return d.Format(dateFormat)
}

func toT(t time.Time) string {
	return t.Format(timeFormat)
}

func toPtrDt(d *time.Time) *string {
	if d == nil {
		return nil
	}
	tmp := toDt(*d)
	return &tmp
}

func (r *Resolver) getStudioByID(ctx context.Context, studioID int) (*model.Studio, error) {
	s, err := models.StudiosByStudioID(ctx, db, studioID)
	if err != nil {
		return nil, err
	}
	if len(s) == 0 {
		return nil, errors.New("not found")
	}
	f := s[0]

	return &model.Studio{
		StudioID:       f.StudioID,
		StudioName:     f.StudioName,
		Introduction:   f.Introduction,
		Precaution:     f.Precaution,
		HomepageURL:    f.HomepageURL,
		Contact:        f.Contact,
		AddressID:      f.AddressID,
		AddressName:    f.AddressName,
		CityID:         f.CityID,
		CityName:       f.CityName,
		PrefectureID:   f.PrefectureID,
		PrefectureName: f.PrefectureName,
		RentByMinHours: f.RentByMinHours,
		CanFreeCancel:  f.CanFreeCancel,
		CreatedAt:      toDt(f.CreatedAt),
		UpdatedAt:      toPtrDt(f.UpdatedAt),
	}, nil
}

func (r *Resolver) getStudios(ctx context.Context, studioNames []string, prefectureIds []int, cityIds []int) ([]*model.Studio, error) {
	s, err := models.GetStudiosByQueries(ctx, db, studioNames, prefectureIds, cityIds)
	if err != nil {
		return nil, err
	}

	resp := make([]*model.Studio, 0, len(s))
	for _, v := range s {
		resp = append(resp, &model.Studio{
			StudioID:       v.StudioID,
			StudioName:     v.StudioName,
			Introduction:   v.Introduction,
			Precaution:     v.Precaution,
			HomepageURL:    v.HomepageURL,
			Contact:        v.Contact,
			AddressID:      v.AddressID,
			AddressName:    v.AddressName,
			CityID:         v.CityID,
			CityName:       v.CityName,
			PrefectureID:   v.PrefectureID,
			PrefectureName: v.PrefectureName,
			RentByMinHours: v.RentByMinHours,
			CanFreeCancel:  v.CanFreeCancel,
			CreatedAt:      toDt(v.CreatedAt),
			UpdatedAt:      toPtrDt(v.UpdatedAt),
		})
	}
	return resp, nil
}

func (r *Resolver) roomSlots(ctx context.Context, obj *model.Room) ([]*model.RoomSlot, error) {
	roomID := obj.RoomID
	rs, err := models.RoomSlotsByRoomID(ctx, db, roomID)
	if err != nil {
		return nil, err
	}

	resp := make([]*model.RoomSlot, 0, len(rs))
	for _, v := range rs {
		resp = append(resp, &model.RoomSlot{
			RoomSlotID:      v.RoomSlotID,
			Date:            toD(v.Date),
			TimeBegin:       toT(v.TimeBegin),
			TimeEnd:         toT(v.TimeEnd),
			Workload:        v.Workload,
			SlotPrice:       v.SlotPrice,
			RemainSlotCount: v.RemainSlotCount,
			CreatedAt:       toDt(v.CreatedAt),
			UpdatedAt:       toPtrDt(v.UpdatedAt),
		})
	}
	return resp, nil
}

func (r *Resolver) getRoomSlots(ctx context.Context, obj *model.Room, dates []string, timeBegin *string, timeEnd *string, minSlotPrice *float64, minRemainSlotCount *int) ([]*model.RoomSlot, error) {
	roomID := obj.RoomID
	rs, err := models.RoomSlotsByRoomIDByQueries(ctx, db, roomID, dates, timeBegin, timeEnd, minSlotPrice, minRemainSlotCount)
	if err != nil {
		return nil, err
	}

	resp := make([]*model.RoomSlot, 0, len(rs))
	for _, v := range rs {
		resp = append(resp, &model.RoomSlot{
			RoomSlotID:      v.RoomSlotID,
			Date:            toD(v.Date),
			TimeBegin:       toT(v.TimeBegin),
			TimeEnd:         toT(v.TimeEnd),
			Workload:        v.Workload,
			SlotPrice:       v.SlotPrice,
			RemainSlotCount: v.RemainSlotCount,
			CreatedAt:       toDt(v.CreatedAt),
			UpdatedAt:       toPtrDt(v.UpdatedAt),
		})
	}
	return resp, nil
}

func (r *Resolver) roomFloorMaterials(ctx context.Context, obj *model.Room) ([]*model.RoomFloorMaterial, error) {
	roomID := obj.RoomID
	rfm, err := models.RoomFloorMaterialsByRoomID(ctx, db, roomID)
	if err != nil {
		return nil, err
	}

	resp := make([]*model.RoomFloorMaterial, 0, len(rfm))
	for _, v := range rfm {
		resp = append(resp, &model.RoomFloorMaterial{
			RoomFloorMaterialID: v.RoomFloorMaterialID,
			FloorMaterialID:     v.FloorMaterialID,
			FloorMaterialName:   v.FloorMaterialName,
			CreatedAt:           toDt(v.CreatedAt),
			UpdatedAt:           toPtrDt(v.UpdatedAt),
		})
	}
	return resp, nil
}

func (r *Resolver) getRoomFloorMaterials(ctx context.Context, obj *model.Room, floorMaterialNames []string) ([]*model.RoomFloorMaterial, error) {
	roomID := obj.RoomID
	rfm, err := models.RoomFloorMaterialsByRoomIDByQueries(ctx, db, roomID, floorMaterialNames)
	if err != nil {
		return nil, err
	}

	resp := make([]*model.RoomFloorMaterial, 0, len(rfm))
	for _, v := range rfm {
		resp = append(resp, &model.RoomFloorMaterial{
			RoomFloorMaterialID: v.RoomFloorMaterialID,
			FloorMaterialID:     v.FloorMaterialID,
			FloorMaterialName:   v.FloorMaterialName,
			CreatedAt:           toDt(v.CreatedAt),
			UpdatedAt:           toPtrDt(v.UpdatedAt),
		})
	}
	return resp, nil
}

func (r *Resolver) roomFacilities(ctx context.Context, obj *model.Room) ([]*model.RoomFacility, error) {
	roomID := obj.RoomID
	rf, err := models.RoomFacilitiesByRoomID(ctx, db, roomID)
	if err != nil {
		return nil, err
	}

	resp := make([]*model.RoomFacility, 0, len(rf))
	for _, v := range rf {
		resp = append(resp, &model.RoomFacility{
			RoomFacilityID:          v.RoomFacilityID,
			FacilityID:              v.FacilityID,
			FacilityName:            v.FacilityName,
			RoomFacilityDescription: v.RoomFacilityDescription,
			RoomFacilityCount:       v.RoomFacilityCount,
			RoomFacilityPrice:       v.RoomFacilityPrice,
			RoomFacilityUnitHour:    v.RoomFacilityUnitHour,
			CreatedAt:               toDt(v.CreatedAt),
			UpdatedAt:               toPtrDt(v.UpdatedAt),
		})
	}
	return resp, nil
}

func (r *Resolver) getRoomFacilities(ctx context.Context, obj *model.Room, facilityNames []string) ([]*model.RoomFacility, error) {
	roomID := obj.RoomID
	rf, err := models.RoomFacilitiesByRoomIDByQueries(ctx, db, roomID, facilityNames)
	if err != nil {
		return nil, err
	}

	resp := make([]*model.RoomFacility, 0, len(rf))
	for _, v := range rf {
		resp = append(resp, &model.RoomFacility{
			RoomFacilityID:          v.RoomFacilityID,
			FacilityID:              v.FacilityID,
			FacilityName:            v.FacilityName,
			RoomFacilityDescription: v.RoomFacilityDescription,
			RoomFacilityCount:       v.RoomFacilityCount,
			RoomFacilityPrice:       v.RoomFacilityPrice,
			RoomFacilityUnitHour:    v.RoomFacilityUnitHour,
			CreatedAt:               toDt(v.CreatedAt),
			UpdatedAt:               toPtrDt(v.UpdatedAt),
		})
	}
	return resp, nil
}

func (r *Resolver) roomImages(ctx context.Context, obj *model.Room) ([]*model.RoomImage, error) {
	roomID := obj.RoomID
	ri, err := models.RoomImagesByRoomID(ctx, db, roomID)
	if err != nil {
		return nil, err
	}

	resp := make([]*model.RoomImage, 0, len(ri))
	for _, v := range ri {
		resp = append(resp, &model.RoomImage{
			RoomImageID: v.RoomImageID,
			ImageID:     v.ImageID,
			ImageName:   v.ImageName,
			ImagePath:   v.ImagePath,
			CreatedAt:   toDt(v.CreatedAt),
			UpdatedAt:   toPtrDt(v.UpdatedAt),
			Description: v.Description,
		})
	}
	return resp, nil
}

func (r *Resolver) studioFacilities(ctx context.Context, obj *model.Studio) ([]*model.StudioFacility, error) {
	studioID := obj.StudioID
	sf, err := models.StudioFacilitiesByStudioID(ctx, db, studioID)
	if err != nil {
		return nil, err
	}

	resp := make([]*model.StudioFacility, 0, len(sf))
	for _, v := range sf {
		resp = append(resp, &model.StudioFacility{
			StudioFacilityID:          v.StudioFacilityID,
			FacilityID:                v.FacilityID,
			FacilityName:              v.FacilityName,
			StudioFacilityDescription: v.StudioFacilityDescription,
			StudioFacilityCount:       v.StudioFacilityCount,
			StudioFacilityPrice:       v.StudioFacilityPrice,
			StudioFacilityUnitHour:    v.StudioFacilityUnitHour,
			CreatedAt:                 toDt(v.CreatedAt),
			UpdatedAt:                 toPtrDt(v.UpdatedAt),
		})
	}
	return resp, nil
}

func (r *Resolver) getStudioFacilities(ctx context.Context, obj *model.Studio, facilityIds []int) ([]*model.StudioFacility, error) {
	studioID := obj.StudioID
	sf, err := models.StudioFacilitiesByStudioIDByQuery(ctx, db, studioID, facilityIds)
	if err != nil {
		return nil, err
	}

	resp := make([]*model.StudioFacility, 0, len(sf))
	for _, v := range sf {
		resp = append(resp, &model.StudioFacility{
			StudioFacilityID:          v.StudioFacilityID,
			FacilityID:                v.FacilityID,
			FacilityName:              v.FacilityName,
			StudioFacilityDescription: v.StudioFacilityDescription,
			StudioFacilityCount:       v.StudioFacilityCount,
			StudioFacilityPrice:       v.StudioFacilityPrice,
			StudioFacilityUnitHour:    v.StudioFacilityUnitHour,
			CreatedAt:                 toDt(v.CreatedAt),
			UpdatedAt:                 toPtrDt(v.UpdatedAt),
		})
	}
	return resp, nil
}

func (r *Resolver) studioAmenities(ctx context.Context, obj *model.Studio) ([]*model.StudioAmenity, error) {
	studioID := obj.StudioID
	sa, err := models.StudioAmenitiesByStudioID(ctx, db, studioID)
	if err != nil {
		return nil, err
	}

	resp := make([]*model.StudioAmenity, 0, len(sa))
	for _, v := range sa {
		resp = append(resp, &model.StudioAmenity{
			StudioAmenityID:          v.StudioAmenityID,
			AmenityID:                v.AmenityID,
			AmenityName:              v.AmenityName,
			StudioAmenityDescription: v.StudioAmenityDescription,
			StudioAmenityCount:       v.StudioAmenityCount,
			StudioAmenityPrice:       v.StudioAmenityPrice,
			StudioAmenityUnitHour:    v.StudioAmenityUnitHour,
			CreatedAt:                toDt(v.CreatedAt),
			UpdatedAt:                toPtrDt(v.UpdatedAt),
		})
	}
	return resp, nil
}

func (r *Resolver) getStudioAmenities(ctx context.Context, obj *model.Studio, amenityIds []int) ([]*model.StudioAmenity, error) {
	studioID := obj.StudioID
	sa, err := models.StudioAmenitiesByStudioIDByQueries(ctx, db, studioID, amenityIds)
	if err != nil {
		return nil, err
	}

	resp := make([]*model.StudioAmenity, 0, len(sa))
	for _, v := range sa {
		resp = append(resp, &model.StudioAmenity{
			StudioAmenityID:          v.StudioAmenityID,
			AmenityID:                v.AmenityID,
			AmenityName:              v.AmenityName,
			StudioAmenityDescription: v.StudioAmenityDescription,
			StudioAmenityCount:       v.StudioAmenityCount,
			StudioAmenityPrice:       v.StudioAmenityPrice,
			StudioAmenityUnitHour:    v.StudioAmenityUnitHour,
			CreatedAt:                toDt(v.CreatedAt),
			UpdatedAt:                toPtrDt(v.UpdatedAt),
		})
	}
	return resp, nil
}

func (r *Resolver) studioPayments(ctx context.Context, obj *model.Studio) ([]*model.StudioPayment, error) {
	studioID := obj.StudioID
	sp, err := models.StudioPaymentsByStudioID(ctx, db, studioID)
	if err != nil {
		return nil, err
	}

	resp := make([]*model.StudioPayment, 0, len(sp))
	for _, v := range sp {
		resp = append(resp, &model.StudioPayment{
			StudioPaymentID: v.StudioPaymentID,
			PaymentID:       v.PaymentID,
			PaymentName:     v.PaymentName,
			CreatedAt:       toDt(v.CreatedAt),
			UpdatedAt:       toPtrDt(v.UpdatedAt),
		})
	}
	return resp, nil
}

func (r *Resolver) getStudioPayments(ctx context.Context, obj *model.Studio, paymentIds []int) ([]*model.StudioPayment, error) {
	studioID := obj.StudioID
	sp, err := models.StudioPaymentsByStudioIDByQueries(ctx, db, studioID, paymentIds)
	if err != nil {
		return nil, err
	}

	resp := make([]*model.StudioPayment, 0, len(sp))
	for _, v := range sp {
		resp = append(resp, &model.StudioPayment{
			StudioPaymentID: v.StudioPaymentID,
			PaymentID:       v.PaymentID,
			PaymentName:     v.PaymentName,
			CreatedAt:       toDt(v.CreatedAt),
			UpdatedAt:       toPtrDt(v.UpdatedAt),
		})
	}
	return resp, nil
}

func (r *Resolver) studioReservations(ctx context.Context, obj *model.Studio) ([]*model.StudioReservation, error) {
	studioID := obj.StudioID
	sr, err := models.StudioReservationsByStudioID(ctx, db, studioID)
	if err != nil {
		return nil, err
	}

	resp := make([]*model.StudioReservation, 0, len(sr))
	for _, v := range sr {
		resp = append(resp, &model.StudioReservation{
			StudioReservationID: v.StudioReservationID,
			ReservationID:       v.ReservationID,
			ReservationName:     v.ReservationName,
			CreatedAt:           toDt(v.CreatedAt),
			UpdatedAt:           toPtrDt(v.UpdatedAt),
		})
	}
	return resp, nil
}

func (r *Resolver) getStudioReservations(ctx context.Context, obj *model.Studio, reservationIds []int) ([]*model.StudioReservation, error) {
	studioID := obj.StudioID
	sr, err := models.StudioReservationsByStudioIDByQueries(ctx, db, studioID, reservationIds)
	if err != nil {
		return nil, err
	}

	resp := make([]*model.StudioReservation, 0, len(sr))
	for _, v := range sr {
		resp = append(resp, &model.StudioReservation{
			StudioReservationID: v.StudioReservationID,
			ReservationID:       v.ReservationID,
			ReservationName:     v.ReservationName,
			CreatedAt:           toDt(v.CreatedAt),
			UpdatedAt:           toPtrDt(v.UpdatedAt),
		})
	}
	return resp, nil
}

func (r *Resolver) studioImages(ctx context.Context, obj *model.Studio) ([]*model.StudioImage, error) {
	studioID := obj.StudioID
	si, err := models.StudioImagesByStudioID(ctx, db, studioID)
	if err != nil {
		return nil, err
	}

	resp := make([]*model.StudioImage, 0, len(si))
	for _, v := range si {
		resp = append(resp, &model.StudioImage{
			StudioImageID: v.StudioImageID,
			ImageID:       v.ImageID,
			ImageName:     v.ImageName,
			ImagePath:     v.ImagePath,
			CreatedAt:     toDt(v.CreatedAt),
			UpdatedAt:     toPtrDt(v.UpdatedAt),
			Description:   v.Description,
		})
	}
	return resp, nil
}

func (r *Resolver) studioStationRailwayExits(ctx context.Context, obj *model.Studio) ([]*model.StudioStationRailwayExit, error) {
	studioID := obj.StudioID
	ssre, err := models.StudioStationRailwayExitsByStudioID(ctx, db, studioID)
	if err != nil {
		return nil, err
	}

	resp := make([]*model.StudioStationRailwayExit, 0, len(ssre))
	for _, v := range ssre {
		resp = append(resp, &model.StudioStationRailwayExit{
			StudioStationRailwayExitID: v.StudioStationRailwayExitID,
			StationRailwayExitID:       v.StationRailwayExitID,
			StationRailwayID:           v.StationRailwayID,
			StationID:                  v.StationID,
			StationName:                v.StationName,
			RailwayID:                  v.RailwayID,
			RailwayName:                v.RailwayName,
			ExitID:                     v.ExitID,
			ExitName:                   v.ExitName,
			MinutesFromStation:         v.MinutesFromStation,
			CreatedAt:                  toDt(v.CreatedAt),
			UpdatedAt:                  toPtrDt(v.UpdatedAt),
		})
	}
	return resp, nil
}

func (r *Resolver) getStudioStationRailwayExits(ctx context.Context, obj *model.Studio, stationIds []int, railwayIds []int, maxMinutesFromStation *int) ([]*model.StudioStationRailwayExit, error) {
	studioID := obj.StudioID
	ssre, err := models.StudioStationRailwayExitsByStudioIDByQueries(ctx, db, studioID, stationIds, railwayIds, maxMinutesFromStation)
	if err != nil {
		return nil, err
	}

	resp := make([]*model.StudioStationRailwayExit, 0, len(ssre))
	for _, v := range ssre {
		resp = append(resp, &model.StudioStationRailwayExit{
			StudioStationRailwayExitID: v.StudioStationRailwayExitID,
			StationRailwayExitID:       v.StationRailwayExitID,
			StationRailwayID:           v.StationRailwayID,
			StationID:                  v.StationID,
			StationName:                v.StationName,
			RailwayID:                  v.RailwayID,
			RailwayName:                v.RailwayName,
			ExitID:                     v.ExitID,
			ExitName:                   v.ExitName,
			MinutesFromStation:         v.MinutesFromStation,
			CreatedAt:                  toDt(v.CreatedAt),
			UpdatedAt:                  toPtrDt(v.UpdatedAt),
		})
	}
	return resp, nil
}

func (r *Resolver) rooms(ctx context.Context, obj *model.Studio) ([]*model.Room, error) {
	studioID := obj.StudioID
	rs, err := models.RoomsByStudioID(ctx, db, studioID)
	if err != nil {
		return nil, err
	}

	resp := make([]*model.Room, 0, len(rs))
	for _, v := range rs {
		resp = append(resp, &model.Room{
			RoomID:               v.RoomID,
			RoomName:             v.RoomName,
			ReservationURL:       v.ReservationURL,
			MinReservablePeople:  v.MinReservablePeople,
			MaxReservablePeople:  v.MaxReservablePeople,
			FloorArea:            v.FloorArea,
			CreatedAt:            toDt(v.CreatedAt),
			UpdatedAt:            toPtrDt(v.UpdatedAt),
		})
	}
	return resp, nil
}

func (r *Resolver) getRooms(ctx context.Context, obj *model.Studio, roomNames []string, minReservePeople *int, maxReservePeople *int, minFloorArea *float64) ([]*model.Room, error) {
	studioID := obj.StudioID
	rs, err := models.RoomsByStudioIDByQueries(ctx, db, studioID, roomNames, minReservePeople, maxReservePeople, minFloorArea)
	if err != nil {
		return nil, err
	}

	resp := make([]*model.Room, 0, len(rs))
	for _, v := range rs {
		resp = append(resp, &model.Room{
			RoomID:               v.RoomID,
			RoomName:             v.RoomName,
			ReservationURL:       v.ReservationURL,
			MinReservablePeople:  v.MinReservablePeople,
			MaxReservablePeople:  v.MaxReservablePeople,
			FloorArea:            v.FloorArea,
			CreatedAt:            toDt(v.CreatedAt),
			UpdatedAt:            toPtrDt(v.UpdatedAt),
		})
	}
	return resp, nil
}