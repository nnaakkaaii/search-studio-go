package models

import (
	"fmt"
)

const timeFormat = "15:04:05"

func str2Query(key string, value *string) string {
	if value == nil {
		return ``
	}
	return fmt.Sprintf(`AND %s = '%s' `, key, *value)
}

func strs2Query(key string, value []string) string {
	if len(value) == 0 {
		return ``
	}
	if len(value) == 1 {
		return fmt.Sprintf(`AND %s = '%s' `, key, value[0])
	}
	ret := `AND (`
	for i, v := range value {
		if i < len(value) - 1 {
			ret += fmt.Sprintf(`%s = '%s' OR `, key, v)
		} else {
			ret += fmt.Sprintf(`%s = '%s') `, key, v)
		}
	}
	return ret
}

func ints2Query(key string, value []int) string {
	if len(value) == 0 {
		return ``
	}
	if len(value) == 1 {
		return fmt.Sprintf(`AND %s = %d `, key, value[0])
	}
	ret := `AND (`
	for i, v := range value {
		if i < len(value) - 1 {
			ret += fmt.Sprintf(`%s = '%d' OR `, key, v)
		} else {
			ret += fmt.Sprintf(`%s = '%d') `, key, v)
		}
	}
	return ret
}

func minStr2Query(key string, value *string) string {
	if value == nil {
		return ``
	}
	return fmt.Sprintf(`AND %s >= '%s'`, key, *value)
}

func maxStr2Query(key string, value *string) string {
	if value == nil {
		return ``
	}
	return fmt.Sprintf(`AND %s <= '%s'`, key, *value)
}

func minInt2Query(key string, value *int) string {
	if value == nil {
		return ``
	}
	return fmt.Sprintf(`AND %s >= %d `, key, *value)
}

func maxInt2Query(key string, value *int) string {
	if value == nil {
		return ``
	}
	return fmt.Sprintf(`AND %s <= %d `, key, *value)
}

func minOptionalInt2Query(key string, value *int) string {
	if value == nil {
		return ``
	}
	return fmt.Sprintf(`AND (%s IS NULL OR %s >= %d) `, key, key, *value)
}

func maxOptionalInt2Query(key string, value *int) string {
	if value == nil {
		return ``
	}
	return fmt.Sprintf(`AND (%s IS NULL OR %s <= %d) `, key, key, *value)
}

func minFloat2Query(key string, value *float64) string {
	if value == nil {
		return ``
	}
	return fmt.Sprintf(`AND %s >= %f `, key, *value)
}
