# Semi-AI Image Editing v1.1.0


- Update to the author's final Semi-AI workflow layout and settings, including denoise 0.9.
- Route the selected generated result to Save Image instead of the mask preview, restoring the generation dependency path through KSampler and VAE Decode.
- Replace the dynamic INT-typed ImpactSwitch with CleanSlateImageMode: two fixed IMAGE inputs, automatic/painted-mask selection and no growing unused input list.
- Integrate Clean Slate v0.2.0: five scoped clearing actions, five image inputs, five masks, separate/paired prompt support, two latents, confirmation/cancellation, preserved wires, persistent cleared previews and saved controller size.
- Keep active prompts and source-image selection blank; preserve local PromptHistory configuration without bundling any history.
- Update dependency and options documentation; add actual screenshots and a separate illustrative overview.

Validation: graph links/types and output reachability checked. The author confirmed generation in their setup; clean-machine dependency compatibility and minimum hardware requirements remain unverified.


Requires Clean Slate v0.2.0 or newer, the listed custom nodes and separately downloaded models. Download the attached ZIP, install dependencies, restart ComfyUI and load workflow.json. No paid generation API is required.
