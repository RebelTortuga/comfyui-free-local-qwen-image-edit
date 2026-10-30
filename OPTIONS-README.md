# Options Guide

Load your image and enter an edit instruction in PromptHistory. Negative text describes unwanted changes. Histories stay local and are not included.

## Supplied settings

| Control | Value |
| --- | --- |
| Processing size | 0.5 megapixels |
| Seed | 123456789 (fixed) |
| Steps | 40 |
| CFG | 4 |
| Sampler / scheduler | euler / simple |
| Denoise | 0.9 |
| Final resize crop | disabled |
| Mask blur | 4 |

These values are from the author's final workflow; change one at a time while comparing the same source and seed. Lower denoise may retain more input detail but can weaken edits. Higher resolution increases memory use. Final resize restores original dimensions but cannot undo model-generated reframing.

## Image Edit Mode

- **1 Automatic:** save the complete instruction-edited image.
- **2 Painted mask:** paint and save a mask through Load Image's Mask Editor, then save the edit composited through that mask onto the original. An empty mask can leave the result unchanged.

Automatic mode does not export an AI-selected editable object mask. The painted mask limits the final composite, not necessarily the model's internal generation.

## Clean Slate

The five Reload buttons clear all connected content, image branches, both prompts, positive only, or negative only. Confirm with OK; Cancel or Esc exits before changes. Wires and saved files/history remain intact. Select a source image again before running after clearing it. Save the workflow to retain blank fields and your chosen controller size.
