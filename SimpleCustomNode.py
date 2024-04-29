class SimpleCustomNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": { "image_in" : ("IMAGE", {}) },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image_out",)
    FUNCTION = "invert"
    CATEGORY = "UserManager"

    def invert(self, image_in):
        image_out = 1 - image_in
        return (image_out,)