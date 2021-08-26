---
title: "Dealing with slow `perf script` on Debian"
date: 2021-08-26T23:10:00+0200
---
[Flamegraphs](https://www.brendangregg.com/flamegraphs.html) have become a pretty established way of visualizing performance of programs written in compiled languages. They give you a quick overview of how much time your program spends on certain subroutines. But preparing them is kind of an errand.

One of the possible sources of performance measurements for flamegraphs is the `perf` framework in Linux kernel. What you do is either wrap the run of your program in a `perf record` tool invocation, or you just tell the tool to attach to an existing process. Then you push the recorded data through the `perf script` command, which (according to my weak understanding) matches up symbols from executables and libraries with the addresses in the data. And finally there are some Perl scripts that generate the flamegraphs from that data.

Or you just use [`flamegraph` crate for Rust](https://github.com/flamegraph-rs/flamegraph) which does the above steps for you, and even has a Cargo integration if that's what you need. Notably, this solution still calls `perf script` for data processing.

And if you only ever did this on Debian or such Linux, perhaps you've accepted that the `perf script` step is extremely slow, and you can't do anything about this.

Unfortunately, I've been to NixOS, and my flamegraphs always finished processing in reasonable amount of time. So when I switched to Debian in the middle of doing some tinkering at work, I felt a massive difference: data that took up to 2 minutes before would just go on forever with no end in sight.

### Okay but why

I haven't flamegraphed the execution of `perf script`, but I went to look at `htop` and it seemed like on NixOS the process was steadily eating a bit over 100% CPU (a whole core) by itself, while on Debian it was eating very little and constantly starting new subprocesses, calling another program called `addr2line` with changing arguments. As you might expect, `addr2line` can be used to translate addresses in a binary to source code references using debug symbols.

From this observation you might realize that there might be something different about how `perf` is built on those platforms. And there is: on NixOS `perf` is built against libbfd, which is a library which can do what `addr2line` does. And it seems to work miracles compared to shelling out to `addr2line`.

And it's not like Debian maintainers don't know it. [They do know.](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=911815#15) But because the Linux kernel is licensed GPL v2 only, while libbfd is licensed GPL v3+, there is no overlap between those licenses, and the resulting program is not distributable. Or at least that's the argument given by a Debian maintainer.

Whether or not NixOS should do something about this is out of the scpoe of this post.

### Okay so how

(This is a rough writeup just to make the idea a bit more discoverable, so I'm assuming that the reader understands what the commands used here do. If not, I'm probably happy to assist, but still this writeup is more oriented towards people who feel comfortable compiling C++ abominations from shell.)

At first I thought the easiest way would be to just remove the lines mentioned in that Debian bug report and rebuild the linux-perf package. But turns out linux-perf is part of the package set of the kernel, and I have no clue how to build just one subpackage – I don't even know if it's possible, unless intentionally supported.

I feel like the easier way is to just get the sources of perf and run `make`.

To get source code of perf, you probably just want the kernel sources. On Debian, you can just run `apt source linux-perf-4.19` (where 4.19 is your kernel version), and you'll get a lot of auxilliary files and a directory with kernel sources. Or you can just download a tarball from kernel.org and get the same directory. Perf is located in `tools/perf` subdirectory.

To get the speedup from not shelling out to `addr2line` all the time, you need to install libbfd, and more importantly, it's development headers. On Debian, it's probably `sudo apt-get install libbfd-dev` that you want.

Once you have libbfd, run something like `make prefix=$HOME/.local install`. Yes, the word prefix is lowercase. `$HOME/.local` is just something that I consider to be a roughly good choice for where to install, because it's probably in your `$PATH` already on Debian. The make process will print a colorful table of which features are enabled and which aren't, and you want to make sure that bfd is green.

You will end up with the binary installed to `$prefix/bin/perf_`, presumably because we missed an environment variable somewhere. Just symlink it to either `perf` (if you're using that name in your scripts) or `perf_4.19` or such (if you're using (`cargo-`)`flamegraph`, cause it's gonna look for one with your kernel version in name) in your path.

And that should be it really. Have fun being more productive! I know I will.
