package models

// Code generated by xo. DO NOT EDIT.

import (
	"context"
	"time"
)

// StudioAmenities represents a row from 'public.studio_amenities'.
type StudioAmenities struct {
	StudioAmenityID       int       `json:"studio_amenity_id"`        // studio_amenity_id
	AmenityID             int       `json:"amenity_id"`               // amenity_id
	AmenityName           string    `json:"amenity_name"`             // amenity_name
	StudioAmenityCount    int       `json:"studio_amenity_count"`     // studio_amenity_count
	StudioAmenityPrice    float64   `json:"studio_amenity_price"`     // studio_amenity_price
	StudioAmenityUnitHour float64   `json:"studio_amenity_unit_hour"` // studio_amenity_unit_hour
	CreatedAt             time.Time `json:"created_at"`               // created_at
	UpdatedAt             time.Time `json:"updated_at"`               // updated_at
}

// StudioAmenitiesByStudioID runs a custom query, returning results as StudioAmenities.
func StudioAmenitiesByStudioID(ctx context.Context, db DB, studioID int) ([]*StudioAmenities, error) {
	// query
	const sqlstr = `SELECT sa.studio_amenity_id, ` +
		`sa.amenity_id, ` +
		`a.amenity_name, ` +
		`sa.studio_amenity_count, ` +
		`sa.studio_amenity_price, ` +
		`sa.studio_amenity_unit_hour, ` +
		`sa.created_at, ` +
		`sa.updated_at ` +
		`FROM studio_amenity AS sa ` +
		`LEFT JOIN amenity AS a ON sa.amenity_id = a.amenity_id ` +
		`WHERE sa.studio_id = $1 ` +
		`AND sa.is_deleted IS FALSE;`
	// run
	logf(sqlstr, studioID)
	rows, err := db.QueryContext(ctx, sqlstr, studioID)
	if err != nil {
		return nil, logerror(err)
	}
	defer rows.Close()
	// load results
	var res []*StudioAmenities
	for rows.Next() {
		var sa StudioAmenities
		// scan
		if err := rows.Scan(&sa.StudioAmenityID, &sa.AmenityID, &sa.AmenityName, &sa.StudioAmenityCount, &sa.StudioAmenityPrice, &sa.StudioAmenityUnitHour, &sa.CreatedAt, &sa.UpdatedAt); err != nil {
			return nil, logerror(err)
		}
		res = append(res, &sa)
	}
	if err := rows.Err(); err != nil {
		return nil, logerror(err)
	}
	return res, nil
}