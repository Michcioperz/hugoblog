{ pkgs ? import <nixpkgs> { config.allowBroken = builtins.currentSystem == "aarch64-darwin"; } }:
pkgs.mkShell {
  nativeBuildInputs = [ pkgs.hugo (pkgs.python3.withPackages  (ps: [ps.requests])) pkgs.proselint ];
}
