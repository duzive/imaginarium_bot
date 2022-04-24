import random
from filters.check import CheckFilter
from config.states import dp, upload
from vk_maria import types


@dp.message_handler(CheckFilter(["меню", "начать", "start"]))
def menu_handler(event: types.Message):
    photos = random.shuffle(list(range(1, 99)))
    attachment = []
    for i in range(5):
        attachment.append(upload.photo(f"/img/{photos[i]}.jpg"))

    event.answer("Держи свою колоду из пяти карт:", attachment=attachment)
