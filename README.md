# PonySwitch Node

<p align="center">
  <img src="https://github.com/user-attachments/assets/913cb1f6-2423-4e9d-b579-ac1d92801228"/>
</p>

The PonySwitch node is a custom node for ComfyUI that modifies prompts based on a toggle switch and adds configurable pony tags.

I found it cumbersome switching the pony tags in the prompt between Pony based models and SDXL based models. 

I had a group of nodes that did the same thing but wanted it to be neater so I have created this.

Uses a Boolean switch that adds or removes the tags at the front of the prompt.

You can change which tags you wish to use right on the widget.

<p align="center">
  <img src="https://github.com/user-attachments/assets/2e2ac63e-a684-4c12-afac-c462b8f3d2e4"/>
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/b8c52ca3-b326-45e5-bf0d-fc76e2d177e2"/>
</p>

## Features

- **Toggle Switch**: Enables or disables the addition of pony tags to prompts.
- **Positive Pony Tags**: Configurable tags added to the beginning of the positive prompt.
- **Negative Pony Tags**: Configurable tags added to the beginning of the negative prompt.
- **Positive and Negative Prompts**: Input prompts that are modified based on the toggle state.

## Installation

1. Git clone https://github.com/ImmortalPie/ComfyUI-PonySwitch into your `custom_nodes` directory of ComfyUI.
2. Restart ComfyUI to load the new node.

or just copy the ComfyUI-PonySwitch.py into the custom nodes folder.

## Usage

1. **Toggle Switch**: Turn on to prepend pony tags to prompts, or off to use the prompts as-is.
2. **Positive Pony Tags**: Enter tags for the positive prompt, separated by commas.
3. **Negative Pony Tags**: Enter tags for the negative prompt, separated by commas.
4. **Positive and Negative Prompts**: Connect your string prompts to these inputs.
5. **Modified prompt outputs**: Connect these to your positive and negative clip text encode.
