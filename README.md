# Computer Architecture

This repository is a collection of projects and assignments developed to understand and implement core Computer Architecture concepts, including processor design, instruction set architecture and memory (cache) design. The projects are implemented in Python, with accompanying Assembly and C code.

## Project Structure

There are three projects inside this repository:

| Project | What it simulates | Entry point |
| --- | --- | --- |
| [`IAS Processor`](IAS%20Processor) | An IAS-architecture processor with its own assembler | `assembler.py`, `Processor.py` |
| [`MIPS processor`](MIPS%20processor) | A MIPS processor that executes machine code generated with MARS | `processor.py` |
| [`Cache - Memory design`](Cache%20-%20Memory%20design) | A set-associative cache with LRU replacement, driven by memory traces | `cache.py` |

1. **IAS Processor**: A Python simulator of a processor based on the IAS architecture, with an integrated assembler. The assembly program computes the sum of an exponentiated series (1^1 + 2^2 + ... + n^n); the equivalent C code is in `C_code.c`. See [Documentation.pdf](IAS%20Processor/Documentation.pdf).
2. **MIPS processor**: A Python simulator of a processor based on the MIPS architecture. It includes three programs, each with C code, MIPS Assembly (written for the MARS simulator) and the assembled binary: `I_power_i` (sum of n^n), `sum_of_GP` (sum of a geometric progression) and `tribonacci series` (nth Tribonacci number). See [Documentation.pdf](MIPS%20processor/Documentation.pdf).
3. **Cache - Memory design**: A cache simulator which gives the overall number of cache hits and cache misses for a given input (memory trace) using the LRU (Least Recently Used) replacement policy. See the [assignment statement](Cache%20-%20Memory%20design/assignment_cache.pdf) and the [report](Cache%20-%20Memory%20design/Assignment_Report.pdf).

For further details, please refer to the documentation inside each project.

## Prerequisites

- Python 3 (standard library only; no packages need to be installed).
- The [MARS](https://github.com/dpetersanderson/MARS) MIPS simulator, only if you want to modify the `.asm` sources and regenerate the MIPS binaries.

## Usage

### IAS Processor

`assembler.py` reads `instructions.txt` (lowercase), while the committed file is `Instructions.txt`. On case-sensitive systems (Linux/macOS), copy it first:

```bash
cd "IAS Processor"
cp Instructions.txt instructions.txt
python3 assembler.py   # assembles instructions.txt into binary_code.txt
python3 Processor.py   # runs binary_code.txt and prints the result
```

`Processor.py` can also be run on its own, using the committed `binary_code.txt`.

### MIPS processor

`processor.py` reads `binary_3.txt` (the Tribonacci program), which is in the `tribonacci series` folder, so run it from there:

```bash
cd "MIPS processor/tribonacci series"
python3 ../processor.py
```

The program asks for an integer input (via a MIPS syscall) while it runs, and writes an intermediate `byte_add_mem.txt` into the current folder. To run one of the other programs, change the filename on line 1 of `processor.py` to `binary_1.txt` (`I_power_i`) or `binary_2` (`sum_of_GP`; note that this file has no `.txt` extension) and run it from that program's folder in the same way.

### Cache - Memory design

```bash
cd "Cache - Memory design"
python3 cache.py
```

The trace file (`gcc.trace`) and the cache parameters (1 MB cache, 4-byte blocks, 32-way set associative) are set at the top of `cache.py`; edit them to try other configurations. The output is two numbers: the number of hits, followed by the number of misses. The available traces (`gcc`, `gzip`, `mcf`, `swim`, `twolf`) are in the project folder and in `traces/`.

## Known Limitations

The input files and parameters for the MIPS and cache simulators are hardcoded, so trying a different program, trace or configuration requires editing the source.

## License

No license has been specified for this repository.
