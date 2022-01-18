package models

// Code generated by xo. DO NOT EDIT.

import (
	"context"
	"time"
)

// StudiosByName represents a row from 'public.studios_by_name'.
type StudiosByName struct {
	StudioID       int       `json:"studio_id"`         // studio_id
	StudioName     string    `json:"studio_name"`       // studio_name
	Introduction   string    `json:"introduction"`      // introduction
	Precaution     string    `json:"precaution"`        // precaution
	HomepageURL    string    `json:"homepage_url"`      // homepage_url
	Contact        string    `json:"contact"`           // contact
	AddressID      int       `json:"address_id"`        // address_id
	AddressName    string    `json:"address_name"`      // address_name
	CityID         int       `json:"city_id"`           // city_id
	CityName       string    `json:"city_name"`         // city_name
	PrefectureID   int       `json:"prefecture_id"`     // prefecture_id
	PrefectureName string    `json:"prefecture_name"`   // prefecture_name
	RentByMinHours float64   `json:"rent_by_min_hours"` // rent_by_min_hours
	CanFreeCancel  bool      `json:"can_free_cancel"`   // can_free_cancel
	CreatedAt      time.Time `json:"created_at"`        // created_at
	UpdatedAt      time.Time `json:"updated_at"`        // updated_at
}

// StudiosByNamesByStudioName runs a custom query, returning results as StudiosByName.
func StudiosByNamesByStudioName(ctx context.Context, db DB, studioName string) ([]*StudiosByName, error) {
	// query
	const sqlstr = `SELECT s.studio_id, ` +
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
		`FROM studio AS s ` +
		`LEFT JOIN address AS a ON s.address_id = a.address_id ` +
		`LEFT JOIN city AS c ON a.city_id = c.city_id ` +
		`LEFT JOIN prefecture AS p ON p.prefecture_id = c.prefecture_id ` +
		`WHERE s.studio_name = $1 AND s.is_deleted IS FALSE;`
	// run
	logf(sqlstr, studioName)
	rows, err := db.QueryContext(ctx, sqlstr, studioName)
	if err != nil {
		return nil, logerror(err)
	}
	defer rows.Close()
	// load results
	var res []*StudiosByName
	for rows.Next() {
		var sbn StudiosByName
		// scan
		if err := rows.Scan(&sbn.StudioID, &sbn.StudioName, &sbn.Introduction, &sbn.Precaution, &sbn.HomepageURL, &sbn.Contact, &sbn.AddressID, &sbn.AddressName, &sbn.CityID, &sbn.CityName, &sbn.PrefectureID, &sbn.PrefectureName, &sbn.RentByMinHours, &sbn.CanFreeCancel, &sbn.CreatedAt, &sbn.UpdatedAt); err != nil {
			return nil, logerror(err)
		}
		res = append(res, &sbn)
	}
	if err := rows.Err(); err != nil {
		return nil, logerror(err)
	}
	return res, nil
}