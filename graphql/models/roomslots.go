package models

import (
	"context"
	"time"
)

// RoomSlotsByRoomIDByQueries runs a custom query, returning results as RoomSlots.
func RoomSlotsByRoomIDByQueries(ctx context.Context, db DB, roomID int, dates []string, timeBegin *time.Time, timeEnd *time.Time, minSlotPrice *float64, minRemainSlotCount *int) ([]*RoomSlots, error) {
	// query
	var sqlstr = `SELECT ` +
		`room_slot_id, ` +
		`date, ` +
		`time_begin, ` +
		`time_end, ` +
		`workload, ` +
		`slot_price, ` +
		`remain_slot_count, ` +
		`created_at, ` +
		`updated_at ` +
		`FROM ` +
		`room_slot ` +
		`WHERE ` +
		`room_id = $1 ` +
		`AND is_deleted IS FALSE ` +
		strs2Query("date", dates) +
		maxOptionalTime2Query("time_begin", timeBegin) +
		minOptionalTime2Query("time_end", timeEnd) +
		minFloat2Query("slot_price", minSlotPrice) +
		minInt2Query("remain_slot_count", minRemainSlotCount) +
		`;`
	// run
	logf(sqlstr, roomID)
	rows, err := db.QueryContext(ctx, sqlstr, roomID)
	if err != nil {
		return nil, logerror(err)
	}
	defer rows.Close()
	// load results
	var res []*RoomSlots
	for rows.Next() {
		var rs RoomSlots
		// scan
		if err := rows.Scan(&rs.RoomSlotID, &rs.Date, &rs.TimeBegin, &rs.TimeEnd, &rs.Workload, &rs.SlotPrice, &rs.RemainSlotCount, &rs.CreatedAt, &rs.UpdatedAt); err != nil {
			return nil, logerror(err)
		}
		res = append(res, &rs)
	}
	if err := rows.Err(); err != nil {
		return nil, logerror(err)
	}
	return res, nil
}

