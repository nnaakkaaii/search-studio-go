package models

// Code generated by xo. DO NOT EDIT.

import (
	"context"
	"time"
)

// StudioFacilities represents a row from 'public.studio_facilities'.
type StudioFacilities struct {
	StudioFacilityID       int       `json:"studio_facility_id"`        // studio_facility_id
	FacilityID             int       `json:"facility_id"`               // facility_id
	FacilityName           string    `json:"facility_name"`             // facility_name
	StudioFacilityCount    int       `json:"studio_facility_count"`     // studio_facility_count
	StudioFacilityPrice    float64   `json:"studio_facility_price"`     // studio_facility_price
	StudioFacilityUnitHour float64   `json:"studio_facility_unit_hour"` // studio_facility_unit_hour
	CreatedAt              time.Time `json:"created_at"`                // created_at
	UpdatedAt              time.Time `json:"updated_at"`                // updated_at
}

// StudioFacilitiesByStudioID runs a custom query, returning results as StudioFacilities.
func StudioFacilitiesByStudioID(ctx context.Context, db DB, studioID int) ([]*StudioFacilities, error) {
	// query
	const sqlstr = `SELECT sf.studio_facility_id, ` +
		`sf.facility_id, ` +
		`f.facility_name, ` +
		`sf.studio_facility_count, ` +
		`sf.studio_facility_price, ` +
		`sf.studio_facility_unit_hour, ` +
		`sf.created_at, ` +
		`sf.updated_at ` +
		`FROM studio_facility AS sf ` +
		`LEFT JOIN facility AS f ON sf.facility_id = f.facility_id ` +
		`WHERE sf.studio_id = $1 ` +
		`AND sf.is_deleted IS FALSE;`
	// run
	logf(sqlstr, studioID)
	rows, err := db.QueryContext(ctx, sqlstr, studioID)
	if err != nil {
		return nil, logerror(err)
	}
	defer rows.Close()
	// load results
	var res []*StudioFacilities
	for rows.Next() {
		var sf StudioFacilities
		// scan
		if err := rows.Scan(&sf.StudioFacilityID, &sf.FacilityID, &sf.FacilityName, &sf.StudioFacilityCount, &sf.StudioFacilityPrice, &sf.StudioFacilityUnitHour, &sf.CreatedAt, &sf.UpdatedAt); err != nil {
			return nil, logerror(err)
		}
		res = append(res, &sf)
	}
	if err := rows.Err(); err != nil {
		return nil, logerror(err)
	}
	return res, nil
}