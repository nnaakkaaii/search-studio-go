package models

import "context"

// StudioFacilitiesByStudioIDByQuery runs a custom query, returning results as StudioFacilities.
func StudioFacilitiesByStudioIDByQuery(ctx context.Context, db DB, studioID int, facilityIds []int) ([]*StudioFacilities, error) {
	// query
	var sqlstr = `SELECT ` +
		`sf.studio_facility_id, ` +
		`sf.facility_id, ` +
		`f.facility_name, ` +
		`sf.studio_facility_count, ` +
		`sf.studio_facility_price, ` +
		`sf.studio_facility_unit_hour, ` +
		`sf.created_at, ` +
		`sf.updated_at ` +
		`FROM ` +
		`studio_facility AS sf ` +
		`LEFT JOIN ` +
		`facility AS f ` +
		`ON  sf.facility_id = f.facility_id ` +
		`WHERE ` +
		`sf.studio_id = $1 ` +
		`AND sf.is_deleted IS FALSE ` +
		ints2Query("sf.facility_id", facilityIds) +
		`;`
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

