class SplitPrompt:
    # Define the required input for the node
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Prompt": ("STRING", {}),
                "max_lines": ("INT", {"default": 16, "min": 1, "max": 16, "step": 1}),
            }
        }
    _max_lines = 16

    # Define 15 output types (all as STRING)
    RETURN_TYPES = ("STRING",) * _max_lines

    RETURN_NAMES = [f"Prompt {i+1}" for i in range(_max_lines)]
    
    CATEGORY = "MitzyNodes/Text"
    

    FUNCTION = "split_text"

    def split_text(self, Prompt, max_lines):
        outputs = [""] * SplitPrompt._max_lines
        
        max_lines = min(max_lines, SplitPrompt._max_lines)
        
        lines = Prompt.split("\n", max_lines)

        for i, line in enumerate(lines):
            outputs[i] = line

        return tuple(outputs)


NODE_CLASS_MAPPINGS = {
    "SplitPrompt": SplitPrompt,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SplitPrompt": "Split Prompt",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
