# E:\StabilityMatrix\Packages\ComfyUI\custom_nodes\PonySwitch.py

class PonySwitch:
    @staticmethod
    def INPUT_TYPES():
        return {
            "required": {
                "Toggle Switch": ("BOOLEAN", {"forceInput": True}),
                "Positive Pony Tags": ("STRING", {"default": "score_9, score_8_up, score_7_up, score_6_up", "multiline": True}),
                "Negative Pony Tags": ("STRING", {"default": "score_1, score_2, score_3, score_4, score_5, score_6", "multiline": True}),
                "Positive Prompt": ("STRING", {"default": '', "forceInput": True}),
                "Negative Prompt": ("STRING", {"default": '', "forceInput": True}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("Modified Positive Prompt", "Modified Negative Prompt")
    OUTPUT_IS_LIST = (False, False)
    FUNCTION = "compute"

    def __init__(self):
        self.name = "Pony Switch"

    def compute(self, **inputs):
        toggle_switch = inputs["Toggle Switch"]
        positive_pony_tags = inputs["Positive Pony Tags"]
        negative_pony_tags = inputs["Negative Pony Tags"]
        positive_prompt = inputs["Positive Prompt"]
        negative_prompt = inputs["Negative Prompt"]

        if toggle_switch:
            # Split tags into a list and strip whitespace
            positive_pony_tags = [tag.strip() for tag in positive_pony_tags.split('\n')]
            negative_pony_tags = [tag.strip() for tag in negative_pony_tags.split('\n')]

            # Add pony tags at the beginning of the positive and negative prompts with two new lines after
            modified_positive_prompt = " ".join(positive_pony_tags) + "\n\n" + positive_prompt
            modified_negative_prompt = " ".join(negative_pony_tags) + "\n\n" + negative_prompt
        else:
            # If toggle switch is off, return original prompts
            modified_positive_prompt = positive_prompt
            modified_negative_prompt = negative_prompt

        return (modified_positive_prompt, modified_negative_prompt)

# Required mapping for ComfyUI to recognize the node
NODE_CLASS_MAPPINGS = {
    "PonySwitch": PonySwitch
}
