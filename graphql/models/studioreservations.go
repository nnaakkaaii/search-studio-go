package models

import "context"

// StudioReservationsByStudioIDByQueries runs a custom query, returning results as StudioReservations.
func StudioReservationsByStudioIDByQueries(ctx context.Context, db DB, studioID int, reservationIds []int) ([]*StudioReservations, error) {
	// query
	var sqlstr = `SELECT ` +
		`sr.studio_reservation_id, ` +
		`sr.reservation_id, ` +
		`r.reservation_name, ` +
		`sr.created_at, ` +
		`sr.updated_at ` +
		`FROM ` +
		`studio_reservation AS sr ` +
		`LEFT JOIN ` +
		`reservation AS r ` +
		`ON  sr.reservation_id = r.reservation_id ` +
		`WHERE ` +
		`sr.studio_id = $1 ` +
		`AND sr.is_deleted IS FALSE ` +
		ints2Query("sr.reservation_id", reservationIds) +
		`;`
	// run
	logf(sqlstr, studioID)
	rows, err := db.QueryContext(ctx, sqlstr, studioID)
	if err != nil {
		return nil, logerror(err)
	}
	defer rows.Close()
	// load results
	var res []*StudioReservations
	for rows.Next() {
		var sr StudioReservations
		// scan
		if err := rows.Scan(&sr.StudioReservationID, &sr.ReservationID, &sr.ReservationName, &sr.CreatedAt, &sr.UpdatedAt); err != nil {
			return nil, logerror(err)
		}
		res = append(res, &sr)
	}
	if err := rows.Err(); err != nil {
		return nil, logerror(err)
	}
	return res, nil
}

