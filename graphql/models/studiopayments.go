package models

import "context"

// StudioPaymentsByStudioIDByQueries runs a custom query, returning results as StudioPayments.
func StudioPaymentsByStudioIDByQueries(ctx context.Context, db DB, studioID int, paymentIds []int) ([]*StudioPayments, error) {
	// query
	var sqlstr = `SELECT ` +
		`sp.studio_payment_id, ` +
		`sp.payment_id, ` +
		`p.payment_name, ` +
		`sp.created_at, ` +
		`sp.updated_at ` +
		`FROM ` +
		`studio_payment AS sp ` +
		`LEFT JOIN ` +
		`payment AS p ` +
		`ON  sp.payment_id = p.payment_id ` +
		`WHERE ` +
		`sp.studio_id = $1 ` +
		`AND sp.is_deleted IS FALSE ` +
		ints2Query("sp.payment_id", paymentIds) +
		`;`
	// run
	logf(sqlstr, studioID)
	rows, err := db.QueryContext(ctx, sqlstr, studioID)
	if err != nil {
		return nil, logerror(err)
	}
	defer rows.Close()
	// load results
	var res []*StudioPayments
	for rows.Next() {
		var sp StudioPayments
		// scan
		if err := rows.Scan(&sp.StudioPaymentID, &sp.PaymentID, &sp.PaymentName, &sp.CreatedAt, &sp.UpdatedAt); err != nil {
			return nil, logerror(err)
		}
		res = append(res, &sp)
	}
	if err := rows.Err(); err != nil {
		return nil, logerror(err)
	}
	return res, nil
}

