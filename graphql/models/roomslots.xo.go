package models

// Code generated by xo. DO NOT EDIT.

import (
	"context"
	"time"
)

// RoomSlots represents a row from 'public.room_slots'.
type RoomSlots struct {
	RoomSlotID      int        `json:"room_slot_id"`      // room_slot_id
	Date            time.Time  `json:"date"`              // date
	TimeBegin       time.Time  `json:"time_begin"`        // time_begin
	TimeEnd         time.Time  `json:"time_end"`          // time_end
	Workload        float64    `json:"workload"`          // workload
	SlotPrice       float64    `json:"slot_price"`        // slot_price
	RemainSlotCount int        `json:"remain_slot_count"` // remain_slot_count
	CreatedAt       time.Time  `json:"created_at"`        // created_at
	UpdatedAt       *time.Time `json:"updated_at"`        // updated_at
}

// RoomSlotsByRoomID runs a custom query, returning results as RoomSlots.
func RoomSlotsByRoomID(ctx context.Context, db DB, roomID int) ([]*RoomSlots, error) {
	// query
	const sqlstr = `SELECT ` +
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