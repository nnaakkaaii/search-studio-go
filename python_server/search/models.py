from django.db import models
from django.core import validators


class Slot(models.Model):
    workload = models.FloatField(
        verbose_name="予約枠単位",
        null=False,
        help_text="連続するworkloadが1以上になって初めて予約が可能 つまり、3枠連続しないと予約できない枠のworkloadは0.33 1枠で予約できる枠のworkloadは1",
        validators=[
            validators.MinValueValidator(0.001)
        ],
    )
    time_begin = models.IntegerField(
        verbose_name="予約開始時間",
        null=False,
        help_text="予約開始時間。必須。",
        validators=[
            validators.MinValueValidator(1600000000),
            validators.MaxValueValidator(3200000000),
        ],
    )
    time_end = models.IntegerField(
        verbose_name="予約終了時間",
        null=False,
        help_text="予約終了時間。必須。",
        validators=[
            validators.MinValueValidator(1600000000),
            validators.MaxValueValidator(3200000000),
        ],
    )
    price = models.FloatField(
        verbose_name="部屋料金",
        null=False,
        help_text="ある部屋のある枠にかかる料金。必須。",
        validators=[
            validators.MinValueValidator(0),
            validators.MaxValueValidator(100000),
        ],
    )
    count = models.IntegerField(
        verbose_name="部屋残り枠数",
        null=False,
        help_text="部屋の残り枠数。必須。",
        validators=[
            validators.MinValueValidator(0),
            validators.MaxValueValidator(100),
        ],
    )


class Amenity(models.Model):
    AMENITY_SET = (
        ("stand-light", "スタンドライト"),
        ("color-light", "カラーライト"),
        ("phone-stand", "スマホ用三脚"),
        ("phone-lens", "スマホ用広角レンズ"),
        ("filming-equipment", "その他撮影機材"),
        ("dj", "DJセット"),
        ("mic", "マイク"),
        ("headset-mic", "ヘッドセットマイク"),
        ("mic-stand", "マイクスタンド"),
        ("keyboard", "キーボード"),
        ("music-stand", "譜面台"),
        ("projector", "プロジェクター"),
        ("monitor", "モニター"),
        ("bluray", "Blu-rayデッキ"),
        ("desk", "机"),
        ("chair", "イス"),
        ("whiteboard", "ホワイトボード"),
        ("partition", "パーテーション"),
        ("ballet-bar", "バレエバー"),
        ("tap-board", "タップ板"),
        ("yoga-mat", "ヨガマット"),
        ("yoga-goods", "ヨガグッズ"),
        ("training-goods", "トレーニンググッズ"),
        ("heel-cover", "ヒールカバー"),
        ("hanger", "ハンガー"),
        ("charger", "充電器"),
        ("alcohol", "アルコール消毒"),
    )
    name = models.CharField(
        verbose_name="アメニティ名",
        null=False,
        help_text="存在するアメニティを列挙する。必須。",
        choices=AMENITY_SET,
        max_length=64,
    )
    count = models.IntegerField(
        verbose_name="アメニティ総数",
        null=True,
        blank=True,
        help_text="アメニティの総数。不明な場合は空に。",
        validators=[
            validators.MinValueValidator(0),
            validators.MaxValueValidator(1000),
        ],
    )
    price = models.FloatField(
        verbose_name="アメニティ利用料金",
        null=False,
        help_text="アメニティの利用料金。必須。",
        validators=[
            validators.MinValueValidator(0),
            validators.MaxValueValidator(10000),
        ],
    )


class RoomFacility(models.Model):
    ROOM_FACILITY_SET = (
        ("two-sides-mirror", "鏡2面"),
        ("color-control", "明るさ調節"),
        ("mirror-ball", "ミラーボール"),
        ("phone-holder", "スマホ固定台"),
        ("mixer", "ミキサー"),
        ("cd", "CD利用"),
        ("ipod", "iPod利用"),
        ("bluetooth", "BlueTooth利用"),
        ("curtain", "カーテン/更衣スペース"),
    )
    name = models.CharField(
        verbose_name="部屋設備名",
        null=False,
        help_text="部屋の設備。必須。",
        choices=ROOM_FACILITY_SET,
        max_length=32,
    )
    count = models.IntegerField(
        verbose_name="部屋設備総数",
        null=True,
        blank=True,
        help_text="部屋の設備の総数。不明な場合は空に。",
        validators=[
            validators.MinValueValidator(0),
            validators.MaxValueValidator(1000),
        ],
    )
    price = models.FloatField(
        verbose_name="部屋設備利用料金",
        null=False,
        help_text="部屋の設備の利用料金。必須。",
        validators=[
            validators.MinValueValidator(0),
            validators.MaxValueValidator(10000),
        ],
    )


