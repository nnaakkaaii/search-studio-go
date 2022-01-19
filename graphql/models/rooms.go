package models

import "context"

// RoomsByStudioIDByQueries runs a custom query, returning results as Rooms.
func RoomsByStudioIDByQueries(ctx context.Context, db DB, studioID int, roomNames []string, minReservePeople *int, maxReservePeople *int, minFloorArea *float64) ([]*Rooms, error) {
	// query
	var sqlstr = `SELECT ` +
		`room_id, ` +
		`room_name, ` +
		`reservation_url, ` +
		`min_reservable_people, ` +
		`max_reservable_people, ` +
		`floor_area, ` +
		`created_at, ` +
		`updated_at ` +
		`FROM ` +
		`room ` +
		`WHERE ` +
		`studio_id = $1 ` +
		`AND is_deleted IS FALSE ` +
		strs2Query("room_name", roomNames) +
		maxOptionalInt2Query("min_reservable_people", minReservePeople) +  // minReservePeople は min_reservable_people より大きい必要がある
		minOptionalInt2Query("max_reservable_people", maxReservePeople) +
		minFloat2Query("floor_area", minFloorArea) +
		`;`
	// run
	logf(sqlstr, studioID)
	rows, err := db.QueryContext(ctx, sqlstr, studioID)
	if err != nil {
		return nil, logerror(err)
	}
	defer rows.Close()
	// load results
	var res []*Rooms
	for rows.Next() {
		var r Rooms
		// scan
		if err := rows.Scan(&r.RoomID, &r.RoomName, &r.ReservationURL, &r.MinReservablePeople, &r.MaxReservablePeople, &r.FloorArea, &r.CreatedAt, &r.UpdatedAt); err != nil {
			return nil, logerror(err)
		}
		res = append(res, &r)
	}
	if err := rows.Err(); err != nil {
		return nil, logerror(err)
	}
	return res, nil
}

