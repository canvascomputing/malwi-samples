# malwi samples - AI Malware Detection

<img src="malwi-logo.png" alt="Logo">

<a href='https://huggingface.co/schirrmacher/malwi'><img src='https://img.shields.io/badge/%F0%9F%A4%97%20HF-Model-blue'></a>&ensp; 

This repository contains the malware samples for training [malwi](https://github.com/schirrmacher/malwi).

[malwi](https://github.com/schirrmacher/malwi) is specialized in detecting **zero-day vulnerabilities**, for classifying code as safe or harmful.

> ⚠️ WARNING: This repository contains **malicious software**. Do not execute the samples in an unprotected environment.

## Sources

The following datasets are used as a source for malicious samples:
- [pypi_malregistry](https://github.com/lxyeternal/pypi_malregistry)
- [DataDog malicious-software-packages-dataset](https://github.com/DataDog/malicious-software-packages-dataset)

## Next Steps

- Removing boilerplate code for creating a high density maliciousness dataset
- Creation of synthetic data