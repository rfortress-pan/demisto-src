This is a collection of scripts to facilitate quickly switching between multiple XSOAR development environments. It supports XSOAR 6 and XSOAR 8.  

## Requirements

- Linux / MacOS
 - Python 3
 - Pip

## Configuration

1. Save the scripts to your `~/.xsoar_dev` folder
		
		git clone https://github.com/rfortress-pan/demisto-src.git ~/.xsoar_dev

2. Add [`bashrc_include.sh`](https://github.com/rfortress-pan/demisto-src/blob/main/bashrc_include.sh) to `~/.bashrc` (Linux). Change to `~/.zshrc` for MacOS.

		echo "source ~/.xsoar_dev/bashrc_include.sh" >> ~/.bashrc

3. Load the commands (only required the first time you install).

		# For linux
		source ~/.bashrc

		# For MacOS
		source ~/.zshrc

4. Add a new XSOAR development environment

		demisto-src add

5. Remove the sample development environment (`rem`, `remove`, `del`, or `delete`)

		demist-src rem

6. Select your development environment

		demisto-src

7. Get the details of the currently selected development environment (`info`, `det` or `details`)

		demisto-src info
