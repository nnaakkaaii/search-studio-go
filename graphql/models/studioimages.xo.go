package models

// Code generated by xo. DO NOT EDIT.

import (
	"context"
	"time"
)

// StudioImages represents a row from 'public.studio_images'.
type StudioImages struct {
	StudioImageID int        `json:"studio_image_id"` // studio_image_id
	ImageID       int        `json:"image_id"`        // image_id
	ImageName     string     `json:"image_name"`      // image_name
	ImagePath     string     `json:"image_path"`      // image_path
	CreatedAt     time.Time  `json:"created_at"`      // created_at
	UpdatedAt     *time.Time `json:"updated_at"`      // updated_at
	Description   *string    `json:"description"`     // description
}

// StudioImagesByStudioID runs a custom query, returning results as StudioImages.
func StudioImagesByStudioID(ctx context.Context, db DB, studioID int) ([]*StudioImages, error) {
	// query
	const sqlstr = `SELECT si.studio_image_id, ` +
		`si.image_id, ` +
		`i.image_name, ` +
		`i.image_path, ` +
		`i.created_at, ` +
		`i.updated_at, ` +
		`si.description ` +
		`FROM studio_image AS si ` +
		`LEFT JOIN Image AS i ON si.image_id = i.image_id ` +
		`WHERE si.studio_id = $1 ` +
		`AND i.is_deleted IS FALSE;`
	// run
	logf(sqlstr, studioID)
	rows, err := db.QueryContext(ctx, sqlstr, studioID)
	if err != nil {
		return nil, logerror(err)
	}
	defer rows.Close()
	// load results
	var res []*StudioImages
	for rows.Next() {
		var si StudioImages
		// scan
		if err := rows.Scan(&si.StudioImageID, &si.ImageID, &si.ImageName, &si.ImagePath, &si.CreatedAt, &si.UpdatedAt, &si.Description); err != nil {
			return nil, logerror(err)
		}
		res = append(res, &si)
	}
	if err := rows.Err(); err != nil {
		return nil, logerror(err)
	}
	return res, nil
}
