# Detailed Options Guide

This guide explains the supplied workflow. Change one setting at a time and compare outputs using the same input image and seed. Save a copy before changing connections.

## Image and prompts

- **Input image:** choose the image you want edited or animated. No example photograph is bundled.
- **Positive prompt:** describe the edit or motion you want. Be specific about what should change.
- **Negative prompt:** describe unwanted features. Its influence depends on the model and guidance settings.
- **Prompt history:** positive and negative fields start blank. The history node can save and reuse prompt pairs; local history files are not included.

## Generation controls

| Control | Meaning | Practical effect |
| --- | --- | --- |
| Seed | Starting random state | Keep it fixed for comparisons; identical seeds do not guarantee identical results across hardware or software changes. |
| Steps | Sampling iterations | More steps usually take longer; more is not automatically better. |
| CFG | Prompt guidance strength | Higher values can strengthen prompt influence but may introduce artifacts. |
| Denoise | Amount of regeneration | Lower values tend to preserve more of the encoded input; behavior depends on the model and conditioning. |
| Sampler / scheduler | Sampling method and noise schedule | Keep supplied defaults for your first result. |
| Dimensions | Image or video size | Larger dimensions usually require more memory and time. |

## Supplied sampler settings

| Node | Steps | CFG | Sampler | Scheduler | Denoise |
| --- | --- | --- | --- | --- | --- |
| 12 | 40 | 4 | euler | simple | 1 |

## Workflow-specific controls and behavior

1. Load an image. Enter an edit instruction in the positive prompt field of the prompt-history node.
2. Leave MODE / ImpactSwitch at 1 for the full instruction-edited output.
3. For mode 2, open the image in ComfyUI's Mask Editor, paint and save a mask, then set the switch to 2. This composites the generated edit into the original image through your mask.
4. Run and inspect the output. An empty mask can make mode 2 appear unchanged.

Automatic mode does not export an AI-selected object mask. The graph processes about 0.5 megapixels with 40 steps, CFG 4, Euler/simple, denoise 1. It uses no style LoRA. Filename capitalization must match the actual downloaded GGUF; select it again in the loader if necessary.


## Mode selection

| Mode | Output |
| --- | --- |
| 1 | Full instruction-edited image |
| 2 | Generated edit composited through your painted mask into the original image |

Mode 2 limits the final composite, not necessarily the model's internal editing operation. Check mask coverage and softened edges in the previews.

## Verification limits

Graph references were checked. These settings are documented from the uploaded JSON; GPU rendering, timings, and minimum VRAM were not verified during packaging.
