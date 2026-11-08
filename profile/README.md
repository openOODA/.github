<div align="center">

<pre>
   ____  ____  ___  ____    ___   ___  ____    _
  / __ \/ __ \/ _ \/ __ \  / _ \ / _ \|  _ \  / \
 / /_/ / /_/ /  __/ / / / | | | | | | | | | |/ _ \
/_____/ .___/\___/_/ /_/  | |_| | |_| | |_| / ___ \
      /_/                   \___/ \___/|____/_/   \_\
</pre>

### openOODA — Capability-Secure Computing Stack (`L0`–`L7`)

[openooda.org](https://openooda.org) • [Overview (`llms.txt`)](https://openooda.org/llms.txt) • [Public Binary Hub (`install@hub`)](https://github.com/openOODA/install/releases/tag/hub) • [Package Catalog (`catalog`)](https://github.com/openOODA/catalog)

</div>

---

## Quick Install & Fedora-Style Group Bundles (`oopm`)

```sh
curl -fsSL https://openooda.org/install.sh | bash

oopm group list                  # List @core, @kernel, @os, @tools, @de, @apps, @cloud, @agents, @workstation, @all
oopm install @core               # L0 compiler (oodac), runtime (oodar), stdlib (oostd), CLI (ooda), oopm, oolsp, oomcp
oopm install @tools              # 39 capability-sandboxed L3 Unix, security, UI, and game-engine utilities
oopm install @workstation        # Full desktop stack (@core + @tools + @de + @apps)
oopm install @all                # All 93 canonical packages across L0–L7
```

---

## Replacing Implicit Trust with Verifiable Proof

Every process in **openOODA** is born with **zero privileges**. That is not an accident—it is the foundation of the type system and the operating environment.

Modern software infrastructure was built for an era of implicit human trust, where every library, script, or autonomous routine inherits the full ambient authority of the host process. In an era where AI systems and humans collaborate at machine speed, ambient authority means any component can touch everything.

**openOODA** rebuilds the computing stack from first principles across eight unified layers (`L0`–`L7`, `93` canonical product packages) so that authority is explicit, scoped, and provable at every boundary:

1. **Zero Ambient Authority & Single-Cycle 64-Bit Capability Register (`CapReg64` = `32 + 32 = 64`)**:
   - The lower 32 bits (`WHAT`) encode all **32 Root Capabilities (`0..31`)** (`13` Hardware + `19` Software/OS, fitting a single 32-lane GPU warp mask and 32-bit seccomp-BPF accumulator), while the upper 32 bits (`HOW & WHEN`) pack a **16-bit OODA Epoch** (instant revocation) + **8-bit Rights Mask** (`R/W/X/Delegate/Revoke` + privacy/zero-telemetry bits) + **8-bit Scope Badge** (`badge8`).
2. **CISA KEV Shield, Active Cyber Defense & Post-Quantum Provenance**:
   - Compile-time and runtime elimination of **CISA Known Exploited Vulnerabilities (KEV)** classes (`CWE-22` path traversal admission, `CWE-78` shell-free argv execution, `CWE-190`/`CWE-787` checked integer/slice arithmetic, `CWE-502` bounded `.oot` parsing), backed by bijective ELF binary polymorphism (`oodefense mutate`), Landlock `O_NOFOLLOW` `link_count==1` + Seccomp-BPF containment (`oosandbox kev-contain`), and post-quantum (`ML-KEM-768`, `ML-DSA-65`) + Stage0 `hex0` + Diverse Double-Compilation (`make det`) provenance (`oosign`, `ooprovenance`).
3. **Full-Stack `L0`–`L7` Hardware + Software Media, Surround Audio & Document Architecture (Zero `ffmpeg`)**:
   - Hardware codec probing (`NVENC`/`NVDEC`, `VAAPI`, `Vulkan`, `V4L2`/`MIPI-CSI`, `DRM`/`KMS`/`GOP`, `DMA-BUF`, `ALSA` 8ch) paired with native zero-FFmpeg codecs across **Surround/Spatial Audio** (`1.0`..`7.1.4` 12ch Atmos bed, Ambisonics, WAV/RF64, FLAC, QOA, DTS/DTS:X, AC-3/E-AC-3/TrueHD, IAMF, Opus, MP3, AAC + ITU-R BS.775 & HRTF), **Video & HDR** (MP4, MKV, MPEG-TS, AVI, Y4M, `.oov` with PQC frame seals, AV1/H.264/HEVC, HDR10, Dolby Vision), **Images** (`.qoi`, `.png` HDR, `.ppm`, `.bmp`, `.svg`, `.tga`, `.ico`, `.webp`, `.jpeg`, `.tiff`/`.dng` RAW), **Subtitles** (`.srt`, `.vtt`, `.ass`), **MIDI/DAW Synthesis** (`oodaw`), and **Office Documents** (`oooffice`: `.docx`/`.odt`/`.rtf`, `.pptx`/`.odp`, `.xlsx`/`.ods`/`.parquet`, `%PDF-1.7`/`.epub`).
4. **Power-of-2 Shape Ladder (`1/2/4/8/16/32/64/128/256`) & 8-Hat Adversarial Consensus (`oohat` + `oofalsify`)**:
   - Every `.oo` page obeys strict Power-of-2 structural laws and must pass deterministic double-compilation (`make det`), adversarial fuzzing (`oofalsify`), and the 8-Hat consensus gate (`oohat cycle` `quorum_mask=255`).

## The Unified 8-Layer Architecture (`L0`–`L7`)

| Layer | Organization | Repos | Architectural Focus |
| :--- | :--- | :---: | :--- |
| **Root** | [`@openOODA`](https://github.com/openOODA) | `6` | Governance & Quick Cards ([`openOODA`](https://github.com/openOODA/openOODA)), Package Index ([`catalog`](https://github.com/openOODA/catalog)), Public Binary Hub ([`install`](https://github.com/openOODA/install)), [`website`](https://openooda.org), [`status`](https://github.com/openOODA/status), [`bench`](https://github.com/openOODA/bench) |
| **`L0`** | [`@openOODA-core`](https://github.com/openOODA-core) | `7` | Capability-secure `.oo` compiler (`oodac`), native C/ASM/GPU/audio runtime (`oodar`), standard library (`oostd`), master CLI (`ooda`), package manager (`oopm`), `oolsp`, `oomcp` |
| **`L1`** | [`@openOODA-kernel`](https://github.com/openOODA-kernel) | `6` | UEFI boot (`ooboot`), capability microkernel (`ookernel`), HAL + DRM/KMS/HDR10 (`oohal`), IOMMU DMA isolation, and ring-3 drivers (`oodrv-storage`, `oodrv-io` V4L2/ALSA/DMA-BUF, `oodrv-virt`) |
| **`L2`** | [`@openOODA-OS`](https://github.com/openOODA-OS) | `9` | Zero-root system daemons (`ooinit`, `oovfs`, `oonetd`, `oosysbus` + PipeWire-style `media-graph`, `ooauthd`, `oohealthd`, `oocontainer`, `oollama` + `ingest-media`, `oomodemd`) |
| **`L3`** | [`@openOODA-tools`](https://github.com/openOODA-tools) | `39` | `7` Security hosts (`oodefense`, `oosandbox`, `ooprovenance`, `ooredact`, `oosign`, `oofirewall`, `oovault`) + `32` Unix, hardware (`oohw`), theme (`ootheme`), UI (`ooui`), and game-engine (`ooengine`) utilities |
| **`L4`** | [`@openOODA-DE`](https://github.com/openOODA-DE) | `8` | Wayland compositor + DMA-BUF/`.oov` capture (`oocomp`), panel/OSK (`oopanel`), privacy portals + `screencast`/`audio-capture` leases (`ooportal`), `ooterm`, `oofiles`, `oosettings`, `oobazaar`, `ooagent-hud` |
| **`L5`** | [`@openOODA-apps`](https://github.com/openOODA-apps) | `16` | `oomedia`, `oodaw`, `oocanvas`, `oooffice` (`docs`/`sheet`/`deck`/`notes`/`pdf`), `oobrowser`, `oostudio`, `ooflash`, `oochat`, `oopass`, `ookvm`, `oocamera`, and 5 flagship games (`ooemu`, `ooarcade`, `oocommand`, `oostrike`, `oovoxel`) |
| **`L6`** | [`@openOODA-cloud`](https://github.com/openOODA-cloud) | `8` | Content-addressed storage + `media-ingest` (`oostore`), PQC mesh + `media-relay` (`oomesh`), `oodb`, `oodeploy`, `oogateway`, `ooidentity`, `ootelemetry`, `oobilling` |
| **`L7`** | [`@openOODA-agents`](https://github.com/openOODA-agents) | `10` | 8-Hat consensus (`oohat`), CISA KEV + media fuzzing (`oofalsify`), `ooloop`, `ooswarm`, `oobench`, `ooquota`, `ooconsensus`, `oocode`, `oomemory`, `oogovern` |
