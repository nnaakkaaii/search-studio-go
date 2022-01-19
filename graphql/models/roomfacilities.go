package models

import "context"

// RoomFacilitiesByRoomIDByQueries runs a custom query, returning results as RoomFacilities.
func RoomFacilitiesByRoomIDByQueries(ctx context.Context, db DB, roomID int, facilityNames []string) ([]*RoomFacilities, error) {
	// query
	var sqlstr = `SELECT ` +
		`rf.room_facility_id, ` +
		`rf.facility_id, ` +
		`f.facility_name, ` +
		`rf.room_facility_description, ` +
		`rf.room_facility_count, ` +
		`rf.room_facility_price, ` +
		`rf.room_facility_unit_hour, ` +
		`rf.created_at, ` +
		`rf.updated_at ` +
		`FROM ` +
		`room_facility AS rf ` +
		`LEFT JOIN ` +
		`facility AS f ` +
		`ON  rf.facility_id = f.facility_id ` +
		`WHERE ` +
		`rf.room_id = $1 ` +
		`AND rf.is_deleted IS FALSE ` +
		strs2Query("f.facility_name", facilityNames) +
		`;`
	// run
	logf(sqlstr, roomID)
	rows, err := db.QueryContext(ctx, sqlstr, roomID)
	if err != nil {
		return nil, logerror(err)
	}
	defer rows.Close()
	// load results
	var res []*RoomFacilities
	for rows.Next() {
		var rf RoomFacilities
		// scan
		if err := rows.Scan(&rf.RoomFacilityID, &rf.FacilityID, &rf.FacilityName, &rf.RoomFacilityDescription, &rf.RoomFacilityCount, &rf.RoomFacilityPrice, &rf.RoomFacilityUnitHour, &rf.CreatedAt, &rf.UpdatedAt); err != nil {
			return nil, logerror(err)
		}
		res = append(res, &rf)
	}
	if err := rows.Err(); err != nil {
		return nil, logerror(err)
	}
	return res, nil
}