class StudioFacility(models.Model):
    STUDIO_FACILITY_SET = (
        ("male-changing-room", "男性更衣室"),
        ("female-changing-room", "女性更衣室"),
        ("shower-room", "シャワールーム"),
        ("smoking-room", "喫煙室"),
        ("waiting-space", "待合室"),
        ("parking", "駐車場"),
        ("wifi", "Wi-Fi"),
    )
    name = models.CharField(
        verbose_name="スタジオ設備名",
        null=False,
        help_text="スタジオの設備の名称。必須。",
        choices=STUDIO_FACILITY_SET,
        max_length=32,
    )
    count = models.IntegerField(
        verbose_name="スタジオ設備総数",
        null=True,
        blank=True,
        help_text="スタジオの設備の総数。不明な場合は空に。",
        validators=[
            validators.MinValueValidator(0),
            validators.MaxValueValidator(100),
        ],
    )
    price = models.FloatField(
        verbose_name="スタジオ設備料金",
        null=False,
        help_text="スタジオの設備の料金。必須。",
        validators=[
            validators.MinValueValidator(0),
            validators.MaxValueValidator(10000),
        ],
    )


class Image(models.Model):
    name = models.CharField(
        verbose_name="画像の名前",
        help_text="間取り、外観など画像の名前。必須。",
        null=False,
        blank=False,
        max_length=32,
    )
    description = models.TextField(
        verbose_name="画像の説明",
        help_text="表示したい画像の説明。必要ない場合は空に。",
        blank=True,
        null=True,
        max_length=300,
    )
    path = models.URLField(
        verbose_name="画像のパス",
        help_text="画像の保存されたパス。通常はAWSのS3へのパス。必須。",
        null=False,
        blank=False,
    )


class Room(models.Model):
    FLOOR_MATERIAL = (
        ("looring", "looring"),
        ("linoleum", "linoleum"),
        ("pvc-tile", "pvc-tile"),
    )
    name = models.CharField(
        verbose_name="部屋名",
        help_text="部屋の名称。必須。",
        null=False,
        max_length=64,
        blank=False,
    )
    images = models.ManyToManyField(Image)
    reserve_url = models.URLField(
        verbose_name="予約ページURL",
        help_text="予約ページへのURL。不明な場合は空に。",
        null=True,
        blank=True,
    )
    slots = models.ManyToManyField(Slot)
    min_people = models.IntegerField(
        verbose_name="予約可能最低人数",
        help_text="予約可能な最低人数。不明な場合は空に。",
        null=True,
        blank=True,
        validators=[
            validators.MinValueValidator(0),
            validators.MaxValueValidator(100),
        ],
    )
    max_people = models.IntegerField(
        verbose_name="予約可能最大人数",
        help_text="予約可能な最大人数。部屋の収容人数。不明な場合は空に。",
        null=True,
        blank=True,
        validators=[
            validators.MinValueValidator(1),
            validators.MaxValueValidator(101),
        ],
    )
    facilities = models.ManyToManyField(RoomFacility)
    floor_area = models.FloatField(
        verbose_name="床面積",
        help_text="スタジオの部屋の床面積。不明な場合は空に。",
        null=True,
        blank=True,
        validators=[
            validators.MinValueValidator(0),
        ],
    )
    floor_material = models.CharField(
        verbose_name="床素材",
        help_text="スタジオの部屋の床の素材。不明な場合は空に。",
        null=True,
        blank=True,
        choices=FLOOR_MATERIAL,
        max_length=32,
    )
    mirror_length = models.FloatField(
        verbose_name="鏡長さ",
        help_text="スタジオの部屋の鏡の長さ。不明な場合は空に。",
        null=True,
        blank=True,
        validators=[
            validators.MinValueValidator(0),
            validators.MaxValueValidator(100),
        ],
    )


class Station(models.Model):
    id = models.CharField(
        primary_key=True,
        verbose_name="駅ID",
        help_text="駅ID (S0001)。必須。",
        null=False,
        max_length=5,
        validators=[
            validators.MinLengthValidator(5),
        ],
    )
    name = models.CharField(
        verbose_name="駅名",
        help_text="駅名 (渋谷駅)。不明な場合は空に。",
        null=True,
        blank=True,
        max_length=32,
    )


class Line(models.Model):
    id = models.CharField(
        primary_key=True,
        verbose_name="路線ID",
        help_text="路線ID (A001)。必須。",
        null=False,
        max_length=4,
        validators=[
            validators.MinLengthValidator(4),
        ],
    )
    name = models.CharField(
        verbose_name="路線名",
        help_text="路線名 (山手線)。不明な場合は空に。",
        null=True,
        blank=True,
        max_length=32,
    )


