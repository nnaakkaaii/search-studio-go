psql -U root -d studio < "/commands/update_amenity_mst.sql" -v path="'/data/studio - アメニティ一覧.csv'" \
  && psql -U root -d studio < "/commands/update_city_mst.sql" -v path="'/data/studio - 市区町村一覧.csv'" \
  && psql -U root -d studio < "/commands/update_day_template_mst.sql" -v path="'/data/day_template.csv'" \
  && psql -U root -d studio < "/commands/update_facility_mst.sql" -v path="'/data/studio - 部屋設備一覧.csv'" \
  && psql -U root -d studio < "/commands/update_facility_mst.sql" -v path="'/data/studio - スタジオ設備一覧.csv'" \
  && psql -U root -d studio < "/commands/update_floor_material_mst.sql" -v path="'/data/studio - 部屋床素材一覧.csv'" \
  && psql -U root -d studio < "/commands/update_payment_mst.sql" -v path="'/data/studio - 支払い方法一覧.csv'" \
  && psql -U root -d studio < "/commands/update_railway_mst.sql" -v path="'/data/studio - 鉄道一覧.csv'" \
  && psql -U root -d studio < "/commands/update_reservation_mst.sql" -v path="'/data/studio - 予約方法一覧.csv'" \
  && psql -U root -d studio < "/commands/update_station_mst.sql" -v path="'/data/studio - 駅一覧.csv'" \
  && psql -U root -d studio < "/commands/update_studio.sql" -v path="'/data/studio - スタジオ.csv'" \
  && psql -U root -d studio < "/commands/update_studio_amenity.sql" -v path="'/data/studio - スタジオアメニティ.csv'" \
  && psql -U root -d studio < "/commands/update_studio_facility.sql" -v path="'/data/studio - スタジオ設備.csv'" \
  && psql -U root -d studio < "/commands/update_studio_image.sql" -v path="'/data/studio - スタジオ画像.csv'" \
  && psql -U root -d studio < "/commands/update_studio_payment.sql" -v path="'/data/studio - スタジオ支払い方法.csv'" \
  && psql -U root -d studio < "/commands/update_studio_reservation.sql" -v path="'/data/studio - スタジオ予約方法.csv'" \
  && psql -U root -d studio < "/commands/update_studio_station.sql" -v path="'/data/studio - スタジオ駅.csv'" \
  && psql -U root -d studio < "/commands/update_room.sql" -v path="'/data/studio - 部屋.csv'" \
  && psql -U root -d studio < "/commands/update_room_facility.sql" -v path="'/data/studio - 部屋設備.csv'" \
  && psql -U root -d studio < "/commands/update_room_image.sql" -v path="'/data/studio - 部屋画像.csv'" \
  && psql -U root -d studio < "/commands/update_room_slot.sql" -v path="'/data/studio - 部屋予約_processed.csv'" \
  && psql -U root -d studio < "/commands/update_day_template_mst.sql" -v path="'/data/studio - 曜日一覧.csv'"
