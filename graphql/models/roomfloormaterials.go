package models

import "context"

// RoomFloorMaterialsByRoomIDByQueries runs a custom query, returning results as RoomFloorMaterials.
func RoomFloorMaterialsByRoomIDByQueries(ctx context.Context, db DB, roomID int, floorMaterialNames []string) ([]*RoomFloorMaterials, error) {
	// query
	var sqlstr = `SELECT ` +
		`rfm.room_floor_material_id, ` +
		`rfm.floor_material_id, ` +
		`fm.floor_material_name, ` +
		`rfm.created_at, ` +
		`rfm.updated_at ` +
		`FROM ` +
		`room_floor_material AS rfm ` +
		`LEFT JOIN ` +
		`floor_material AS fm ` +
		`ON  rfm.floor_material_id = fm.floor_material_id ` +
		`WHERE ` +
		`rfm.room_id = $1 ` +
		`AND rfm.is_deleted IS FALSE ` +
		strs2Query("fm.floor_material_name", floorMaterialNames) +
		`;`
	// run
	logf(sqlstr, roomID)
	rows, err := db.QueryContext(ctx, sqlstr, roomID)
	if err != nil {
		return nil, logerror(err)
	}
	defer rows.Close()
	// load results
	var res []*RoomFloorMaterials
	for rows.Next() {
		var rfm RoomFloorMaterials
		// scan
		if err := rows.Scan(&rfm.RoomFloorMaterialID, &rfm.FloorMaterialID, &rfm.FloorMaterialName, &rfm.CreatedAt, &rfm.UpdatedAt); err != nil {
			return nil, logerror(err)
		}
		res = append(res, &rfm)
	}
	if err := rows.Err(); err != nil {
		return nil, logerror(err)
	}
	return res, nil
}

