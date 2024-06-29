# PonySwitch Node

<p align="center">
  <img src="https://github.com/ImmortalPie/ComfyUI-PonySwitch/assets/6324517/d85e7264-7165-4ff9-9c96-8931e2060784"/>
</p>

The PonySwitch node is a custom node for ComfyUI that modifies prompts based on a toggle switch and adds configurable pony tags.

I found it cumbersome switching the pony tags in the prompt between Pony based models and Sdxl based models. 

I had a group of nodes that did the same thing but wanted it to be neater so I have created this.

Uses a Boolean switch that adds or removes the tags at the front of the prompt.

You can change which tags you wish to use right on the widget.

<p align="center">
  <img src="https://github.com/ImmortalPie/ComfyUI-PonySwitch/assets/6324517/7dd0af57-a4a6-4e99-b6a9-cabe3cc9ff0b"/>
</p>

<p align="center">
  <img src="https://github.com/ImmortalPie/ComfyUI-PonySwitch/assets/6324517/6bcef9da-25c7-4c1a-b618-4cd7cc16e06e"/>
</p>

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
5. **Modified prompt outputs**: Connect these to your positive and negative clip text encode.

## Example usage

I like to change the Boolean to input so I can have the switch somewhere more convienient in my workflow.

<p align="center">
  <img src="https://github.com/ImmortalPie/ComfyUI-PonySwitch/assets/6324517/814d70f8-57fb-44b6-962e-3c4ed70ac039"/>
  <img src="https://github.com/ImmortalPie/ComfyUI-PonySwitch/assets/6324517/893b9bb2-05e0-4940-adc7-e41dffdfa529"/>
</p>

<p align="center">
</p>
