package models

import "context"

// GetStudiosByQueries runs a custom query, returning results as Studios.
func GetStudiosByQueries(ctx context.Context, db DB, studioNames []string, prefectureIds []int, cityIds []int) ([]*Studios, error) {
	// query
	 var sqlstr = `SELECT ` +
		`s.studio_id, ` +
		`s.studio_name, ` +
		`s.introduction, ` +
		`s.precaution, ` +
		`s.homepage_url, ` +
		`s.contact, ` +
		`a.address_id, ` +
		`a.address_name, ` +
		`c.city_id, ` +
		`c.city_name, ` +
		`p.prefecture_id, ` +
		`p.prefecture_name, ` +
		`s.rent_by_min_hours, ` +
		`s.can_free_cancel, ` +
		`s.created_at, ` +
		`s.updated_at ` +
		`FROM ` +
		`studio AS s ` +
		`LEFT JOIN ` +
		`address AS a ` +
		`ON  s.address_id = a.address_id ` +
		`LEFT JOIN ` +
		`city AS c ` +
		`ON  a.city_id = c.city_id ` +
		`LEFT JOIN ` +
		`prefecture AS p ` +
		`ON  p.prefecture_id = c.prefecture_id ` +
		`WHERE ` +
		`s.is_deleted IS FALSE ` +
		strs2Query("s.studio_name", studioNames) +
	 	ints2Query("c.city_id", cityIds) +
	 	ints2Query("p.prefecture_id", prefectureIds) +
		`;`
	// run
	logf(sqlstr)
	rows, err := db.QueryContext(ctx, sqlstr)
	if err != nil {
		return nil, logerror(err)
	}
	defer rows.Close()
	// load results
	var res []*Studios
	for rows.Next() {
		var s Studios
		// scan
		if err := rows.Scan(&s.StudioID, &s.StudioName, &s.Introduction, &s.Precaution, &s.HomepageURL, &s.Contact, &s.AddressID, &s.AddressName, &s.CityID, &s.CityName, &s.PrefectureID, &s.PrefectureName, &s.RentByMinHours, &s.CanFreeCancel, &s.CreatedAt, &s.UpdatedAt); err != nil {
			return nil, logerror(err)
		}
		res = append(res, &s)
	}
	if err := rows.Err(); err != nil {
		return nil, logerror(err)
	}
	return res, nil
}

