# PonySwitch Node

The PonySwitch node is a custom node for ComfyUI that modifies prompts based on a toggle switch and adds configurable pony tags.

I found it cumbersome switching the pony tags in the prompt between Pony based models and Sdxl based models. 

I had a group of nodes that did the same thing but wanted it to be neater so I have created this.

Uses a Boolean switch that adds or removes the tags at the front of the prompt.

You can change which tags you wish to use right on the widget.

## Features

- **Toggle Switch**: Enables or disables the addition of pony tags to prompts.
- **Positive Pony Tags**: Configurable tags added to the beginning of the positive prompt.
- **Negative Pony Tags**: Configurable tags added to the beginning of the negative prompt.
- **Positive and Negative Prompts**: Input prompts that are modified based on the toggle state.

## Installation

1. Place the `PonySwitch.py` file in your `custom_nodes` directory of ComfyUI.
2. Restart ComfyUI to load the new node.

## Usage

1. **Toggle Switch**: Turn on to prepend pony tags to prompts, or off to use the prompts as-is.
2. **Positive Pony Tags**: Enter tags for the positive prompt, separated by commas.
3. **Negative Pony Tags**: Enter tags for the negative prompt, separated by commas.
4. **Positive and Negative Prompts**: Connect your string prompts to these inputs.

## Example

When the toggle is on, the node adds the specified pony tags to the beginning of the prompts with two new lines separating them. When off, it outputs the prompts unchanged.
