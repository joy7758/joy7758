# Citation And Bibliography Consistency Check

## Scope

This check covers the canonical TSE flagship manuscript and appendix together
with the dedicated TSE bibliography file:

- `manuscript/tse_flagship/tse_flagship_main.md`
- `manuscript/tse_flagship/tse_flagship_appendix.md`
- `submission/58_references_tse.bib`

## Citation Keys Used In The Manuscript

The following citation keys are actually used in the canonical TSE manuscript
package:

- `acm2020artifactbadging`
- `cheney2013provconstraints`
- `dona2018doip`
- `groth2013provoverview`
- `intoto2023spec`
- `kahn2006framework`
- `moreau2013provdm`
- `slsaBuildProvenance`
- `slsaProvenance`
- `soilandreyes2024evaluating`
- `torresarias2019intoto`

## Match Check Against `.bib`

| Citation key | Matching `.bib` entry present | Notes |
| --- | --- | --- |
| `acm2020artifactbadging` | yes | exact key match |
| `cheney2013provconstraints` | yes | exact key match |
| `dona2018doip` | yes | exact key match |
| `groth2013provoverview` | yes | exact key match |
| `intoto2023spec` | yes | exact key match |
| `kahn2006framework` | yes | exact key match |
| `moreau2013provdm` | yes | exact key match |
| `slsaBuildProvenance` | yes | exact key match |
| `slsaProvenance` | yes | exact key match |
| `soilandreyes2024evaluating` | yes | exact key match |
| `torresarias2019intoto` | yes | exact key match |

## Unused `.bib` Entries

- none

## Unresolved Or Suspicious Citation Patterns

- No unresolved citation keys were found in the canonical TSE manuscript or
  appendix.
- No `.bib` entries were found unused in the dedicated TSE bibliography file.
- One naive regex pattern can misread the profile version string
  `execution-evidence-operation-accountability-profile@0.1` as if `@0` were a
  citation key, but that string does not appear inside citation brackets and is
  not a real unresolved citation.
- Citation numbering order for final journal formatting still needs to be
  verified in the rendered output path because the current manuscript is still
  in Markdown form rather than final typeset form.

## Conclusion

The current citation package is internally consistent enough for final
formatting. The canonical TSE manuscript uses only citation keys that have
matching entries in `submission/58_references_tse.bib`, and the `.bib` file
contains no unused entries.
