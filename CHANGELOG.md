# Changelog

## 1.1.0 — Fixed output routing and integrated Clean Slate

- Update to the author's final Semi-AI workflow layout and settings, including denoise 0.9.
- Route the selected generated result to Save Image instead of the mask preview, restoring the generation dependency path through KSampler and VAE Decode.
- Replace the dynamic INT-typed ImpactSwitch with CleanSlateImageMode: two fixed IMAGE inputs, automatic/painted-mask selection and no growing unused input list.
- Integrate Clean Slate v0.2.0: five scoped clearing actions, five image inputs, five masks, separate/paired prompt support, two latents, confirmation/cancellation, preserved wires, persistent cleared previews and saved controller size.
- Keep active prompts and source-image selection blank; preserve local PromptHistory configuration without bundling any history.
- Update dependency and options documentation; add actual screenshots and a separate illustrative overview.

Validation: graph links/types and output reachability checked. The author confirmed generation in their setup; clean-machine dependency compatibility and minimum hardware requirements remain unverified.

## Initial repository package

- Published a cleaned workflow derived from the supplied source; see SOURCE.json for source checksum and recorded adjustments.
- Added setup, model, dependency, troubleshooting, and detailed settings guides.
- Added source checksum and graph validation script.
- Added GitHub issue templates.
- Clarified free local operation and current testing limitations.

## October 25, 2026 — Clean Slate connected

- Verified source image and both prompt links.
- Aligned utility node inside the first workflow group; added a rendered layout preview.

## Clean templates (October 25, 2026)

- Blank image/prompt defaults; Prompt History auto-save and recall preserved.
- Corrected negative Clean Slate link where necessary.
- Included PNG preview generated from the final clean graph.

- Highlighted free local inference and the absence of paid API requirements in the README.

## GitHub presentation and licensing (October 25, 2026)

- Added the official RebelTortuga mascot and optional Ko-fi link.
- Reorganized README sections and clarified the illustrative workflow preview.
- Added an MIT license for the authored workflow and repository documentation.
- Preserved workflow.json byte-for-byte during this presentation update.

