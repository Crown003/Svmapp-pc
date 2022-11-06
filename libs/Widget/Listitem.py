from kivymd.uix.list import OneLineAvatarIconListItem
from kivy.properties import (
StringProperty,
)
class ListItemWithIcon(OneLineAvatarIconListItem):
    icon = StringProperty("android")
    text = StringProperty("hello")
    main_color = StringProperty()
    