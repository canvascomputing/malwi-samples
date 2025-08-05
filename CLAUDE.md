# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a malware sample repository for training the malwi AI malware detection system. It contains actual malicious Python packages collected from various sources for security research purposes.

⚠️ **CRITICAL SECURITY WARNING**: This repository contains dangerous malware samples. Never execute any code from the `/python/malicious/` or `/triage/` directories. These samples are for analysis and training purposes only.

## Project Structure

- `/python/malicious/`: Main collection of analyzed malicious Python packages
- `/triage/`: Unprocessed malware samples awaiting analysis (data* subdirectories)
- `/utils/`: Utility scripts for managing the malware collection
  - `refactor.py`: Uses LLM to comment out setup() calls in Python files
  - `flatten.sh`: Flattens nested directory structures
  - `count_and_move_files.sh`: Moves packages based on file count criteria

## Common Commands

This project uses `uv` as the Python package manager:

```bash
# Install dependencies
uv sync

# Run the refactor utility (requires Ollama with codestral model)
python utils/refactor.py <directory>

# Flatten nested directory structures
bash utils/flatten.sh

# Count and move files based on criteria
bash utils/count_and_move_files.sh
```

## Architecture and Key Concepts

### Malware Organization
- Packages are organized by name and version: `packagename_version/`
- Many samples are typosquatting attempts (e.g., variations of popular packages like BeautifulSoup, PyTorch)
- Common attack patterns include:
  - Reverse shells to attacker-controlled servers
  - Supply chain attacks via malicious setup.py
  - Data exfiltration attempts
  - Obfuscated malicious code

### Data Sources
- pypi_malregistry: Registry of malicious PyPI packages
- DataDog's malicious-software-packages-dataset

### Analysis Workflow
1. New samples are placed in `/triage/data*/` directories
2. Samples are flattened using `utils/flatten.sh` to normalize structure
3. The `refactor.py` utility can be used to safely comment out setup() calls
4. Analyzed samples are moved to `/python/malicious/`

## Important Notes

- This is a security research repository - all code should be treated as potentially harmful
- Never install or execute any packages from this repository
- When analyzing samples, focus on understanding attack patterns and detection methods
- The repository serves as training data for the malwi AI system to detect zero-day vulnerabilities