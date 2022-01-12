package presenter

import "encoding/json"

func Jsonify(body interface{}) (data []byte, err error) {
	data, err = json.Marshal(body)
	return
}