class City(models.Model):
    id = models.CharField(
        primary_key=True,
        verbose_name="市区町村ID",
        help_text="市区町村ID (C0001)。必須。",
        null=False,
        max_length=5,
        validators=[
            validators.MinLengthValidator(5),
        ],
    )
    name = models.CharField(
        verbose_name="市区町村名",
        help_text="市区町村名 (渋谷区)。必須。",
        null=False,
        max_length=32,
    )


class Prefecture(models.Model):
    id = models.CharField(
        primary_key=True,
        verbose_name="都道府県ID",
        help_text="都道府県ID (P01)。必須。",
        null=False,
        max_length=3,
        validators=[
            validators.MinLengthValidator(3),
        ]
    )
    name = models.CharField(
        verbose_name="都道府県名",
        help_text="都道府県名 (東京都)。必須。",
        null=False,
        max_length=32,
    )


class Address(models.Model):
    address = models.CharField(
        verbose_name="住所",
        help_text="住所。必須。",
        null=False,
        max_length=256,
    )
    prefecture = models.ForeignKey(Prefecture, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    line = models.ManyToManyField(Line, on_delete=models.CASCADE)
    station = models.ManyToManyField(Station, on_delete=models.CASCADE)
    exit = models.CharField(
        verbose_name="出口名",
        help_text="出口名。不明な場合は空に。",
        null=True,
        blank=True,
        max_length=32,
    )
    minutes_from_station = models.FloatField(
        verbose_name="駅から徒歩何分か",
        help_text="駅から徒歩何分か",
        null=True,
        blank=True,
        validators=[
            validators.MinValueValidator(0),
            validators.MaxValueValidator(1000),
        ]
    )


class Payment(models.Model):
    id = models.CharField(
        primary_key=True,
        verbose_name="決済方法ID",
        help_text="決済方法ID (Q01)。必須。",
        null=False,
        max_length=3,
        validators=[
            validators.MinLengthValidator(3),
        ]
    )
    name = models.CharField(
        verbose_name="決済方法名",
        help_text="決済方法名 (オンライン決済)。必須。",
        null=False,
        max_length=32,
    )


class Reservation(models.Model):
    id = models.CharField(
        primary_key=True,
        verbose_name="予約方法ID",
        help_text="予約方法ID (R01)。必須。",
        null=False,
        max_length=3,
        validators=[
            validators.MinLengthValidator(3),
        ]
    )
    name = models.CharField(
        verbose_name="予約方法名",
        help_text="予約方法名 (サイト決済)。必須。",
        null=False,
        max_length=32,
    )


class Studio(models.Model):
    id = models.CharField(
        primary_key=True,
        verbose_name="スタジオID",
        help_text="スタジオID (99999999)。必須。",
        null=False,
        max_length=8,
        validators=[
            validators.MinLengthValidator(8),
        ],
    )
    name = models.CharField(
        verbose_name="スタジオ名",
        help_text="スタジオ名 (Mission)。必須。",
        null=False,
        max_length=256,
    )
    images = models.ManyToManyField(Image)
    introduction = models.TextField(
        verbose_name="紹介文",
        help_text="表示する紹介文を任意で記載する。markdownが利用可能。",
        null=True,
        blank=True,
        max_length=10000,
    )
    precaution = models.TextField(
        verbose_name="注意事項",
        help_text="表示する注意事項を任意で記載する。markdownが利用可能。",
        null=True,
        blank=True,
        max_length=10000,
    )
    homepage_url = models.URLField(
        verbose_name="ホームページURL",
        help_text="スタジオのホームページのURL。不明な場合は空に。",
        null=True,
        blank=True,
    )
    contact = models.CharField(
        verbose_name="連絡先",
        help_text="スタジオの電話番号。不明な場合は空に。",
        null=True,
        blank=True,
        max_length=11,
        validators=[
            validators.MinLengthValidator(10),
        ],
    )
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    rooms = models.ManyToManyField(Room)
    amenities = models.ManyToManyField(Amenity)
    facilities = models.ManyToManyField(StudioFacility)
    payment = models.ManyToManyField(Payment)
    reservation = models.ManyToManyField(Reservation)
    rent_by_hours = models.FloatField(
        verbose_name="表示予約可能最低時間",
        help_text="スタジオの表示上の予約可能な最低時間。表示上なので深夜などは考慮せず標準的な時間のみを示す。不明な場合は空に。",
        null=True,
        blank=True,
        validators=[
            validators.MinValueValidator(0),
            validators.MaxValueValidator(10),
        ],
    )
    free_cancel = models.BooleanField(
        verbose_name="キャンセル可否",
        help_text="指定期間外であればキャンセルが無料で可能か。不明な場合は空に。",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        verbose_name="掲載日",
        help_text="情報の掲載日。作成時に自動で追加されて以降編集されない。",
        null=False,
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name="更新日",
        help_text="情報の更新日。更新時に毎回自動で追加される。",
        null=False,
        auto_now=True,
    )
