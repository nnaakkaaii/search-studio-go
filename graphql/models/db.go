package models

import "fmt"

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

func int2Query(key string, value *int) string {
	if value == nil {
		return ``
	}
	return fmt.Sprintf(`AND %s = %d `, key, *value)
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
