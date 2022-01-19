package models

import "context"

// StudioAmenitiesByStudioIDByQueries runs a custom query, returning results as StudioAmenities.
func StudioAmenitiesByStudioIDByQueries(ctx context.Context, db DB, studioID int, amenityIds []int) ([]*StudioAmenities, error) {
	// query
	var sqlstr = `SELECT ` +
		`sa.studio_amenity_id, ` +
		`sa.amenity_id, ` +
		`a.amenity_name, ` +
		`sa.studio_amenity_count, ` +
		`sa.studio_amenity_price, ` +
		`sa.studio_amenity_unit_hour, ` +
		`sa.created_at, ` +
		`sa.updated_at ` +
		`FROM ` +
		`studio_amenity AS sa ` +
		`LEFT JOIN ` +
		`amenity AS a ` +
		`ON  sa.amenity_id = a.amenity_id ` +
		`WHERE ` +
		`sa.studio_id = $1 ` +
		`AND sa.is_deleted IS FALSE ` +
		ints2Query("sa.amenity_id", amenityIds) +
		`;`
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

