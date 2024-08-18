# E:\StabilityMatrix\Packages\ComfyUI\custom_nodes\PonySwitch.py

class PonySwitch:
    @staticmethod
    def INPUT_TYPES():
        return {
            "required": {
                "Toggle Switch": ("BOOLEAN", {"forceInput": False}),
                "Positive Pony Tags": ("STRING", {"default": "score_9, score_8_up, score_7_up, score_6_up", "multiline": True}),
                "Negative Pony Tags": ("STRING", {"default": "score_1, score_2, score_3, score_4, score_5, score_6", "multiline": True}),
                "Positive": ("STRING", {"default": '', "forceInput": True}),
                "Negative": ("STRING", {"default": '', "forceInput": True}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("Positive", "Negative")
    OUTPUT_IS_LIST = (False, False)
    FUNCTION = "compute"

    def __init__(self):
        self.name = "Pony Switch"

    def compute(self, **inputs):
        toggle_switch = inputs["Toggle Switch"]
        positive_pony_tags = inputs["Positive Pony Tags"]
        negative_pony_tags = inputs["Negative Pony Tags"]
        positive = inputs["Positive"]
        negative = inputs["Negative"]

        if toggle_switch:
            # Split tags into a list and strip whitespace
            positive_pony_tags = [tag.strip() for tag in positive_pony_tags.split('\n')]
            negative_pony_tags = [tag.strip() for tag in negative_pony_tags.split('\n')]

            # Add pony tags at the beginning of the positive and negative  s with two new lines after
            positive = " ".join(positive_pony_tags) + "\n\n" + positive
            negative = " ".join(negative_pony_tags) + "\n\n" + negative
        else:
            # If toggle switch is off, return original  s
             positive = positive
             negative = negative

        return (positive, negative)

# Required mapping for ComfyUI to recognize the node
NODE_CLASS_MAPPINGS = {
    "PonySwitch": PonySwitch
}
