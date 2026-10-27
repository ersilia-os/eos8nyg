# Ersilia Reference Library Similarity

Retrieves the 100 nearest neighbours of a query molecule in the Ersilia Reference Library, a set of 1.36 million compounds maintained by Ersilia. Three learned embeddings are searched independently, namely CLAMP for bioactivity, SAND for 3D shape and Mol-JEPA for predicted biological context, and their rankings are fused into one list. Ersilia built the search with LazySim, which indexes each embedding with turbovec 4-bit quantization.

This model was incorporated on 2026-10-19.Last packaged on 2026-10-20.

## Information
### Identifiers
- **Ersilia Identifier:** `eos8nyg`
- **Slug:** `reference-library-similarity`

### Domain
- **Task:** `Sampling`
- **Subtask:** `Similarity search`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Similarity`, `Embedding`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `100`
- **Output Consistency:** `Fixed`
- **Interpretation:** The 100 closest compounds in the Ersilia Reference Library, fused across the CLAMP, SAND and Mol-JEPA rankings.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| smi_00 | string |  | Library compound ranked 0 by reciprocal rank fusion of the CLAMP, SAND and Mol-JEPA searches |
| smi_01 | string |  | Library compound ranked 1 by reciprocal rank fusion of the CLAMP, SAND and Mol-JEPA searches |
| smi_02 | string |  | Library compound ranked 2 by reciprocal rank fusion of the CLAMP, SAND and Mol-JEPA searches |
| smi_03 | string |  | Library compound ranked 3 by reciprocal rank fusion of the CLAMP, SAND and Mol-JEPA searches |
| smi_04 | string |  | Library compound ranked 4 by reciprocal rank fusion of the CLAMP, SAND and Mol-JEPA searches |
| smi_05 | string |  | Library compound ranked 5 by reciprocal rank fusion of the CLAMP, SAND and Mol-JEPA searches |
| smi_06 | string |  | Library compound ranked 6 by reciprocal rank fusion of the CLAMP, SAND and Mol-JEPA searches |
| smi_07 | string |  | Library compound ranked 7 by reciprocal rank fusion of the CLAMP, SAND and Mol-JEPA searches |
| smi_08 | string |  | Library compound ranked 8 by reciprocal rank fusion of the CLAMP, SAND and Mol-JEPA searches |
| smi_09 | string |  | Library compound ranked 9 by reciprocal rank fusion of the CLAMP, SAND and Mol-JEPA searches |

_10 of 100 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `Internal`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos8nyg](https://hub.docker.com/r/ersiliaos/eos8nyg)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos8nyg.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos8nyg.zip)

### Resource Consumption
- **Model Size (Mb):** `1731`
- **Environment Size (Mb):** `587`
- **Image Size (Mb):** `4000.91`

**Computational Performance (seconds):**
- 10 inputs: `29.85`
- 100 inputs: `27.34`
- 10000 inputs: `542.83`

### References
- **Source Code**: [https://github.com/ersilia-os/lazy-sim](https://github.com/ersilia-os/lazy-sim)
- **Publication**: [https://github.com/ersilia-os/lazy-sim](https://github.com/ersilia-os/lazy-sim)
- **Publication Type:** `Other`
- **Publication Year:** `2026`
- **Ersilia Contributor:** [arnaucoma24](https://github.com/arnaucoma24)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [Non-commercial](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos8nyg
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos8nyg
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
