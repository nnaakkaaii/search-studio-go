package models

import (
	"context"
)

// StudioStationRailwayExitsByStudioIDByQueries runs a custom query, returning results as StudioStationRailwayExits.
func StudioStationRailwayExitsByStudioIDByQueries(ctx context.Context, db DB, studioID int, stationIds []int, railwayIds []int, maxMinutesFromStation *int) ([]*StudioStationRailwayExits, error) {
	// query
	var sqlstr = `SELECT ` +
		`ssre.studio_station_railway_exit_id, ` +
		`ssre.station_railway_exit_id, ` +
		`sre.station_railway_id, ` +
		`sr.station_id, ` +
		`s.station_name, ` +
		`sr.railway_id, ` +
		`r.railway_name, ` +
		`sre.exit_id, ` +
		`e.exit_name, ` +
		`ssre.minutes_from_station, ` +
		`ssre.created_at, ` +
		`ssre.updated_at ` +
		`FROM ` +
		`studio_station_railway_exit AS ssre ` +
		`LEFT JOIN ` +
		`station_railway_exit AS sre ` +
		`ON ssre.station_railway_exit_id = sre.station_railway_exit_id ` +
		`LEFT JOIN ` +
		`station_railway AS sr ` +
		`ON sre.station_railway_id = sr.station_railway_id ` +
		`LEFT JOIN ` +
		`station AS s ` +
		`ON sr.station_id = s.station_id ` +
		`LEFT JOIN ` +
		`railway AS r ` +
		`ON sr.railway_id = r.railway_id ` +
		`LEFT JOIN ` +
		`exit AS e ` +
		`ON sre.exit_id = e.exit_id ` +
		`WHERE ` +
		`ssre.studio_id = $1 ` +
		`AND ssre.is_deleted IS FALSE ` +
		ints2Query("sr.station_id", stationIds) +
		ints2Query("sr.railway_id", railwayIds) +
		maxInt2Query("ssre.minutes_from_station", maxMinutesFromStation) +
		`;`
	// run
	logf(sqlstr, studioID)
	rows, err := db.QueryContext(ctx, sqlstr, studioID)
	if err != nil {
		return nil, logerror(err)
	}
	defer rows.Close()
	// load results
	var res []*StudioStationRailwayExits
	for rows.Next() {
		var ssre StudioStationRailwayExits
		// scan
		if err := rows.Scan(&ssre.StudioStationRailwayExitID, &ssre.StationRailwayExitID, &ssre.StationRailwayID, &ssre.StationID, &ssre.StationName, &ssre.RailwayID, &ssre.RailwayName, &ssre.ExitID, &ssre.ExitName, &ssre.MinutesFromStation, &ssre.CreatedAt, &ssre.UpdatedAt); err != nil {
			return nil, logerror(err)
		}
		res = append(res, &ssre)
	}
	if err := rows.Err(); err != nil {
		return nil, logerror(err)
	}
	return res, nil
}

