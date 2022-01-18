import datetime
import os
import csv
import argparse


def _parse_timedelta(txt: str) -> datetime.timedelta:
    return datetime.timedelta(
        hours=int(txt.split(':')[0]),
        minutes=int(txt.split(':')[1]),
    )


def preprocess(path: str) -> None:
    save_path = os.path.join(
        os.path.dirname(path),
        os.path.splitext(os.path.basename(path))[0] + '_processed' + os.path.splitext(os.path.basename(path))[1]
    )

    _base_date = datetime.datetime(1980, 1, 1)
    lines = []
    header = ['スタジオ名', '部屋名', '曜日', '予約枠ワークロード', '開始時刻', '終了時刻', '予約枠基本料金', '予約枠母数']

    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        for line in reader:
            studio_name = line['スタジオ名']
            room_names = line['部屋名'].split(',')
            days = line['何曜日'].split(',')
            _time_begin = _parse_timedelta(line['何時から'])
            _time_end = _parse_timedelta(line['何時まで'])
            time_unit = _parse_timedelta(line['何時間あたり'])
            slot_base_price = line['いくら']
            min_span = _parse_timedelta(line['最低何時間から'])
            slot_count = line['部屋数(missionなら全部1だけど)']

            workload = min(1., time_unit.seconds / min_span.seconds)

            time_span_seconds = int(_time_end.total_seconds() - _time_begin.total_seconds())
            time_unit_seconds = time_unit.seconds
            assert time_span_seconds % time_unit_seconds == 0
            for i in range(time_span_seconds // time_unit_seconds):
                for room_name in room_names:
                    for day in days:
                        time_begin = _base_date + (_time_begin + i * time_unit)
                        time_end = _base_date + (_time_begin + (1 + i) * time_unit)
                        assert (_time_begin + i * time_unit).days == 0
                        if (_time_begin + (1 + i) * time_unit).days == 0:
                            lines.append({
                                'スタジオ名': studio_name,
                                '部屋名': room_name,
                                '曜日': day,
                                '予約枠ワークロード': workload,
                                '開始時刻': time_begin.strftime('%H:%M:%S'),
                                '終了時刻': time_end.strftime('%H:%M:%S'),
                                '予約枠基本料金': slot_base_price,
                                '予約枠母数': slot_count,
                            })
                        elif (_time_begin + (1 + i) * time_unit).days == 1:
                            lines.append({
                                'スタジオ名': studio_name,
                                '部屋名': room_name,
                                '曜日': day,
                                '予約枠ワークロード': workload,
                                '開始時刻': time_begin.strftime('%H:%M:%S'),
                                '終了時刻': str(24 + time_end.hour) + time_end.strftime(':%M:%S'),
                                '予約枠基本料金': slot_base_price,
                                '予約枠母数': slot_count,
                            })
                        else:
                            assert False
    with open(save_path, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(lines)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--path',
        '-p',
        type=str,
        default=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'studio - 部屋予約.csv')),
    )
    args = parser.parse_args()

    preprocess(args.path)
