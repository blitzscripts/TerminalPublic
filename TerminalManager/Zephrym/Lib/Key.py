"""_Summary
#* Default Terminal API:
    Used to set Keys
"""

class Key():
    @staticmethod
    def Press(vk_code):
        print("vk_code", vk_code,"has been sent")

    @staticmethod
    def Up(vk_code):
        print("vk_code", vk_code,"has been lifted")

    @staticmethod
    def Down(vk_code):
        print("vk_code", vk_code,"has been pressed")

    @staticmethod
    def Set(keyvk, type, id):
        print("Assigns skill or potion to key", keyvk,"with id of", id, "and type of", type)
