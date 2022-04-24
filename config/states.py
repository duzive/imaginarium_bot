import os

from vk_maria import Vk
from vk_maria.dispatcher.fsm import MemoryStorage
from vk_maria.dispatcher import Dispatcher
from vk_maria.upload import Upload


vk = Vk(os.getenv("VK_TOKEN"))
dp = Dispatcher(vk, MemoryStorage())
upload = Upload()
